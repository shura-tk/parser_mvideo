def get_cookies(city_id, shop_id):
    cookies = {
    '_dc_gtm_UA-1873769-37': '1',
    '__SourceTracker': 'google__organic',
    'admitad_deduplication_cookie': 'google__organic',
    'afUserId': 'ca695dc8-8534-499d-b3c2-b01d47fc086b-p',
    '__lhash_': '724bb3884c9ce5e64b8738adaedf312e',
    'MVID_AB_PDP_CHAR': '2',
    'MVID_AB_SERVICES_DESCRIPTION': 'var4',
    'MVID_AB_TOP_SERVICES': '1',
    'MVID_ACTOR_API_AVAILABILITY': 'true',
    'MVID_BLACK_FRIDAY_ENABLED': 'true',
    'MVID_CART_AVAILABILITY': 'true',
    'MVID_CATALOG_STATE': '1',
    'MVID_CITY_ID': city_id,
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
    'MVID_KLADR_ID': '3400000100000',
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
    'MVID_REGION_ID': '23',
    'MVID_REGION_SHOP': shop_id,
    'MVID_SERVICES': '111',
    'MVID_SERVICES_MINI_BLOCK': 'var2',
    'MVID_TIMEZONE_OFFSET': '3',
    'MVID_WEBP_ENABLED': 'true',
    'MVID_WEB_SBP': 'true',
    'SENTRY_ERRORS_RATE': '0.1',
    'SENTRY_TRANSACTIONS_RATE': '0.5',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    '_gid': 'GA1.2.1750653394.1671086758',
    '_dc_gtm_UA-1873769-1': '1',
    '_sp_ses.d61c': '*',
    '_ym_uid': '1671086758241256681',
    '_ym_d': '1671086758',
    '_ym_isad': '2',
    'SMSError': '',
    'authError': '',
    'tmr_lvid': '86d44efafef1dc227f18713dfb8e5a94',
    'tmr_lvidTS': '1671086761222',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': '53e228fc-3e3e-4524-9675-640500c5aa7d',
    'flocktory-uuid': 'dd760104-d112-410a-abd5-02dc056a41ba-6',
    'uxs_uid': '2374c930-7c44-11ed-8d7c-2f22c2d01125',
    'advcake_track_id': 'ff146331-8ca4-07c3-b215-e4aa68cbee2f',
    'advcake_session_id': 'fe72c9fc-f7c6-f051-bdde-b19d0cc0a564',
    'AF_SYNC': '1671086761728',
    'flacktory': 'no',
    'BIGipServeratg-ps-prod_tcp80': '2449792010.20480.0000',
    'bIPs': '-1707567431',
    'mindboxDeviceUUID': '78c681e0-1435-4932-9448-89d37891fb82',
    'directCrm-session': '%7B%22deviceGuid%22%3A%2278c681e0-1435-4932-9448-89d37891fb82%22%7D',
    'MVID_ENVCLOUD': 'prod1',
    '_sp_id.d61c': '63c2e8c2-10f5-4d8b-be11-88143d38d1c1.1671086758.1.1671086777..12a6aba7-7279-403a-ba22-bd6f2b5286e8..1d693343-6624-4506-a11b-d6b2a7b95d6e.1671086757719.18',
    '_ga_BNX5WPP3YK': 'GS1.1.1671086746.30.1.1671086776.30.0.0',
    '_ga_CFMZTSS5FM': 'GS1.1.1671086745.30.1.1671086776.0.0.0',
    '_ga': 'GA1.2.1291648423.1670936769',
    'tmr_detect': '0%7C1671086782583'
}
    return cookies


def get_headers():
    headers = {
        'authority': 'www.mvideo.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://www.mvideo.ru/',
        'sec-ch-ua': '"Chromium";v="106", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/4.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 (Chromium GOST)',
    }

    return headers


def get_params(category_id, offset, limit):
    params = {
        'categoryId': {category_id},
        'offset': {offset},
        'limit': {limit},
        'filterParams': [
        'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        'WyJ6YWJyYXQtY2hlcmV6LTE1LW1pbnV0IiwiIiwiczk2MSJd'],
        'doTranslit': 'true'
    }

    return params
