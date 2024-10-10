import re
from datetime import datetime

import math
import traceback
from time import sleep

import psycopg2
import requests
from psycopg2 import sql
from psycopg2._psycopg import Error

import settings


def main(last_city_id=None, last_category_id=None):
    # last_city_id = 'CityR_62' #city_id на котором остановился парсинг
    # last_category_id = '287' #category_id, на котором остановился парсинг

    for city in get_cities_id_db():  #Проходимся по каждому городу
        if last_city_id is None or last_city_id == city[0]:
            last_city_id = None
            for category in get_categories_db():  # Проходимся по каждой категории
                if last_category_id is None or last_category_id == category[0]:
                    last_category_id = None
                    get_products_id_mv(city[0], get_shop_id(city[0]), category[0])




def get_products_id_mv(city_id, shop_id, category_id, limit=72): #Получаем список id товаров с сайта mvideo
    shop_id = 'S903'
    #1. Получить первую партию id товаров из общего кол-ва
    #2. Получить пагинацию
    #3. Циклом пройтись для получения оставшихся товаров
    #4. Записать id's товаров в db
    try:
        response = requests.get('https://www.mvideo.ru/bff/products/listing', cookies=settings.get_cookies(city_id, shop_id), headers=settings.get_headers(), params=settings.get_params(category_id, 0, limit)).json()
        sleep(0.35)
        total_products = response.get('body').get('total')
        number_pages = math.ceil(total_products/limit)

        if total_products > 0:
            products_id_list = []
            products_id_list.extend([(x, category_id) for x in response.get('body').get('products')])

            for offset in range(limit, limit * number_pages - limit, limit):
                response = requests.get('https://www.mvideo.ru/bff/products/listing',
                                        cookies=settings.get_cookies(city_id, shop_id), headers=settings.get_headers(),
                                        params=settings.get_params(category_id, offset, limit)).json()
                sleep(0.35)
                products_id_list.extend([(x, category_id) for x in response.get('body').get('products')]) #Формируем список кортежей с product_id и region id, для добавления в db

            insert_db("INSERT INTO products (product_id, category_id) VALUES {} ON CONFLICT ON CONSTRAINT products_product_id_key DO NOTHING", products_id_list) # Вставка данных в db

        print(f"Time: {datetime.now()}; City: {city_id}; Category: {category_id}; Total products: {total_products};")
    except:
        print('При выполнении запроса к mvideo произошла ошибка')
        options = ('error', f'Не удалось получить products_id from mvideo.ru city_id = {city_id}; category_id = {category_id}', f'city_id = {city_id}; category_id = {category_id}')
        insert_db('INSERT INTO public.logs(status, description, options) VALUES {}', (options, ))
        sleep(10)
        main(city_id, category_id)



def get_shop_id(city_id):
    return select_db('SELECT city_id, shop_id FROM public.cities_shops WHERE city_id = %s ORDER BY shop_id LIMIT 1', city_id)[0][1]



def get_categories_db():  # Получаем список категорий с db
    return select_db('SELECT category_id FROM public.categories')


def get_cities_id_db():  # Получаем список городов c db
    return select_db('SELECT city_id FROM public.cities')


def select_db(sql, option=None):
    try:
        conn = psycopg2.connect(dbname='mvideo', user='postgres', password='IHR89653h,n!', host='127.0.0.1',
                                port='5432')
        cursor = conn.cursor()
        if option is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, (option, ))
        return cursor.fetchall()
    except (Exception, Error) as error:
        print(f"Ошибка при работе с PostgreSQL - {error}; Сбойный модуль - {traceback.extract_stack()[2]};")
    finally:
        if conn:
            cursor.close()
            conn.close()
            #print("Соединение с PostgreSQL закрыто")


def insert_db(sql_insert, data):
    # Добавляем полученные данные в БД
    try:
        conn = psycopg2.connect(dbname='mvideo', user='postgres', password='IHR89653h,n!', host='127.0.0.1',
                                port='5432')

        cursor = conn.cursor()
        insert = sql.SQL(sql_insert).format(
            sql.SQL(',').join(map(sql.Literal, data)))
        cursor.execute(insert)
        conn.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            #print("Соединение с PostgreSQL закрыто")



if __name__ == '__main__':
    main('CityR_123', '7956')