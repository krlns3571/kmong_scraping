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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tqdm import tqdm

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
    excel_file = 'input.xlsx'

    excel_dir = os.path.join(excel_file)

    df_from_excel = pd.read_excel(excel_dir,  # write your directory here
                                  sheet_name='Sheet1',
                                  )

    urls = df_from_excel['URL'].values.tolist()
    results = []
    try:
        for url in tqdm(urls, unit='url'):
            driver = driver_setting()
            if url.find('http') < 0:
                url = 'https://' + url
            try:
                driver.get(url)
            except:
                results.append('')
                driver.quit()
                continue

            if url.find('www.naeil.com') > 0:
                results.append(
                    driver.find_element(By.XPATH, "//div[contains(@class,'article')][contains(@id,'contents')]").text)

            elif url.find('segye.com') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@itemprop,'articleBody')]").text)
            elif url.find('chosun.com') > 0:
                results.append(driver.find_element(By.XPATH, "//section[contains(@class,'article-body')]").text)

            elif url.find('hani.co.kr') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@itemprop,'articleBody')]").text)

            elif url.find('hankookilbo.com') > 0:
                results.append(
                    "\n".join([x.text for x in driver.find_elements(By.XPATH, "//p[contains(@class,'editor-p')]")]))
            elif url.find('kookje.co.kr') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@class,'news_article')]").text)
            elif url.find('busan.com') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@class,'article_content')]").text)

            elif url.find('kado.net') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@class,'article-body')]").text)

            elif url.find('ytn.co.kr') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@class,'article')]/span").text)

            elif url.find('khan.co.kr') > 0:
                results.append(
                    "\n\n".join([x.text for x in driver.find_elements(By.XPATH, "//p[contains(@class,'content_text')]")]))
            elif url.find('joongang.co.kr') > 0:
                results.append("\n\n".join(
                    [x.text for x in driver.find_elements(By.XPATH, "//div[contains(@class,'article_body')]/p")]))

            elif url.find('hankyung.com') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@id,'articletxt')]").text)

            elif url.find('ytn.co.kr') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@id,'articletxt')]").text)
            elif url.find('donga.com') > 0:
                results.append(
                    driver.find_element(By.XPATH, "//div[contains(@class,'article_txt')]").text.split("\n\n\n")[0])
            elif url.find('asiae.co.kr') > 0:
                results.append("\n\n".join(
                    [x.text for x in driver.find_elements(By.XPATH, "//div[contains(@itemprop,'articleBody')]/p")]))

            elif url.find('news.sbs.co.kr') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@itemprop,'articleBody')]").text)
            elif url.find('news.kbs.co.kr') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@id,'cont_newstext')]").text)
            elif url.find('seoul.co.kr') > 0:
                results.append(driver.find_element(By.XPATH, "//*[@id='atic_txt1']").text)
            elif url.find('saedaily.com') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@class,'con_left')]").text)
            elif url.find('obsnews.co.kr') > 0:
                results.append(driver.find_element(By.XPATH, "//article[contains(@itemprop,'articleBody')]").text)
            elif url.find('munhwa.com') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@id,'view_body')]").text)
            elif url.find('mk.co.kr') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@itemprop,'articleBody')]").text)

            elif url.find('ihalla.com') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@class,'cont_gisa')]").text)
            elif url.find('fnnews.com') > 0:
                try:
                    results.append(re.compile(r'(.*.com .* 기자)').search(
                        driver.find_element(By.XPATH, "//div[contains(@id,'article_content')]").text.replace('\n',
                                                                                                             '\t')).group(
                        1).replace('\t', '\n'))
                except:
                    results.append(driver.find_element(By.XPATH, "//div[contains(@id,'article_content')]").text)
            elif url.find('etnews.com') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@itemprop,'articleBody')]").text)
            elif url.find('dt.co.kr') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@itemprop,'articleBody')]").text)
            elif url.find('ajunews.com') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@itemprop,'articleBody')]").text)
            elif url.find('news.mt.co.kr') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@id,'textBody')]").text)
            elif url.find('news.kmib.co.kr') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@itemprop,'articleBody')]").text)
            elif url.find('biz.heraldcorp.com') > 0:
                results.append(driver.find_element(By.XPATH, "//div[contains(@itemprop,'articleBody')]").text)

            else:
                try:
                    results.append(driver.find_element(By.XPATH, "//div[contains(@itemprop,'articleBody')]").text)
                except:
                    results.append('')

            driver.quit()
        print_xlsx(pd.DataFrame([urls, results]).T, 'result', ['URL', '본문'], [40, 40])
        print(f'총 {len(results)}개의 수집이 완료되었습니다. 해당 창은 종료하셔도 좋습니다.')
    except:
        print_xlsx(pd.DataFrame([urls, results]).T, 'result', ['URL', '본문'], [40, 40])
        print(f'총 {len(results)}개의 수집이 완료되었습니다. 해당 창은 종료하셔도 좋습니다.')


