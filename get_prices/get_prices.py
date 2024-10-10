from math import ceil
import psycopg2
from psycopg2 import sql
from psycopg2._psycopg import Error
import settings
import requests
from time import sleep


def main():
    categories = []
    current_region_id = None
    resp_products_id = []
    continue_parse = True

    #Выборка последней добавленной цены в бд, что бы продолжить парсить цены
    last_product = (select_db('SELECT one.product_id, one.region_id, two.category_id FROM public.prices AS one LEFT JOIN '
                    'products AS two ON one.product_id = two.product_id ORDER BY date DESC LIMIT 1;'))

    for category in select_db('SELECT category_id FROM public.categories'):
        if last_product[0][2] == category[0] or not continue_parse:
            products = select_db(
                "SELECT product_id FROM public.products WHERE name IS NOT NULL AND url IS NOT NULL AND category_id = %s;",
                category[0])

            for region in select_db('SELECT one.region_id, one.city_id, two.shop_id FROM public.cities AS one LEFT JOIN public.cities_shops AS two ON one.city_id = two.city_id WHERE one.use IS NOT FALSE;'):

                if last_product[0][1] == region[0] or not continue_parse:
                    continue_parse = False
                    if current_region_id is None or region[0] != current_region_id:
                        current_region_id = region[0]
                        list_split_prod = list_split_products(products)
                        if list_split_prod is not None:
                            for product in list_split_prod:
                                pricies = get_price(region[0], region[1], region[2], product)
                                price_status = get_product_status(region[0], region[1], region[2], product, pricies)
                                insert_db("INSERT INTO public.prices (product_id, region_id, base_price, sale_price, product_status) VALUES {};", price_status)



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
            #print("Соединение с PostgreSQL закрыто")


def get_product_status(region_id, city_id, shop_id, products, list_prod_price_status):
    list_status = []
    response = requests.get('https://www.mvideo.ru/bff/products/statuses',
                            cookies=settings.get_cookies2(region_id, city_id, shop_id), params={'productIds': products},
                            headers=settings.get_headers())

    print(region_id, city_id) #Отладка
   # print(len(products)) #Отладка
    if response.status_code == 400:#Отладка
        print(response.status_code)#Отладка
        #print(response.json())#Отладка
        sleep(7.5)#Отладка
        get_product_status(region_id, city_id, shop_id, products, list_prod_price_status)#Отладка


    sleep(0.1)

    for status in response.json().get('body').get('statuses'):
        if status.get('productId') in list_prod_price_status:
            list_prod_price_status[status.get('productId')]['productStatus'] = status.get('productStatus')
            list_status.append((status.get('productId'), list_prod_price_status[status.get('productId')]['region_id'], list_prod_price_status[status.get('productId')]['basePrice'], list_prod_price_status[status.get('productId')]['salePrice'], list_prod_price_status[status.get('productId')]['productStatus']))

    return list_status




def get_price(region_id, city_id, shop_id, products):
    list_price = {}
    response = requests.get('https://www.mvideo.ru/bff/products/prices', cookies=settings.get_cookies(region_id, city_id, shop_id), params=settings.get_params(products), headers=settings.get_headers())
    #print(response.status_code)

    for price in response.json().get('body').get('materialPrices'):
        list_price[price.get('price').get('productId')] = {
            'productId': price.get('price').get('productId'),
            'region_id': region_id,
            'basePrice': price.get('price').get('basePrice'),
            'salePrice': price.get('price').get('salePrice'),
            'productStatus': 'None'
        }

    return list_price


if __name__ == '__main__':
    main()
