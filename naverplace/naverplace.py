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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm

excel_file = 'input.xlsx'

excel_dir = os.path.join(excel_file)

df_from_excel = pd.read_excel(excel_dir, sheet_name='input')
df_from_excel = df_from_excel.replace({np.nan: None})

links = df_from_excel['예약 link']

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
chromedriver_autoinstaller.install(True)
warnings.simplefilter("ignore", category=pymysql.Warning)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'

WAITTIME = 5

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument('--incognito')
options.add_argument('--headless')
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

results = []


def explicitly_wait(driver, by, name):
    try:
        return WebDriverWait(driver, WAITTIME).until(EC.presence_of_element_located((by, name)))
    except Exception as e:
        raise ValueError(by, name)


def get_info(link, driver):
    rows = []
    if link is None:
        results.append('링크없음')
        # print('링크없음')
        time.sleep(.5)
        return

    if link.find('/items/') == -1:
        results.append('유효하지않음')
        # print('유효하지않음', link)
        time.sleep(.5)
        return
    link = link.split('?')[0] + "?area=bmp&service-target=map-pc"
    driver.get(link)

    try:
        explicitly_wait(driver, By.XPATH, "//div[contains(@id,'calendar')]")

        try:
            driver.find_element(By.XPATH, "//i[contains(@class,'fn-calendar1')]").click()
        except:
            pass

        try:
            driver.find_element(By.XPATH, "//span[contains(text(),'오늘')]").click()
            time.sleep(.5)

            try:
                driver.find_element(By.XPATH, "//span[contains(@class,'_toast_alert_text')]/span")
                results.append('예약불가')
                return
            except:
                try:
                    driver.find_element(By.XPATH, "//span[contains(@class,'alert_txt')]")
                    results.append('예약불가')
                    return
                except:
                    pass

            rows = len(driver.find_elements(By.XPATH, "//*[contains(@class,'sold_out')]"))
        except:
            pass

        if not rows:
            rows = len(driver.find_elements(By.XPATH, "//*[contains(@class,'none')]"))

        if rows == 0:
            try:
                rows = len(driver.find_elements(By.XPATH, "//*[contains(@class,'none')]"))
            except:
                pass
        results.append(rows)
    except Exception as e:
        try:
            if driver.find_element(By.XPATH, "//*[contains(@translate,'CM-ERRORNOTIFY_INFO')]"):
                results.append('이용할 수 없는 예약서비스')
                get_info(link, driver)
        except:
            pass
        results.append('유효하지않음')
    time.sleep(.5)


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=f'./{chrome_ver}/chromedriver.exe', chrome_options=options,
                              desired_capabilities=caps)

    for link in tqdm(links, unit='링크'):
        get_info(link, driver)
    close_time = f"{datetime.datetime.now().strftime('%y%m%d_%H%M%S')}"
    x1 = pd.concat([df_from_excel, pd.Series(results, name='예약 건수')], axis=1)
    writer = pd.ExcelWriter(f"{datetime.datetime.now().strftime(f'{close_time}_결과.xlsx')}", engine='xlsxwriter', )
    x1.to_excel(writer, index=False)
    for column, column_length in zip(x1, [8, 30, 30, 70, 30, 8]):
        col_idx = x1.columns.get_loc(column)
        writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_length)
    writer.close()
    driver.close()
    print('수집이 완료되었습니다. 해당 창을 꺼주셔도 좋습니다.')