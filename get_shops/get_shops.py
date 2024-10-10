import math
from random import randint, random, uniform

import psycopg2
from psycopg2 import sql
from psycopg2._psycopg import Error
from time import sleep

import requests
from bs4 import BeautifulSoup
import settings

shops_id = []
cities_shops = []

def get_shops_id(city_id):

    response = requests.get('https://www.mvideo.ru/shops/store-list', params=settings.get_params(city_id), cookies=settings.get_cookies(city_id), headers=settings.get_headers()).text
    sleep(uniform(0.5, 2.5))
    count_pages = get_count_pagination(response)
    get_shops_id_current_page(response, city_id)

    if count_pages > 1:
        for i in range(2, count_pages+1):
            response = requests.get('https://www.mvideo.ru/sitebuilder/blocks/browse/store/locator/storePickerList.json.jsp', params={'tab': 'list', 'page': i}, cookies=settings.get_cookies(city_id), headers=settings.get_headers()).json().get('storeList')
            sleep(uniform(0.5, 2.5))
            get_shops_id_current_page(response, city_id)

    return shops_id


def get_shops_id_current_page(response, city_id):

    soup_shop_id = BeautifulSoup(response, 'lxml').find('div', id='js-stock-level-tooltips').find_all('li', class_='store-locator-list-item')

    for item in soup_shop_id:
        name_shop = item.find('h3').text.strip()
        address_shop = item.find('p').text.strip()
        url_shop = 'https://www.mvideo.ru' + item.find('a', class_='btn btn-fluid').get('href')
        id_shop = item.get('id')
        data = (id_shop, url_shop, name_shop, address_shop)

        shops_id.append(data)
        cities_shops.append((city_id, id_shop))



def get_count_pagination(response): # Возвращает число страниц
    soup = BeautifulSoup(response, 'lxml')
    return math.ceil(float(soup.find('div', class_='pagination-section-column pagination-section-info').text.split()[3])/24)


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
            print("Соединение с PostgreSQL закрыто")



def select_db():
    # Добавляем полученные данные в БД

    try:
        conn = psycopg2.connect(dbname='mvideo', user='postgres', password='IHR89653h,n!', host='127.0.0.1',
                                port='5432')

        cursor = conn.cursor()
        select = 'SELECT city_id FROM cities'
        cursor.execute(select)
        data = cursor.fetchall()
        return data

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Соединение с PostgreSQL закрыто")



if __name__ == '__main__':
    sql_one = 'INSERT INTO shops (shop_id, url, name, address) VALUES {} ON CONFLICT ON CONSTRAINT shops_shop_id_key DO NOTHING'
    sql_two = 'INSERT INTO cities_shops (city_id, shop_id) VALUES {} ON CONFLICT ON CONSTRAINT cities_id_to_shops_id_city_id_shop_id_key DO NOTHING'


    #insert_db(get_shops_id('CityCZ_975'))
    for city in select_db():
        shops_id = []
        cities_shops = []
        insert_db(sql_one, get_shops_id(city[0]))
        insert_db(sql_two, cities_shops)



