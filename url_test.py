from pathlib import Path

from selenium.webdriver.common.by import By

import numpy as np
import time

import pandas as pd

import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

WAITTIME = 15
DOWNPATH = str(Path(os.path.dirname(os.path.abspath(__file__)), 'downloads', f'{os.getpid()}'))

if os.name == 'nt':
    CHROMEDRIVERPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver')
else:
    CHROMEDRIVERPATH = 'chromedriver'

prefs = {'download.default_directory': DOWNPATH}
options = webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-setuid-sandbox")

# options.add_argument("--disable-notifications")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('user-agent={0}'.format(user_agent))
options.add_experimental_option('prefs', prefs)
# options.add_extension('./referer_control.crx')
# options.add_extension('./tampermonkey.crx')
options.add_argument("--lang=en-US")

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}



excel_file = 'URL.xlsx'

excel_dir = os.path.join(excel_file)


df_from_excel = pd.read_excel(excel_dir, # write your directory here

                              sheet_name = 'Sheet1',

                              # header = 2,
                              #
                              # #names = ['region', 'sales_representative', 'sales_amount'],
                              #
                              # dtype = {'region': str,
                              #
                              #            'sales_representative': np.int64,
                              #
                              #            'sales_amount': float}, # dictionary type
                              #
                              # index_col = 'id',
                              #
                              # na_values = 'NaN',
                              #
                              # thousands = ',',
                              #
                              # nrows = 10,
                              #
                              # comment = '#'
                              )


driver = webdriver.Chrome(executable_path=CHROMEDRIVERPATH, chrome_options=options,
                          desired_capabilities=caps)

rule = 5584

for idx, url in enumerate(df_from_excel.URL[rule:]):
    try:
        idx += rule
        print(url)
        driver.get(f'http://{url}')
        try:
            print(idx, driver.find_element(By.XPATH, '//*[@id="pc-storeNameWidget"]/div/div/a/img').accessible_name)
        except:
            try:
                print(idx, driver.find_element(By.XPATH, '//*[@id="pc-storeNameWidget"]/div/div/a/span').text)
            except:
                try:
                    print(idx, driver.find_element(By.XPATH, '//*[@id="pc-gnbWidget"]/div/div/div[1]/div[2]/h1/a/img').accessible_name)
                except:
                    print(idx, driver.find_element(By.XPATH, '//*[@id="pc-gnbWidget"]/div/div/div[1]/div[2]/h1/a/span').text)

        # time.sleep(1)
    except Exception as e:
        alert_text = driver.find_element(By.XPATH, '//*[@id]/div/div/strong').text
        if alert_text.find('운영')>-1:
            continue
        # if driver.find_element(By.XPATH, '//*[@id]/div/div/strong').text == '판매자의 사정에 따라 운영이 중지되었습니다.':
        #     continue
        print(e)
# https://brand.naver.com/mayton


# 베스트가 없는경우도 있고
# 베스트의 종류가 다양하다 (ex. BEST, "일간,주간,월간,실시간"베스트 등등)

# alert 2 , '페이지를 찾을 수 없습니다.'
# driver.find_element(By.XPATH, '//*[@id="MAIN_CONTENT_ROOT_ID"]/div/div[2]/div[2]/h2').accessible_name
