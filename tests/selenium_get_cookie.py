import pickle
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    print(get_cookie_afUserID())


def get_cookie_afUserID():

    driver = webdriver.Chrome('c:\chromedriver')
    driver.get("http://www.mvideo.ru")
    sleep(10)
    afUserId = driver.get_cookie('afUserId').get('value')

    if afUserId is not None:
        return afUserId
    else:
        return False


if __name__ == '__main__':
    main()