def get_cookies(city_id='CityCZ_978', shop_id='S063'):
    cookies = {
        'afUserId': 'ca695dc8-8534-499d-b3c2-b01d47fc086b-p',
        '__lhash_': '724bb3884c9ce5e64b8738adaedf312e',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'JSESSIONID': 'xQ2WjFdYz2vPLjNrkrGB1J1yNcp5J8T1hTZyBBtJ9fnC1Qq52q2L!1460690751',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_AB_TOP_SERVICES': '0',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_1272',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_GUEST_ID': '21936722715',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IMG_RESIZE': 'true',
        'MVID_INIT_DATA_OFF': 'false',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '3400000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_HANDOVER': '0',
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
        'MVID_REGION_SHOP': 'S912',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'bIPs': '672961728',
        'flacktory': 'no',
        'searchType2': '2',
        'MVID_ENVCLOUD': 'prod2',
        '_ga_BNX5WPP3YK': 'GS1.1.1669709915.28.1.1669717368.60.0.0',
        '_ga_CFMZTSS5FM': 'GS1.1.1669709915.28.1.1669717368.0.0.0'
    }
    return cookies


def get_headers():
    headers = {
        'authority': 'www.mvideo.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CREDIT_AVAILABILITY=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=21522820870; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; searchType2=2; _ym_uid=16641895541062015197; _ym_d=1664189554; uxs_uid=560893d0-3d89-11ed-92b2-e7b4aec9cc97; flocktory-uuid=58efd88f-e5b0-4159-bacc-1ae61f985985-2; afUserId=ca695dc8-8534-499d-b3c2-b01d47fc086b-p; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_MINDBOX_DYNAMICALLY=true; __ttl__widget__ui=1665748923827-4fc892c57bbb; cookie_ip_add=188.247.36.86; MVID_GLP=true; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; utm_term=330564f2e1b0794b14b21caaddce420a; MVID_GTM_ENABLED=011; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=53e228fc-3e3e-4524-9675-640500c5aa7d; MVID_GLC=true; advcake_track_id=2750879b-43fe-5bc4-3e1a-9a8404fef7bd; advcake_session_id=f0911fcf-1877-7702-d31e-7ad9cc7f7b70; MVID_SHOW_MFS=true; MVID_GEOLOCATION_NEEDED=false; MVID_LP_HANDOVER=1; MVID_CHECKOUT_REGISTRATION_AB_TEST=2; MVID_TIMEZONE_OFFSET=3; MVID_CITY_CHANGED=false; flacktory=no; MVID_GTM_BROWSER_THEME=1; SMSError=; authError=; _gid=GA1.2.2020732088.1669611028; tmr_lvid=659723c6ce7b05a6c5198647f608b8e4; tmr_lvidTS=1666163713653; MVID_AB_TOP_SERVICES=1; MVID_IMG_RESIZE=true; BIGipServeratg-ps-prod_tcp80=1208278026.20480.0000; bIPs=930512162; BIGipServeratg-ps-prod_tcp80_clone=1208278026.20480.0000; MVID_INIT_DATA_OFF=false; __lhash_=724bb3884c9ce5e64b8738adaedf312e; AF_SYNC=1669632005758; _ym_isad=2; MVID_CITY_ID=CityCZ_975; MVID_REGION_ID=1; _sp_ses.d61c=*; MVID_KLADR_ID=7700000000000; MVID_MULTIOFFER=true; MVID_REGION_SHOP=S002; JSESSIONID=pnMVjFHN4WkGMpPLXMhXfJCLFychkhrtJhQzGFFHKynvJnjGjpyf!1347216633; mindboxDeviceUUID=78c681e0-1435-4932-9448-89d37891fb82; directCrm-session=%7B%22deviceGuid%22%3A%2278c681e0-1435-4932-9448-89d37891fb82%22%7D; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpeQpDIV1xPUd8EBhCWTEbG0APL0F1UF0LRFxzKFUpE3NXZCdkFzsxLEgxaWlFRXJ3CT4xGjxoIWZJWiVJWFBqJh8XCHIkUA8NXD5Hb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTJCZiJmT1snRFxJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=V0EnFw==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpeQpDIV1xPUd8EBhCWTEbG0APL0F1UF0LRFxzKFUpE3NXZCdkFzsxLEgxaWlFRXJ3CT4xGjxoIWZJWiVJWFBqJh8XCHIkUA8NXD5Hb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTJCZiJmT1snRFxJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=V0EnFw==; _ga=GA1.2.906953078.1664189554; tmr_detect=0%7C1669715786966; cfidsgib-w-mvideo=JfvQ3qelWHgS4688C2O7mW35ShvyKpsFNOwV1vnijdCUOhBII3vM26ggn0VuQyoCOh05NYFrMCevZIkC8VA75L6S3dsI/Xpz4F+1UFrQHjzcr/PpgBcwNmHOLuWKcTc3UV+aHNPkbdUT9CxL/PqQB1QboniL4dk9Td0DPkY=; cfidsgib-w-mvideo=JfvQ3qelWHgS4688C2O7mW35ShvyKpsFNOwV1vnijdCUOhBII3vM26ggn0VuQyoCOh05NYFrMCevZIkC8VA75L6S3dsI/Xpz4F+1UFrQHjzcr/PpgBcwNmHOLuWKcTc3UV+aHNPkbdUT9CxL/PqQB1QboniL4dk9Td0DPkY=; gsscgib-w-mvideo=sPpuvx45khZnLQcjlWrPc5d5LF29ZLv+Y08t/jAP09wgCDH2EJxQKdo/qBvixdOsUSaczwrPUNn1dyN3YAgS3u363OWZ56DKNhfuxyilMekKMO6wS/d12EG4DuHz+q7KxJcdCfFJ3lsVQTbUFwSoXvZbMe9EZKlRz2KBvTn6LQF1INtemIbYr5sRzP4lnDu1PaBC3XDKWeybhy47KikDsZQmFWy4t+9JKyhhoqwQ9cU9XkAT3NjyfgZ7eBI9A/3Ywa4=; gsscgib-w-mvideo=sPpuvx45khZnLQcjlWrPc5d5LF29ZLv+Y08t/jAP09wgCDH2EJxQKdo/qBvixdOsUSaczwrPUNn1dyN3YAgS3u363OWZ56DKNhfuxyilMekKMO6wS/d12EG4DuHz+q7KxJcdCfFJ3lsVQTbUFwSoXvZbMe9EZKlRz2KBvTn6LQF1INtemIbYr5sRzP4lnDu1PaBC3XDKWeybhy47KikDsZQmFWy4t+9JKyhhoqwQ9cU9XkAT3NjyfgZ7eBI9A/3Ywa4=; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; _sp_id.d61c=b589ac88-82e2-4755-9ad1-b8c53b36cfd4.1664189555.27.1669716458.1669707166.26a5ed68-1c66-4650-88cd-536320c915ff.e4ce2380-be23-494d-8007-1acd52a4a889.4fdfad76-9198-435b-b976-5d975b8b439f.1669709915233.234; fgsscgib-w-mvideo=e6x129c919788786ed10f441c5966d55b429be64; fgsscgib-w-mvideo=e6x129c919788786ed10f441c5966d55b429be64; cfidsgib-w-mvideo=ZeJyVkesujbWcX9R8IpYk1ztgLvjoUTyaVBqa7GZUNJSF6GdXgXH0/uvzONzpCEMZpu1YebbYbmNYqeWzAdYgGuzBilagIYGi15I2SLgkemCnIBzBXCihm3GQlZPBZLVvb2xe3RbD8qxh+k4ih3/rsO60vYTJXdR+5UgRLM=; gssc218=; CACHE_INDICATOR=false; MVID_ENVCLOUD=prod2; _ga_CFMZTSS5FM=GS1.1.1669709915.28.1.1669716458.0.0.0; _ga_BNX5WPP3YK=GS1.1.1669709915.28.1.1669716458.60.0.0',
        'referer': 'https://www.mvideo.ru/',
        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 (Chromium GOST)',
    }

    return headers


def get_params(city_id):
    params = {
        'citystores': city_id,
        'cityId': city_id,
    }

    return params
