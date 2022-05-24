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


def print_xlsx(list_, name):
    df = pd.DataFrame(list_, )
    writer = pd.ExcelWriter(f"{datetime.datetime.now().strftime(f'%y%m%d_%H%M%S_{name}.xlsx')}",
                            engine='xlsxwriter', )
    df.to_excel(writer, header=False, index=False)
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
                          desired_capabilities=caps) # 카테고리 세팅을 위한 chromedriver

options.add_argument('--headless')
driver2 = webdriver.Chrome(service=s, options=options,
                           desired_capabilities=caps) # headless로 세팅한 카테고리의 수집을 위한 chromedriver

driver2.get(f"https://featuring.co/accounts/login/")

driver2.find_element(By.XPATH, '//input[contains(@type,"email")]').send_keys("contact@celebram.co.kr")
driver2.find_element(By.XPATH, '//input[contains(@type,"password")]').send_keys("rhddbqjsgh12!@")
driver2.find_element(By.XPATH, '//button[contains(@type,"submit")]').send_keys(Keys.ENTER)

driver2.get("https://featuring.co/featapp/apps/discover/")
explicitly_wait(driver2, By.XPATH, "//div[contains(@class,'filter-accept')]")

infos = []
no_data = []


def get_infos(user_urls):
    for url in tqdm(user_urls, unit='링크'):
        driver2.get(url)
        try:
            explicitly_wait(driver2, By.XPATH, "//div[contains(@class,'cont-box')]//div[@id='featuring_score']")
        except:
            # if driver2.find_element(By.XPATH, "//div[contains(@class,'empty-profile-desc-no-account')]"):
            no_data.append(url)
            continue  # 존재하지않는계정 pass
            # case 1 존재하지않는계정
            # case 2 일시적으로 사용 할 수 없음('https://featuring.co/featapp/apps/report/?username=ssenseboy&channel=instagram'
        while True:
            if driver2.find_element(By.XPATH,
                                    "//div[contains(@class,'cont-box')]//div[@id='featuring_score']").text == '1점' or \
                    driver2.find_element(By.XPATH,
                                         "//div[contains(@class,'cont-box')]//div[@id='featuring_score']").text == '0점':
                # 정확한 정보가 제공될 떄 까지 대기
                time.sleep(2)
            else:
                break

        user_name = driver2.find_element(By.XPATH, "//div[@id='prof_prt']//div[contains(@class,'prof-name')]").text
        user_nick = unicodedata.normalize('NFC', driver2.find_element(By.XPATH,
                                                                      "//div[@id='prof_prt']//div[contains(@class,'real-name')]").text)  # 자모음 분리현상 해결
        user_link = \
            driver2.find_element(By.XPATH,
                                 "//div[@id='prof_prt']//div[contains(@class,'outlink-btn')]/img").get_attribute(
                'onclick').split("\'")[1]
        user_post = driver2.find_element(By.XPATH, "//div[@id='prof_prt']//div[@class='video-count']").text.split('\n')[
            1]
        user_follower = \
            driver2.find_element(By.XPATH, "//div[@id='prof_prt']//div[@class='sbcrb-count']").text.split('\n')[
                1]
        user_following = \
            driver2.find_element(By.XPATH, "//div[@id='prof_prt']//div[@class='view-count']").text.split('\n')[
                1]
        try:
            user_cate = \
                driver2.find_element(By.XPATH, "//div[@id='prof_prt']//div[@class='ctgr-cont']").text.split('\n')[1]
        except:
            user_cate = ''
        real_influence = driver2.find_element(By.XPATH, "//div[@id='influencer_score']").text.split('명')[0]

        infos.append(
            [user_link, user_name, user_nick, user_post, user_follower, user_following, user_cate, real_influence])


if __name__ == '__main__':
    # 사이트주소: featuring.co
    # ID: contact@celebram.co.kr
    # PW: rhddbqjsgh12!@

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
    driver.find_element(By.XPATH, "//div[contains(@class,'filter-accept')]").click()
    while True:
        page += 1
        explicitly_wait(driver, By.XPATH, "//div[contains(@class,'filter-accept')]")
        print(driver.current_url)

        user_urls = ['https://featuring.co/' + x.get_attribute('onclick').split("href=\'/")[1].split("\'")[0] for x in
                     driver.find_elements(By.XPATH, "//div[contains(@onclick,'/report/?username')]")]
        if len(user_urls) == 0:
            break
        get_infos(user_urls)
        driver.find_element(By.XPATH, "//div[contains(@class,'pagination-next')]/span").click()
        print(f'{page} page 완료')

    driver.close()
    driver2.close()

    print_xlsx(infos, '결과물')
    print_xlsx(no_data, '없는 계정')
