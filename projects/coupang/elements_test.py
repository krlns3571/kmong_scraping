# coding: utf-8
import json
import sys
import time
import warnings

import chromedriver_autoinstaller
import pandas as pd
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
chromedriver_autoinstaller.install(True)
warnings.simplefilter("ignore", category=pymysql.Warning)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'

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
s = Service(f'./{chrome_ver}/chromedriver.exe')

driver = webdriver.Chrome(service=s, options=options,
                          desired_capabilities=caps)

page = 1
keyword = input('사용하실 키워드를 입력해주세요 : ')
first_time = True
flag = True

product_result = []
while flag:

    driver.get(
        f"https://www.coupang.com/np/search?rocketAll=false&q={keyword}&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page={page}&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&component=&rating=0&sorter=scoreDesc&listSize=36")
    if first_time:
        driver.refresh()
        first_time = False
        try:
            lastpage = int(driver.find_element(By.XPATH, "//a[contains(@class,'btn-last')]").text)
        except:
            try:
                lastpage = int(driver.find_elements(By.XPATH, "//span[contains(@class,'btn-page')]/a")[-1].text)
            except:
                lastpage = 1

    list_all = driver.find_elements(By.XPATH, "//a[contains(@class,'search-product-link')]")
    list_rocket = driver.find_elements(By.XPATH,
                                       "//a[contains(@class,'search-product-link')]//span[contains(@class,'badge rocket')]//ancestor::a")
    list_all_name = driver.find_elements(By.XPATH,
                                         "//a[contains(@class,'search-product-link')]//div[contains(@class,'descriptions')]/div[contains(@class,'name')]")
    list_rocket_name = driver.find_elements(By.XPATH,
                                            "//a[contains(@class,'search-product-link')]//span[contains(@class,'badge rocket')]//ancestor::div[contains(@class,'descriptions')]/div[contains(@class,'name')]")
    if lastpage == page:
        flag = False
    page += 1
    not_rocket = [x for x in list_all if x not in list_rocket]
    not_rocket_name = [x for x in list_all_name if x not in list_rocket_name]

    product_list = [x.get_attribute('data-product-id') for x in not_rocket]
    item_list = [x.get_attribute('data-item-id') for x in not_rocket]
    vender_item_list = [x.get_attribute('data-vendor-item-id') for x in not_rocket]
    name_list = [x.text for x in not_rocket_name]
    driver.execute_script('window.open("");')
    driver.switch_to.window(driver.window_handles[1])
    for product, item, vender_item, name in zip(product_list, item_list, vender_item_list, name_list):
        try:
            if name == '':
                driver.get(f"https://www.coupang.com/vp/products/{product}?itemId={item}&vendorItemId={vender_item}")
                name = driver.find_element(By.XPATH, '//h2[contains(@class,"prod-buy-header__title")]').text
            driver.get(f'https://www.coupang.com/vp/products/{product}/items/{item}/vendoritems/{vender_item}')
            result = json.loads(driver.find_element(By.TAG_NAME, 'body').text)
        except:
            continue
        product_result.append([name,
                               f"https://www.coupang.com/vp/products/{product}?itemId={item}&vendorItemId={vender_item}",
                               result['returnPolicyVo']['sellerDetailInfo']['sellerWithRepPersonName'],
                               result['returnPolicyVo']['sellerDetailInfo']['repAddress'],
                               result['returnPolicyVo']['sellerDetailInfo']['repEmail'],
                               result['returnPolicyVo']['sellerDetailInfo']['repPhoneNum'],
                               result['returnPolicyVo']['sellerDetailInfo']['ecommReportNum'],
                               result['returnPolicyVo']['sellerDetailInfo']['bizNum']
                               ])
        sys.stdout.write('\r' + '현재페이지 : ' + str(page - 1) + ', ' + str(len(product_result)) + '개째 수집중..')

        time.sleep(.5)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

df = pd.DataFrame(product_result, columns=("상품명", "상품 url", "상호/대표자", "사업장 소재지", "email", "연락처", "통신판매업 신고번호", "사업자번호"))
writer = pd.ExcelWriter(f'{keyword}_결과물.xlsx', engine='xlsxwriter')
df.to_excel(writer, index=False)
for column, column_length in zip(df, [50, 50, 20, 20, 20, 20, 20, 20]):
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_length)
writer.close()
print('\n수집이 완료되었습니다. 해당 창은 꺼주셔도 좋습니다.')
sys.exit()
