from time import sleep

import requests
from netmiko import ConnectHandler
from pythonping import ping
from selenium import webdriver


def get_cookies(region_id, city_id, shop_id):
    cookies = {
        'afUserId': '75ebdb84-469b-4345-88fd-1a96811a89d5-p',
    '__lhash_': 'bd011c285168dc9192a133c8c0ad2a0a',
    'MVID_AB_PDP_CHAR': '2',
    'MVID_AB_SERVICES_DESCRIPTION': 'var4',
    'MVID_AB_TOP_SERVICES': '1',
    'MVID_ACTOR_API_AVAILABILITY': 'true',
    'MVID_BLACK_FRIDAY_ENABLED': 'true',
    'MVID_CART_AVAILABILITY': 'true',
    'MVID_CATALOG_STATE': '1',
    'MVID_CITY_ID': 'CityCZ_2128',
    'MVID_CREDIT_AVAILABILITY': 'true',
    'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
    'MVID_FILTER_CODES': 'true',
    'MVID_FILTER_TOOLTIP': '1',
    'MVID_FLOCKTORY_ON': 'true',
    'MVID_GEOLOCATION_NEEDED': 'true',
    'MVID_GIFT_KIT': 'true',
    'MVID_GLC': 'true',
    'MVID_GLP': 'true',
    'MVID_GTM_ENABLED': '011',
    'MVID_IMG_RESIZE': 'true',
    'MVID_INIT_DATA_OFF': 'true',
    'MVID_IS_NEW_BR_WIDGET': 'true',
    'MVID_KLADR_ID': '2300000100000',
    'MVID_LAYOUT_TYPE': '1',
    'MVID_LP_HANDOVER': '2',
    'MVID_LP_SOLD_VARIANTS': '3',
    'MVID_MCLICK': 'true',
    'MVID_MINDBOX_DYNAMICALLY': 'true',
    'MVID_MINI_PDP': 'true',
    'MVID_MOBILE_FILTERS': 'true',
    'MVID_NEW_ACCESSORY': 'true',
    'MVID_NEW_DESKTOP_FILTERS': 'true',
    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
    'MVID_NEW_LK_OTP_TIMER': 'true',
    'MVID_NEW_MBONUS_BLOCK': 'true',
    'MVID_PROMO_CATALOG_ON': 'true',
    'MVID_REGION_ID': '11',
    'MVID_REGION_SHOP': 'S911',
    'MVID_SERVICES': '111',
    'MVID_SERVICES_MINI_BLOCK': 'var2',
    'MVID_TIMEZONE_OFFSET': '3',
    'MVID_WEBP_ENABLED': 'true',
    'MVID_WEB_SBP': '2',
    'SENTRY_ERRORS_RATE': '0.1',
    'SENTRY_TRANSACTIONS_RATE': '0.5',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    '_gid': 'GA1.2.1157858374.1671373090',
    '_dc_gtm_UA-1873769-1': '1',
    '_ym_uid': '1671373090863782333',
    '_ym_d': '1671373090',
    '_sp_ses.d61c': '*',
    '_ym_isad': '2',
    '_ga': 'GA1.2.535661928.1671373090',
    '_dc_gtm_UA-1873769-37': '1',
    'SMSError': '',
    'authError': '',
    'tmr_lvid': '3a7ce44eb44c60c88a843dbd99e8c9af',
    'tmr_lvidTS': '1671373093550',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': '9d3fdc8d-22cf-4482-8999-611851a66fb6',
    'flocktory-uuid': '82013691-898f-4b0e-a522-3d135fbd0b69-3',
    'uxs_uid': 'cef1b560-7ede-11ed-9096-479f05ec9fab',
    'advcake_track_id': '1c316f0f-6e1f-39ad-44ba-0c16e1559b39',
    'advcake_session_id': '9fd3dffc-aca0-7201-fecd-683f7012ead4',
    'flacktory': 'no',
    'BIGipServeratg-ps-prod_tcp80': '1812257802.20480.0000',
    'bIPs': '434929338',
    'AF_SYNC': '1671373095295',
    'tmr_detect': '0%7C1671373095905',
    '_sp_id.d61c': 'c429758f-b0b2-451b-97d2-70801e42cbf0.1671373090.1.1671373099..4260366c-b2c1-48c8-b81d-0424163c94df..ee3ad10d-5566-4ad9-83a8-a673d8df96b5.1671373090034.34',
    'MVID_ENVCLOUD': 'prod2',
    '_ga_BNX5WPP3YK': 'GS1.1.1671373090.1.0.1671373098.52.0.0',
    '_ga_CFMZTSS5FM': 'GS1.1.1671373090.1.0.1671373098.0.0.0',
    'mindboxDeviceUUID': '838bce3b-e901-45a9-810d-4233ca58d668',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22838bce3b-e901-45a9-810d-4233ca58d668%22%7D'
    }

    cookies['MVID_REGION_ID'] = region_id
    cookies['MVID_CITY_ID'] = city_id
    cookies['MVID_REGION_SHOP'] = shop_id
    cookies['afUserId'] = 'e5bd9fc3-b24a-4e5b-9cba-038ff5cfef92-p'


    return cookies

