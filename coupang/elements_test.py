# coding: utf-8
import datetime
import os
import time
import warnings

import chromedriver_autoinstaller
import numpy as np
import pandas as pd
import pymysql
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
from urllib.request import urlretrieve

import datetime
import time

import requests

headers = {
    'authority': 'www.coupang.com',
    'accept': '*/*',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
chromedriver_autoinstaller.install(True)
warnings.simplefilter("ignore", category=pymysql.Warning)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'

WAITTIME = 5

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument('--incognito')
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-setuid-sandbox")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('user-agent={0}'.format(user_agent))

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}

driver = webdriver.Chrome(executable_path=f'./{chrome_ver}/chromedriver.exe', chrome_options=options,
                          desired_capabilities=caps)

page = 1
refresh_cnt = 5
keyword = input()
first_time = True
while True:
    driver.get(
        f"https://www.coupang.com/np/search?rocketAll=false&q={keyword}&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page={page}&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&component=&rating=0&sorter=scoreDesc&listSize=36")
    if first_time:
        driver.refresh()
        first_time = False
    list_all = driver.find_elements(By.XPATH, "//a[contains(@class,'search-product-link')]")
    list_rocket = driver.find_elements(By.XPATH,
                                       "//a[contains(@class,'search-product-link')]//span[contains(@class,'badge rocket')]//ancestor::a")
    page += 1
    not_rocket = [x for x in list_all if x not in list_rocket]

    product_list = [x.get_attribute('data-product-id') for x in not_rocket]
    item_list = [x.get_attribute('data-item-id') for x in not_rocket]
    vender_item_list = [x.get_attribute('data-vendor-item-id') for x in not_rocket]
    for product, item, vender_item in zip(product_list, item_list, vender_item_list):
        try:
            response = requests.get(
                f'https://www.coupang.com/vp/products/{product}/items/{item}/vendoritems/{vender_item}',
                headers=headers, timeout=5)
        except:
            continue

        print(response.status_code, datetime.datetime.now())
        time.sleep(.5)

    print([x.get_attribute('data-product-id') for x in not_rocket])
    print([x.get_attribute('data-item-id') for x in not_rocket])
    print([x.get_attribute('data-vendor-item-id') for x in not_rocket])

    driver.find_element(By.XPATH, "//a[contains(@class,'btn-next')]")
