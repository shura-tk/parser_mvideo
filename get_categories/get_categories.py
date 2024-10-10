import re
import xml.etree.ElementTree as ET
import psycopg2
import wget as wget
from psycopg2 import sql
from psycopg2._psycopg import Error


def download_xml():
    # try:
    wget.download("https://www.mvideo.ru/sitemaps/sitemap-categories-www.mvideo.ru-1.xml", "data/mv_categories_urls.xml")
    # except:
    #     print('Не удалось скачать xml фал со ссылками на категории товаров!')


def get_categories():
    download_xml()
    categ_list = []
    tmp = []

    with open('data/mv_categories_urls.xml') as file:
        categories = ET.parse(file).getroot()

    for child in categories:
        for i in child:
            if i.tag == '{http://www.sitemaps.org/schemas/sitemap/0.9}loc':
                if '/f/category=' not in i.text:
                    tmp.append(i.text)

    for item in tmp:
        if ''.join(tmp).count(item) == 1:
            category_id = re.compile(r'\d*$').search(item)[0]
            categoru_url = item
            categ_list.append((category_id, categoru_url))

    return categ_list


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


def main():
    sql_one = 'INSERT INTO categories (category_id, url) VALUES {} ON CONFLICT ON CONSTRAINT category_category_id_key DO NOTHING'
    insert_db(sql_one, get_categories())


if __name__ == '__main__':
    main()