def get_cookies2(region_id, city_id, shop_id):
    cookies = {
    'afUserId': '75ebdb84-469b-4345-88fd-1a96811a89d5-p',
    '__lhash_': 'bd011c285168dc9192a133c8c0ad2a0a',
    'MVID_AB_PDP_CHAR': '2',
    'MVID_AB_SERVICES_DESCRIPTION': 'var4',
    'MVID_AB_TOP_SERVICES': '1',
    'MVID_ACTOR_API_AVAILABILITY': 'true',
    'MVID_BLACK_FRIDAY_ENABLED': 'true',
    'MVID_CART_AVAILABILITY': 'true',
    'MVID_CATALOG_STATE': '1',
    'MVID_CITY_ID': 'CityCZ_2128',
    'MVID_CREDIT_AVAILABILITY': 'true',
    'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
    'MVID_FILTER_CODES': 'true',
    'MVID_FILTER_TOOLTIP': '1',
    'MVID_FLOCKTORY_ON': 'true',
    'MVID_GEOLOCATION_NEEDED': 'true',
    'MVID_GIFT_KIT': 'true',
    'MVID_GLC': 'true',
    'MVID_GLP': 'true',
    'MVID_GTM_ENABLED': '011',
    'MVID_IMG_RESIZE': 'true',
    'MVID_INIT_DATA_OFF': 'true',
    'MVID_IS_NEW_BR_WIDGET': 'true',
    'MVID_KLADR_ID': '2300000100000',
    'MVID_LAYOUT_TYPE': '1',
    'MVID_LP_HANDOVER': '2',
    'MVID_LP_SOLD_VARIANTS': '3',
    'MVID_MCLICK': 'true',
    'MVID_MINDBOX_DYNAMICALLY': 'true',
    'MVID_MINI_PDP': 'true',
    'MVID_MOBILE_FILTERS': 'true',
    'MVID_NEW_ACCESSORY': 'true',
    'MVID_NEW_DESKTOP_FILTERS': 'true',
    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
    'MVID_NEW_LK_OTP_TIMER': 'true',
    'MVID_NEW_MBONUS_BLOCK': 'true',
    'MVID_PROMO_CATALOG_ON': 'true',
    'MVID_REGION_ID': '11',
    'MVID_REGION_SHOP': 'S911',
    'MVID_SERVICES': '111',
    'MVID_SERVICES_MINI_BLOCK': 'var2',
    'MVID_TIMEZONE_OFFSET': '3',
    'MVID_WEBP_ENABLED': 'true',
    'MVID_WEB_SBP': '2',
    'SENTRY_ERRORS_RATE': '0.1',
    'SENTRY_TRANSACTIONS_RATE': '0.5',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    '_gid': 'GA1.2.1157858374.1671373090',
    '_dc_gtm_UA-1873769-1': '1',
    '_ym_uid': '1671373090863782333',
    '_ym_d': '1671373090',
    '_sp_ses.d61c': '*',
    '_ym_isad': '2',
    '_ga': 'GA1.2.535661928.1671373090',
    '_dc_gtm_UA-1873769-37': '1',
    'SMSError': '',
    'authError': '',
    'tmr_lvid': '3a7ce44eb44c60c88a843dbd99e8c9af',
    'tmr_lvidTS': '1671373093550',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': '9d3fdc8d-22cf-4482-8999-611851a66fb6',
    'flocktory-uuid': '82013691-898f-4b0e-a522-3d135fbd0b69-3',
    'uxs_uid': 'cef1b560-7ede-11ed-9096-479f05ec9fab',
    'advcake_track_id': '1c316f0f-6e1f-39ad-44ba-0c16e1559b39',
    'advcake_session_id': '9fd3dffc-aca0-7201-fecd-683f7012ead4',
    'flacktory': 'no',
    'BIGipServeratg-ps-prod_tcp80': '1812257802.20480.0000',
    'bIPs': '434929338',
    'AF_SYNC': '1671373095295',
    'tmr_detect': '0%7C1671373095905',
    '_sp_id.d61c': 'c429758f-b0b2-451b-97d2-70801e42cbf0.1671373090.1.1671373099..4260366c-b2c1-48c8-b81d-0424163c94df..ee3ad10d-5566-4ad9-83a8-a673d8df96b5.1671373090034.34',
    'MVID_ENVCLOUD': 'prod2',
    '_ga_BNX5WPP3YK': 'GS1.1.1671373090.1.0.1671373098.52.0.0',
    '_ga_CFMZTSS5FM': 'GS1.1.1671373090.1.0.1671373098.0.0.0',
    'mindboxDeviceUUID': '838bce3b-e901-45a9-810d-4233ca58d668',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22838bce3b-e901-45a9-810d-4233ca58d668%22%7D'
    }

    cookies['MVID_REGION_ID'] = region_id
    cookies['MVID_CITY_ID'] = city_id
    cookies['MVID_REGION_SHOP'] = shop_id
    cookies['afUserId'] = '7db2a645-c8f2-4d68-aaca-5c4c70ff62fc-p'

    return cookies


