# coding: utf-8
import datetime
import json
import os
import re
import time

import chromedriver_autoinstaller
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  # 크롬드라이버 버전 확인
path = chromedriver_autoinstaller.install(True)
file_datetime = datetime.datetime.now().strftime('%y%m%d_%H%M')
os.mkdir(f'./{file_datetime}')


def print_xlsx(list_, path, header, header_size):
    df = pd.DataFrame(list_, )
    writer = pd.ExcelWriter(f"./{file_datetime}/{path}.xlsx", engine='xlsxwriter', )
    df.to_excel(writer, header=header, index=False)
    for column, column_length in zip(df, header_size):
        col_idx = df.columns.get_loc(column)
        writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_length)
    writer.close()



user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument('--incognito')
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--lang=en-US")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('user-agent={0}'.format(user_agent))

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
s = Service(path)

titles = []
summaries = []
ratings = []


def driver_setting():
    driver = webdriver.Chrome(service=s, options=options,
                              desired_capabilities=caps)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver


driver = driver_setting()

for x in range(1, 11):
    driver.get(f'https://comic.naver.com/genre/bestChallenge?&page={x}')

    [titles.append(x.text) for x in driver.find_elements(By.XPATH,
                                                         "//div[contains(@class,'weekchallenge')]//h6//a[contains(@href,'bestChallenge/list?')]")]
    [summaries.append(x.text) for x in
     driver.find_elements(By.XPATH, "//div[contains(@class,'weekchallenge')]//div[contains(@class,'summary')]")]
    [ratings.append(x.text.split('\n')[1]) for x in
     driver.find_elements(By.XPATH, "//div[contains(@class,'weekchallenge')]//div[contains(@class,'rating_type')]")]

print_xlsx(pd.DataFrame([titles, summaries, ratings]).T, 'result', ['제목', '설명', '평점'], [20, 20, 20])
