# https://shopping.naver.com/outlet/branch/10011

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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  # 크롬드라이버 버전 확인
path = chromedriver_autoinstaller.install(True)
file_datetime = datetime.datetime.now().strftime('%y%m%d_%H%M')
try:
    os.mkdir(f'./{file_datetime}')
except:
    pass

def log_flush(driver):
    while driver.get_log('performance'):
        time.sleep(.5)


def print_xlsx(list_, path, header, header_size):
    df = pd.DataFrame(list_, )
    writer = pd.ExcelWriter(f"./{file_datetime}/{path}.xlsx", engine='xlsxwriter', )
    df.to_excel(writer, header=header, index=False)
    for column, column_length in zip(df, header_size):
        col_idx = df.columns.get_loc(column)
        writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_length)
    writer.close()
    print("\n"+os.path.abspath(f"./{file_datetime}/{path}.xlsx")+ " 저장완료")


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

WAITTIME = 30

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--lang=en-US")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('user-agent={0}'.format(user_agent))

# prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 40960}
# options.add_experimental_option("prefs", prefs)
caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
s = Service(path)


def driver_setting():
    driver = webdriver.Chrome(service=s, options=options,
                              desired_capabilities=caps)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver


if __name__ == '__main__':
    urls = input("상품을 수집할 smartstore를 입력해주세요 ,(comma)로 구분가능\n : ")
    try:

        for url in urls.split(','):
            url = url.strip()
            try:
                url = 'http://' + re.compile(r'(smartstore.naver.com\/[A-z0-9\-]+)').search(url).group(1)
            except:
                print(f'유효하지 않은 링크입니다. : {url}')
                continue
            driver = driver_setting()
            page = 0
            results = []
            while True:
                page += 1
                print(f'\r{url}\t{page} 페이지 진행중', end='')
                driver.get(url + f'/category/ALL?&page={page}')
                while True:
                    try:
                        result = json.loads(re.compile(r"window.__PRELOADED_STATE__=(\{.*\})").search(
                            driver.page_source).group(1))
                        break
                    except:
                        driver.refresh()
                        continue
                ch_no = result['smartStoreV2']['channelNo']
                urlname = result['smartStoreV2']['channel']['url']

                for product in result['category']['A']['simpleProducts']:
                    results.append(
                        [product['category']['wholeCategoryName'],
                         product['name'],
                         product['benefitsView']['discountedSalePrice'],
                         product['representativeImageUrl'],
                         f"https://smartstore.naver.com/{urlname}/products/{product['id']}"]
                    )
                if len(result['category']['A']['simpleProducts']) < 40:
                    break
            print_xlsx(results, f'{urlname}_결과물', ['카테고리', '상품명', '가격', '이미지주소', '상품링크'], [30, 30, 15, 30, 30])
            try:
                driver.quit()
                # driver.close()
            except:
                pass
        print('프로그램이 완료되었습니다. 해당 창은 꺼주셔도 좋습니다.')
    except Exception as e:
        try:
            driver.quit()
        except:
            pass
        print(e)
        with open(r'error.txt', 'w', encoding='utf8') as f:
            f.write(str(e))