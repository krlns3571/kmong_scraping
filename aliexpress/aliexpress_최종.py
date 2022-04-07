# coding: utf-8
import datetime
import os
import sys
import time
import warnings

import pandas as pd
import pymysql
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy.ext.declarative import declarative_base
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import chromedriver_autoinstaller
import xlsxwriter
import openpyxl

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  # 크롬드라이버 버전 확인
chromedriver_autoinstaller.install(True)


def explicitly_wait(driver, by, name):
    try:
        return WebDriverWait(driver, WAITTIME).until(EC.presence_of_element_located((by, name)))
    except Exception as e:
        raise ValueError(by, name)


pymysql.install_as_MySQLdb()

warnings.simplefilter("ignore", category=pymysql.Warning)

Base = declarative_base()
metadata = Base.metadata

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

WAITTIME = 15
if os.name == 'nt':
    CHROMEDRIVERPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver')
else:
    CHROMEDRIVERPATH = 'chromedriver'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument('--incognito')
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

# 링크 입력하셔서 사용하시면 되고, list에 여러개 입력 가능합니다
links = [
    "https://ko.aliexpress.com/item/1005003731563532.html?spm=a2g0o.productlist.0.0.33ebfea9nbIhkk&algo_pvid=993fd025-c7db-44ef-ad85-7f9cda2b89d4&algo_exp_id=993fd025-c7db-44ef-ad85-7f9cda2b89d4-8&pdp_ext_f=%7B%22sku_id%22%3A%2212000026966598087%22%7D&pdp_pi=28301.0%3B6512.0%3B-1%3B-1%40salePrice%3BKRW%3Bsearch-mainSearch",
    "https://ko.aliexpress.com/item/4000934672679.html?spm=a2g0o.productlist.0.0.1682fea97gLwOf&algo_pvid=b04f1c59-9b37-4e26-8776-d25209af7330&algo_exp_id=b04f1c59-9b37-4e26-8776-d25209af7330-2&pdp_ext_f=%7B%22sku_id%22%3A%2210000011289134527%22%7D&pdp_pi=-1%3B9002.0%3B-1%3B-1%40salePrice%3BKRW%3Bsearch-mainSearch",
    "https://ko.aliexpress.com/item/1005002615991860.html?spm=a2g0o.productlist.0.0.1682fea97gLwOf&algo_pvid=b04f1c59-9b37-4e26-8776-d25209af7330&algo_exp_id=b04f1c59-9b37-4e26-8776-d25209af7330-55&pdp_ext_f=%7B%22sku_id%22%3A%2212000021408298422%22%7D&pdp_pi=-1%3B24379.0%3B-1%3B-1%40salePrice%3BKRW%3Bsearch-mainSearch"
]

if __name__ == '__main__':
    options = []

    for idx, link in enumerate(links):
        driver.get(link)
        print(link)
        options.append(link)
        while True:
            try:
                # 원화가 아닐경우 원화로 변경
                if driver.find_element(By.XPATH, "//span[contains(@class,'currency')]").text != 'KRW':
                    explicitly_wait(driver, By.XPATH, "//a[contains(@id,'switcher-info')]")
                    driver.find_element(By.XPATH, "//a[contains(@id,'switcher-info')]").click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, "//a[contains(@id,'switcher-info')]").click()

                    explicitly_wait(driver, By.XPATH, "//div[contains(@data-role,'switch-currency')]")
                    driver.find_element(By.XPATH, "//div[contains(@data-role,'switch-currency')]").click()

                    explicitly_wait(driver, By.XPATH,
                                    "//div[contains(@data-role,'switch-currency')]//input[contains(@class,'search-currency')]")
                    driver.find_element(By.XPATH,
                                        "//div[contains(@data-role,'switch-currency')]//input[contains(@class,'search-currency')]").send_keys(
                        'krw')

                    explicitly_wait(driver, By.XPATH, "//a[contains(@data-currency,'KRW')]")
                    driver.find_element(By.XPATH, "//a[contains(@data-currency,'KRW')]").click()

                    explicitly_wait(driver, By.XPATH, "//button[contains(@data-role,'save')]")
                    driver.find_element(By.XPATH, "//button[contains(@data-role,'save')]").click()
                    driver.find_element(By.XPATH, "//button[contains(@data-role,'save')]").click()

                    while True:
                        if driver.find_element(By.XPATH, "//span[contains(@class,'currency')]").text == "KRW":
                            break
                        time.sleep(1)
                    break
                else:
                    break
            except:
                driver.refresh()
                continue

        # 각각의 첫번째 옵션 클릭
        for x in driver.find_elements(By.XPATH, "//div[@class='sku-property']//li[1]"):
            x.click()

        price_list = []

        prices = ""
        for x in range(len(driver.find_elements(By.XPATH, "//div[@class='sku-property']/ul"))):
            price_list.append(driver.find_element(By.XPATH, "//span[contains(@class,'price')]").text)
            for idx, value in enumerate(driver.find_elements(By.XPATH, f"//div[@class='sku-property'][{x + 1}]//li")):
                if idx == 0: continue
                value.click()
                price_list.append(driver.find_element(By.XPATH, "//span[contains(@class,'price')]").text)
                time.sleep(.5)

            driver.find_elements(By.XPATH, f"//div[@class='sku-property'][{x + 1}]//li")[0].click()
            prices +=", ".join([price.split(' ')[1].replace(',', '') for price in price_list])+ '\n'
            price_list = []
        options.append(prices[:-1])

    df = pd.DataFrame(options, )
    writer = pd.ExcelWriter(f"{datetime.datetime.now().strftime('%y%m%d_%H%M%S_result.xlsx')}", engine='xlsxwriter', )
    df.to_excel(writer,header=False, index=False)
    writer.close()

    driver.close()
    sys.exit()
