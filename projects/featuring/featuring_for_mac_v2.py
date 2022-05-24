# coding: utf-8
import datetime
import os
import time
import unicodedata

import chromedriver_autoinstaller
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tqdm import tqdm

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  # 크롬드라이버 버전 확인
path = chromedriver_autoinstaller.install(True)


def explicitly_wait(driver, by, name):
    try:
        return WebDriverWait(driver, WAITTIME).until(EC.presence_of_element_located((by, name)))
    except Exception as e:
        raise ValueError(by, name)


def print_xlsx(list_, name, header):
    df = pd.DataFrame(list_, )
    writer = pd.ExcelWriter(f"{datetime.datetime.now().strftime(f'%y%m%d_%H%M%S_{name}.xlsx')}",
                            engine='xlsxwriter', )
    df.to_excel(writer, header=header, index=False)
    for column, column_length in zip(df, [40, 15, 15, 15, 15]):
        col_idx = df.columns.get_loc(column)
        writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_length)
    writer.close()


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

WAITTIME = 30

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
s = Service(path)

driver = webdriver.Chrome(service=s, options=options,
                          desired_capabilities=caps)  # 카테고리 세팅을 위한 chromedriver

options.add_argument('--headless')
# driver2 = webdriver.Chrome(service=s, options=options,
#                            desired_capabilities=caps)  # headless로 세팅한 카테고리의 수집을 위한 chromedriver
#
# driver2.get(f"https://featuring.co/accounts/login/")
#
# driver2.find_element(By.XPATH, '//input[contains(@type,"email")]').send_keys("contact@celebram.co.kr")
# driver2.find_element(By.XPATH, '//input[contains(@type,"password")]').send_keys("rhddbqjsgh12!@")
# driver2.find_element(By.XPATH, '//button[contains(@type,"submit")]').send_keys(Keys.ENTER)
#
# driver2.get("https://featuring.co/featapp/apps/discover/")
# explicitly_wait(driver2, By.XPATH, "//div[contains(@class,'filter-accept')]")

infos = []
no_data = []

# def get_infos(url):
#     driver.get(url)
#     explicitly_wait(driver, By.XPATH, "//div[contains(@class,'filter-accept')]")
#     time.sleep(.5)


if __name__ == '__main__':
    # 사이트주소: featuring.co
    # ID: contact@celebram.co.kr
    # PW: rhddbqjsgh12!@
    try:
        driver.get(f"https://featuring.co/accounts/login/")
        page = 0
        driver.find_element(By.XPATH, '//input[contains(@type,"email")]').send_keys("contact@celebram.co.kr")
        driver.find_element(By.XPATH, '//input[contains(@type,"password")]').send_keys("rhddbqjsgh12!@")
        driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').send_keys(Keys.ENTER)

        driver.get("https://featuring.co/featapp/apps/discover/")
        explicitly_wait(driver, By.XPATH, "//div[contains(@class,'filter-accept')]")

        input('사용하고자 하시는 필터를 선택 후 ENTER를 입력해주세요')
        explicitly_wait(driver, By.XPATH, "//div[contains(@class,'filter-accept')]")
        time.sleep(1)
        try:
            driver.find_element(By.XPATH, "//div[contains(@class,'filter-accept')]").click()
        except:
            driver.find_element(By.XPATH, "//body").send_keys(Keys.HOME)
            driver.find_element(By.XPATH, "//div[contains(@class,'filter-accept')]").click()
        while True:
            page += 1
            explicitly_wait(driver, By.XPATH, "//div[contains(@class,'filter-accept')]")
            print(driver.current_url)

            user_urls = ['https://featuring.co/' + x.get_attribute('onclick').split("href=\'/")[1].split("\'")[0] for x
                         in
                         driver.find_elements(By.XPATH, "//div[contains(@onclick,'/report/?username')]")]
            if len(user_urls) == 0:
                break
            links = [x.get_attribute('onclick').split("'")[1] for x in
                     driver.find_elements(By.XPATH, "//img[@class='outlink']")]
            names = [x.text for x in driver.find_elements(By.XPATH, "//div[contains(@onclick,'/report/?username')]")]
            categories = [", ".join(x.text.split('\n')) for x in
                          driver.find_elements(By.XPATH, "//div[@class='list-contents']//div[@class='category']")]
            real_influences = [x.text.replace(',', '') for x in
                               driver.find_elements(By.XPATH, "//div[@class='list-contents']//div[@class='influence']")]
            followers = [x.text.replace(',', '') for x in
                         driver.find_elements(By.XPATH, "//div[@class='list-contents']/div/div[@class='follower']")]

            [infos.append(x) for x in list(zip(links, names, categories, real_influences, followers))]

            try:
                driver.find_element(By.XPATH, "//div[contains(@class,'pagination-next')]/span").click()
            except:
                driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
                driver.find_element(By.XPATH, "//div[contains(@class,'pagination-next')]/span").click()
            print(f'{page} page 완료')

        driver.close()
    except:
        try:
            driver.close()
        except:
            pass

    print_xlsx(infos, '결과물', ['링크', 'user_id', '카테고리', '진짜영향력', '팔로워'])
    print('작업이 모두 완료되었습니다. 해당창은 꺼주셔도 좋습니다.')
    time.sleep(10)
    exit(1)
