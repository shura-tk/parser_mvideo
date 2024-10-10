import threading
import traceback
from itertools import repeat
from math import ceil
import psycopg2
from psycopg2 import sql
from psycopg2._psycopg import Error
import settings
import requests
from time import sleep
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from functools import partial



def main():
    # with multiprocessing.Pool(10) as tr:
    #     tr.map(get_price, select_db('SELECT category_id FROM public.categories'))
    #     tr.close()
    #     tr.join()

    for category in select_db('SELECT category_id FROM public.categories ORDER BY last_scan ASC'):
        insert_db("UPDATE public.categories SET last_scan = now(), scan_status = 'scan' WHERE category_id = {};", (category[0],))
        data = []
        current_region_id = None

        print('Получение нового ip адреса')
        settings.restart_mikrotik_interface() #Перезапуск LTE1 интерфеса на микротик для получения нового ip
        settings.wait_ping() #Задержка, пока появится интернет.
        cookie = settings.get_cookie_from_selenium() # Получение cookei afUserID из браузера с использвоанием библиотеки selenium

        print(category[0])

        products = select_db(
            "SELECT product_id FROM public.products WHERE name IS NOT NULL AND url IS NOT NULL AND category_id = %s;",
            category[0])

        regions = select_db(
            'SELECT one.region_id, one.city_id, two.shop_id FROM public.cities AS one LEFT JOIN public.cities_shops AS two ON one.city_id = two.city_id WHERE one.use IS NOT FALSE ORDER BY one.region_id ASC;')

        # [data.append((i, products))for i in regions]

        for region in regions:
            if current_region_id is None or region[0] != current_region_id:
                current_region_id = region[0]
                data.append((region, products, cookie, category[0]))




        try:
            with multiprocessing.Pool(20) as tr:
                tr.starmap(get_price, data)
                tr.close()
                tr.join()

        except:
            print('Ошибка при выполнении многопоточной обработки')



def get_price(region, products, cookie, category):
    count_error = 0
    list_split_prod = list_split_products(products)
    if list_split_prod is not None:
        for product in list_split_prod:
            pricies = get_price_in_region(region[0], region[1], region[2], product, cookie)
            if pricies is not None:
                price_status = get_product_status(region[0], region[1], region[2], product, pricies, cookie)
                if pricies and price_status:
                    insert_db("INSERT INTO public.prices (product_id, region_id, base_price, sale_price, product_status) VALUES {};", price_status)

                    #!!!!!!!!!!!!!!!!!!!Данная конструкция должна была помечать в бд успешность или не успешность парсинга в категории. Она стоит не здесь. Нужно поставить в другой цикл
                    if count_error == 0:
                        insert_db("UPDATE public.categories SET last_scan = now(), scan_status= 'true' WHERE category_id = {};", (category,))
                    else:
                        insert_db("UPDATE public.categories SET last_scan = now(), scan_status = 'false' WHERE category_id = {};", (category,))
                else:
                    count_error = count_error + 1
                    options = ('error', 'Не удалось получить products_id from mvideo.ru', f"'region_id'='{region[0]}'; 'city_id'='{region[1]}'; 'category_id'='{category}'")
                    insert_db('INSERT INTO public.logs(status, description, options) VALUES {}', (options,))
                    print(f'Не удалось получить цены и статусы на товары в region_id {region[0]}')


def list_split_products(products=[], len_prod_json=72):
    res = []
    # products = [1, 2, 3, 4, 1, 2, 3]
    resp_products_id = []
    for i, product in enumerate(products):

        if len(resp_products_id) < len_prod_json:
            resp_products_id.append(product[0])
        elif len(resp_products_id) == len_prod_json:
            res.append(','.join(map(str, resp_products_id)))
            resp_products_id = [product[0]]

        if i + 1 == len(products):
            res.append(','.join(map(str, resp_products_id)))

    if len(res) == 0:
        return None
    else:
        return res


def select_db(sql, option=None):
    try:
        conn = psycopg2.connect(dbname='mvideo', user='postgres', password='IHR89653h,n!', host='localhost',
                                port='5432')
        cursor = conn.cursor()
        if option is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, (option,))
        return cursor.fetchall()
    except (Exception, Error) as error:
        print(f"Ошибка при работе с PostgreSQL - {error}; Сбойный модуль - {traceback.extract_stack()[2]};")
    finally:
        if conn:
            cursor.close()
            conn.close()
            # print("Соединение с PostgreSQL закрыто")


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
            # print("Соединение с PostgreSQL закрыто")


def get_product_status(region_id, city_id, shop_id, products, list_prod_price_status, cookie):
    list_status = []
    sleep(0.1)
    try:
        response = requests.get('https://www.mvideo.ru/bff/products/statuses',
                                cookies=settings.edit_cookie(cookie, region_id, city_id, shop_id), params={'productIds': products},
                                headers=settings.get_headers())

        if response.status_code == 200:
            # print(city_id)
            for status in response.json().get('body').get('statuses'):
                if status.get('productId') in list_prod_price_status:
                    list_prod_price_status[status.get('productId')]['productStatus'] = status.get('productStatus')
                    list_status.append(
                        (status.get('productId'), list_prod_price_status[status.get('productId')]['region_id'],
                         list_prod_price_status[status.get('productId')]['basePrice'],
                         list_prod_price_status[status.get('productId')]['salePrice'],
                         list_prod_price_status[status.get('productId')]['productStatus']))

            return list_status
        else:
            return False

    except:
        print('Сбой в получение статуса товара', response.status_code)
        return False


def get_price_in_region(region_id, city_id, shop_id, products, cookie):
    list_price = {}
    sleep(0.1)
    try:
        response = requests.get('https://www.mvideo.ru/bff/products/prices',
                                cookies=settings.edit_cookie(cookie, region_id, city_id, shop_id),
                                params=settings.get_params(products), headers=settings.get_headers())

        if response.status_code == 200:

            for price in response.json().get('body').get('materialPrices'):
                list_price[price.get('price').get('productId')] = {
                    'productId': price.get('price').get('productId'),
                    'region_id': region_id,
                    'basePrice': price.get('price').get('basePrice'),
                    'salePrice': price.get('price').get('salePrice'),
                    'productStatus': 'None'
                }
            return list_price
        else:
            return False
    except:
        print('Сбой в получении цен на товары')

        return False


if __name__ == '__main__':
    main()
