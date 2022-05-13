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


def print_xlsx(list_):
    df = pd.DataFrame(list_, )
    writer = pd.ExcelWriter(f"{datetime.datetime.now().strftime('%y%m%d_%H%M%S_result.xlsx')}",
                            engine='xlsxwriter', )
    df.to_excel(writer, header=False, index=False)
    writer.close()


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

names = []
locations = []

if __name__ == '__main__':
    for x in range(1,30):
        driver.get(f"https://superbin.co.kr/new/contents/location_list.php?skey=&sval=&pg={x}")
        [names.append(x.text) for x in driver.find_elements(By.XPATH, "//strong[contains(@class,'lc_point')]")]
        [locations.append(x.text) for x in driver.find_elements(By.XPATH, "//span[contains(@class,'lc_adress')]")]
        pass

print(1)