def get_cookie(region_id, city_id, shop_id, afUserID):
    responce = requests.get('https://www.mvideo.ru/', headers=get_headers())
    if responce.status_code == 200:
        cookie = {}
        for item in responce.cookies:
            cookie[item.name] = item.value

        cookie['MVID_REGION_ID'] = region_id
        cookie['MVID_CITY_ID'] = city_id
        cookie['MVID_REGION_SHOP'] = shop_id
        cookie['afUserId'] = afUserID
        return cookie


def get_cookie_from_selenium():

    driver = webdriver.Chrome('c:\chromedriver')
    driver.get("http://www.mvideo.ru")
    sleep(10)

    cookies = {}

    for coo in driver.get_cookies():
        cookies[coo.get('name')] = coo.get('value')

    return cookies


def edit_cookie(cookie, region_id, city_id, shop_id):

    cookie['MVID_REGION_ID'] = region_id
    cookie['MVID_CITY_ID'] = city_id
    cookie['MVID_REGION_SHOP'] = shop_id

    return cookie


def restart_mikrotik_interface():
    mikrotik_settings = {
        'device_type': 'mikrotik_routeros',
        'host': '192.168.1.2',
        'port': '22',
        'username': 'mvideo',
        'password': ''
    }
    sshCli = ConnectHandler(**mikrotik_settings)
    sshCli.send_command("/system script run RestartInterfaceLTE1")
    sshCli.disconnect()


def get_headers():
    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': '__lhash_=b9dee644c478e53efbd1f4c8712d0be3; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_2128; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_INIT_DATA_OFF=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=2300000100000; MVID_LAYOUT_TYPE=1; MVID_LP_HANDOVER=0; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=11; MVID_REGION_SHOP=S911; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod2',
        'referer': 'https://www.mvideo.ru/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Chromium GOST) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-set-application-id': '0e65bf90-11f7-43c6-9e35-ecfd9ce332f2',
    }

    return headers


def get_params(prosuct_id):
    params = {
        'productIds': prosuct_id,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true'
    }

    return params


def wait_ping():
    sleep(0.2)
    ex = False
    while not ex:
        try:
            ex = ping('ya.ru').success()
            sleep(0.5)
        except:
            pass