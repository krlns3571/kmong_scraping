# coding: utf-8
import datetime
import json
import os
import re
import time
import warnings
from multiprocessing import Pool
from pathlib import Path

import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sqlalchemy import Column, JSON, String, text, update, and_
from sqlalchemy import create_engine, orm
from sqlalchemy.dialects.mysql import BIGINT, DATETIME
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd


pymysql.install_as_MySQLdb()

warnings.simplefilter("ignore", category=pymysql.Warning)

Base = declarative_base()
metadata = Base.metadata

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

WAITTIME = 15
DOWNPATH = str(Path(os.path.dirname(os.path.abspath(__file__)), 'downloads', f'{os.getpid()}'))
if os.name == 'nt':
    CHROMEDRIVERPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver')
else:
    CHROMEDRIVERPATH = 'chromedriver'

prefs = {'download.default_directory': DOWNPATH}
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument('--incognito')
# options.add_argument('--headless')
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

df_from_excel = pd.read_excel(excel_dir,  # write your directory here

                              sheet_name='Sheet1',

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

def log_filter(log_, filter_url):
    return (
        # is an actual response
            log_["method"] == "Network.responseReceived"
            # and json
            and "json" in log_["params"]["response"]["mimeType"]
            and log_["params"]["response"]["url"].find(filter_url) > 1
    )


def return_result():
    return {
        '스마트스토어 링크': None,
        '쇼핑몰명': None,
        '쇼핑몰 소개': None,
        '스토어 등급': None,
        '서비스만족': None,
        '스토어찜': None,
        '상호명': None,
        '사업자등록번호': None,
        '대표자': None,
        '사업장 소재지': None,
        '고객센터': None,
        '통신판매업번호': None,
        'e-mail': None,
        '카테고리': None,
        '방문자(투데이)': None,
        '방문자(통합)': None,
        '베스트': None,
        '카테고리별 상품수': None,
        '수집시간': None,
    }


def get_result(target):
    driver = webdriver.Chrome(executable_path=CHROMEDRIVERPATH, chrome_options=options,
                              desired_capabilities=caps)
    return_dict = return_result()
    h = Handler()

    try:
        # target.url = 'https://smartstore.naver.com/whocaremall'

        driver.get(f'{target.url}')

        if driver.current_url.find('brand.naver') > -1:
            target.url = driver.current_url
            driver.get(f'{target.url}')
        return_dict['스마트스토어 링크'] = target.url
        try:
            return_dict['쇼핑몰명'] = driver.find_element(By.XPATH,
                                                      '//*[@id="pc-storeNameWidget"]/div/div/a/img').accessible_name
        except:
            try:
                return_dict['쇼핑몰명'] = driver.find_element(By.XPATH, '//*[@id="pc-storeNameWidget"]/div/div/a/span').text
            except:
                try:
                    return_dict['쇼핑몰명'] = driver.find_element(By.XPATH,
                                                              '//*[@id="pc-gnbWidget"]/div/div/div[1]/div[2]/h1/a/img').accessible_name
                except:
                    return_dict['쇼핑몰명'] = driver.find_element(By.XPATH,
                                                              '//*[@id="pc-gnbWidget"]/div/div/div[1]/div[2]/h1/a/span').text
        try:
            return_dict['스토어찜'] = driver.find_element(By.XPATH, "//span[contains(@class,'number')]").text.replace(',',
                                                                                                                  '')
        except:
            return_dict['스토어찜'] = None

        try:
            grade = driver.find_elements(By.XPATH, "//span[contains(@class,'_3CfLtIh1fI')]")
            return_dict['스토어 등급'] = grade[0].text
            return_dict['서비스만족'] = grade[1].text
        except:
            if return_dict['스토어 등급']:
                return_dict['서비스만족'] = return_dict['스토어 등급']
                return_dict['스토어 등급'] = None

        try:
            categories = driver.find_elements(By.XPATH, "//ul[contains(@class,'_3AV7RVieRB')]/li/a")
            cat_links = [value.get_attribute('href') for value in categories]
            return_dict['카테고리'] = ["".join(value.text.split('\n')[0]) for value in categories if
                                   value.text.find('전체상품')]
            return_dict['카테고리'] = "\n".join(return_dict['카테고리'])


        except Exception as e:
            pass

        if return_dict['카테고리'] == '':
            categories = driver.find_elements(By.XPATH, "//ul[contains(@class,'category')]/li/a")
            cat_links = [value.get_attribute('href') for value in categories]
            return_dict['카테고리'] = ["".join(value.text.split('\n')[0]) for value in categories if
                                   value.text.find('전체상품')]
            return_dict['카테고리'] = "\n".join(return_dict['카테고리'])

        cnt = 3
        while cnt:
            try:
                browser_log = driver.get_log('performance')
                logs = [json.loads(lr["message"])["message"] for lr in browser_log]
                logs = list(filter(lambda x: log_filter(x, '/v1/visit'), logs))
                for log in logs:
                    request_id = log["params"]["requestId"]
                    visit = json.loads(driver.execute_cdp_cmd(
                        "Network.getResponseBody", {"requestId": request_id})['body'])
                return_dict['방문자(투데이)'] = visit['today']
                return_dict['방문자(통합)'] = visit['total']
                break
            except:
                driver.refresh()
                time.sleep(.5)
                cnt -= 1

        try:
            bests = driver.find_elements(By.XPATH,
                                         "//div[@id='pc-bestProductWidget']//a//strong[contains(@class,'_2lLEGeuRvN')]")
            return_dict['베스트'] = "\n".join([value.text for value in bests])
        except:
            pass

        driver.get(target.url + '/profile')

        try:
            return_dict['쇼핑몰 소개'] = driver.find_element(By.XPATH, "//*[contains(@class,'_2NXSJqvT18')]").text
        except:
            pass
        try:
            info = driver.find_elements(By.XPATH,
                                        "//*[contains(@class,'_2E256BP8nc')]")  # info = driver.find_elements(By.XPATH, "//*[contains(@class,'_2E256BP8nc')]")

            for element in info:
                try:
                    return_dict[element.text] = element.find_elements(By.XPATH,
                                                                      "following-sibling::*")[0].text.split('인증')[0]
                except Exception as e:
                    pass

        except:
            pass

        cat = []
        for link in cat_links:
            try:
                driver.get(link)
                cat_name = driver.find_element(By.XPATH, "//strong[contains(@class,'x0Bjqs3xao')]").text
                cat_count = re.sub(r'[^0-9]', '',
                                   driver.find_element(By.XPATH, '//span[contains(@class,"_3-WhDl_6j2")]').text)
                cat.append(f"{cat_name} : {cat_count}")
                time.sleep(.5)
            except:
                pass
        return_dict['카테고리별 상품수'] = "\n".join(cat)
        driver.close()
        return_dict['수집시간'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for _, value in return_dict.items():
            if value is None or value == '':
                if _ != '베스트' and _ != '카테고리' and _ != '스토어 등급' and _ != '서비스만족' and _ != '쇼핑몰 소개' \
                        and _ != '사업자등록번호' \
                        and _ != '통신판매업번호' \
                        and _ != 'e-mail' \
                        and _ != '카테고리별 상품수' \
                        and _ != '방문자(투데이)' \
                        and _ != '방문자(통합)' \
                        and _ != '고객센터' \
                        :
                    print(target.url, _)
                    return True
        h.insert_result(target.idx, return_dict)
        h.engine.dispose()
        # time.sleep(1)
    except Exception as e:
        alert_text = driver.find_element(By.XPATH, '//*[@id]/div/div/strong').text
        if alert_text.find('운영') > -1 or alert_text.find('접속이 불가합니다.') > -1or alert_text.find('일시적으로 ') > -1:
            # result = -1
            h.insert_result(target.idx, -1)
            driver.close()
            return True
        if driver.find_element(By.XPATH, '//*[@id]/div/div/strong').text == '판매자의 사정에 따라 운영이 중지되었습니다.':
            h.insert_result(target.idx, -1)
            driver.close()
            return True
        if driver.current_url=='https://shopping.naver.com/outlink':
            h.insert_result(target.idx, -1)
            driver.close()
            return True

        print(e)
        return True
        #     con        print(e)
        #         driver.close()tinue


class TbS(Base):
    __tablename__ = 'tb_sss'

    idx = Column(BIGINT(20), primary_key=True)
    cat = Column(String(50), nullable=False, server_default=text("'0'"))
    url = Column(String(100), unique=True)
    result = Column(JSON)
    created_at = Column(DATETIME(fsp=3), server_default=text("CURRENT_TIMESTAMP(3)"))
    updated_at = Column(DATETIME(fsp=3), server_default=text("CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3)"))


class Handler:
    def __init__(self):
        # dbinfo = get_dbinfo('attracker_scraping')
        # jdbc:mysql://15.164.152.174:3306/?serverTimezone=Asia/Seoul
        self.engine = create_engine(
            f'mysql+pymysql://nuvent_dev:nuvent1!@15.164.152.174:3306/account?charset=utf8mb4',
            pool_size=1000, pool_recycle=9, encoding='utf-8', pool_pre_ping=True)
        SessionFactory = orm.sessionmaker(bind=self.engine, autoflush=True)
        self.session = orm.scoped_session(SessionFactory)

    def insert_url(self, url, category, idx):
        if idx % 1000 == 0:
            self.session.commit()
        insert_stmt = insert(TbS).values(
            url='http://' + url,
            cat=category
        ).prefix_with('IGNORE')

        # on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
        #
        # )
        self.session.execute(insert_stmt)

    def insert_result(self, idx, result):
        stmt = update(TbS).where(and_(TbS.idx == idx)).values(result=result)
        self.session.execute(stmt)
        self.session.commit()

        # insert_stmt = insert(TbS).values(
        #     result=json.dumps(dict(result), ensure_ascii=False).replace('\\', '\\\\'),
        # ).filter(TbS.idx == idx)

        # on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
        #
        # )
        # self.session.execute(insert_stmt)
        # self.session.commit()

    def get_target(self):
        return self.session.query(TbS).filter(TbS.result == None).all()

    def get_pd(self):
        return self.session.query(TbS).filter(and_(TbS.result != None, TbS.result != -1)).all()

    def get_pd2(self):
        return self.session.query(TbS).filter(and_(TbS.result != -1)).all()

# 27565
# df_from_excel
# h = Handler()
# [h.insert_url(url, None, idx) for idx, url in enumerate(df_from_excel.URL)]
# h.session.commit()
# print(h)


if __name__ == '__main__':
    h = Handler()

    targets = h.get_target()
    # print(targets)

    pool = Pool(processes=1)
    pool.map(get_result, targets)
