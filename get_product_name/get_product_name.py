import traceback
from time import sleep

from math import ceil

import psycopg2
import requests
from psycopg2 import sql
from psycopg2._psycopg import Error

import settings


def select_db(sql, option=None):
    try:
        conn = psycopg2.connect(dbname='mvideo', user='postgres', password='IHR89653h,n!', host='127.0.0.1',
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


def main():
    prod_list_insert_db = []
    count = select_db('SELECT count(id) FROM public.products WHERE name IS NULL or url IS NULL;')[0][0]

    for i in range(1, ceil(count / 72) + 1):
        product_list = []
        product_list.extend([prod[0] for prod in select_db(
            'SELECT product_id FROM public.products WHERE name IS NULL or url IS NULL LIMIT 72;')])

        if len(product_list) > 0:

            products = get_product_name(product_list).get('body').get('products')
            print(products)
            for product in products:
                prod_list_insert_db.append((product.get('productId'), product.get('name'),
                                            'https://www.mvideo.ru/products/' + product.get(
                                                'nameTranslit') + '-' + product.get('materialCisNumber')))

            if len(prod_list_insert_db) > 0:
                insert_db(
                    "INSERT INTO products (product_id, name, url) VALUES {} ON CONFLICT ON CONSTRAINT products_product_id_key DO UPDATE SET name = EXCLUDED.name, url = EXCLUDED.url",
                    prod_list_insert_db)

        else:
            print('Все поля столбцы в таблице товаров бд заполненны')


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


def get_product_name(product_id):
    sleep(3)
    res =  requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=settings.get_cookies(),
                         headers=settings.get_headers(), json=settings.get_json_data(product_id))
    print(res)
    return res.json()


if __name__ == '__main__':
    main()
