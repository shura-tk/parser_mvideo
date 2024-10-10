import json
import re
from random import randint

from time import sleep

import requests
from bs4 import BeautifulSoup
from psycopg2 import sql
from psycopg2._psycopg import Error

import settings
import get_shops_ids
import psycopg2
from contextlib import closing


def get_city():
    city_shop_ids = []

    response = requests.get('https://www.mvideo.ru/shops', cookies=settings.get_cookies(),
                            headers=settings.get_headers())
    sleep(randint(1, 3))
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        column = soup.find('div', class_="column")

        for item in column.find_all('a'):
            city_id = re.search(r"(?<=&cityId=).*$", item.get("href")).group(0)
            city_shop_ids.append((city_id, item.text, item.get('href')))

        return city_shop_ids

    else:
        print("Не удалось получить страницу со списоком городов")
        exit(0)




def insert_db(data):
    # Добавляем полученные данные в БД

    try:
        conn = psycopg2.connect(dbname='mvideo', user='postgres', password='IHR89653h,n!', host='127.0.0.1',
                                port='5432')

        cursor = conn.cursor()
        insert = sql.SQL(
            'INSERT INTO cities (city_id, city, url) VALUES {} ON CONFLICT ON CONSTRAINT cities_city_id_key DO NOTHING').format(
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


if __name__ == '__main__':
    insert_db(get_city())
