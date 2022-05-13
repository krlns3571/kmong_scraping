import os
# coding: utf-8
import re
import time
import warnings

import chromedriver_autoinstaller
import pymysql
import requests
import win32com.client as w3c
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
chromedriver_autoinstaller.install(True)
warnings.simplefilter("ignore", category=pymysql.Warning)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'

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
s = Service(f'./{chrome_ver}/chromedriver.exe')

driver = webdriver.Chrome(service=s, options=options,
                          desired_capabilities=caps)


headers = {
    'Accept': '*/*',
    'Accept-Language': 'ko-KR,ko;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'ACEUCI=1; JSESSIONID=8E4UoOZHRrAyvyGA1WY4zudiIEGErurt4cng81AaQRCSd6bh7cpfCGzWndQwvRRX.nongsaro-web_servlet_engine1; SCOUTER=x68gtf766ialk; ACEUACS=1650329860371151824; ACEFCID=UID-625E09033C7CD1EF97399203',
    'Origin': 'https://www.nongsaro.go.kr',
    'Referer': 'https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfo.ps?menuId=PS03618&sYear=2013&sUnit=0&sAtpt=9900000000&sTest=&eqpCode=&totalSearchYn=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# x1 = pd.read_html(requests.post('https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfoDtl.ps', headers=headers, data=data).text)
# response = requests.post('https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfoDtl.ps', headers=headers, data=data)

driver.get(
    "https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfo.ps?menuId=PS03618&sYear=2013&sUnit=0&sAtpt=9900000000&sTest=&eqpCode=&totalSearchYn=")

years = [x.text for x in driver.find_elements(By.XPATH, "//a[contains(@id,'yr')]")]

for year in years[13:]:
    driver.get(
        f"https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfo.ps?menuId=PS03618&sYear={year}&sUnit=0&sAtpt=9900000000&sTest=&eqpCode=&totalSearchYn=")
    time.sleep(5)
    regions = [x.get_attribute('id').replace('at_', '') for x in
               driver.find_elements(By.XPATH, "//a[contains(@id,'at')]")]
    regions_files = [x.text for x in driver.find_elements(By.XPATH, "//a[contains(@id,'at')]")]
    for region, region_text_file in zip(regions,regions_files):
        driver.get(
            f"https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfo.ps?menuId=PS03618&sYear={year}&sUnit=0&sAtpt={region}&sTest=&eqpCode=&totalSearchYn=")
        time.sleep(5)
        products = [x.get_attribute('onclick').split("'")[1] for x in
                    driver.find_elements(By.XPATH, "//a[contains(@onclick,'fncDetail')]")]
        products_text_file = [x.text for x in driver.find_elements(By.XPATH, "//a[contains(@onclick,'fncDetail')]")]
        for product, filename in zip(products, products_text_file):
            data = {
                'sYear': year,
                'eqpCode': product,
                'sAtpt': region,
            }
            headers['referer'] = f'https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfo.ps?menuId=PS03618&sYear={year}&sUnit=0&sAtpt={region}&sTest=&eqpCode=&totalSearchYn='
            r = requests.post('https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfoDtl.ps', headers=headers,
                              data=data)
            xx = re.compile('서비스 이용 불가')
            if xx.search(r.text):
                with open(fr'./result/{year}_{region_text_file}_{filename}.txt', 'w', encoding='utf8') as f:
                    f.write('데이터 없음')
                continue
            with open(r'r.html', 'wb') as f:
                f.write(r.content)

            excelApp = w3c.Dispatch('Excel.Application')
            book = excelApp.Workbooks.Open(os.path.abspath('r.html'))
            book.SaveAs(f'./result/{year}_{region_text_file}_{filename}' + '.xlsx', 51)
            excelApp.Quit()
