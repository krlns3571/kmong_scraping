# coding: utf-8
import datetime
import json
import os
import re
import time
import warnings
from multiprocessing import Pool
from pathlib import Path
from urllib.request import urlretrieve

import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy import Column, JSON, String, text, update, and_
from sqlalchemy import create_engine, orm
from sqlalchemy.dialects.mysql import BIGINT, DATETIME
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC

from PIL import Image

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


def explicitly_wait(driver, by, name):
    try:
        return WebDriverWait(driver, WAITTIME).until(EC.presence_of_element_located((by, name)))
    except Exception as e:
        raise ValueError(by, name)


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


def get_result():
    driver = webdriver.Chrome(executable_path=CHROMEDRIVERPATH, chrome_options=options,
                              desired_capabilities=caps)
    h = Handler()

    try:
        driver.get('https://www.facebook.com/login.php?skip_api_login=1&api_key=155037361239837&kid_directed_site=0&app_id=155037361239837&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fclient_id%3D155037361239837%26redirect_uri%3Dhttps%253A%252F%252Fwww.tradingview.com%252Faccounts%252Fcomplete%252Ffacebook%252F%26state%3Dwxf9ZqdNS4Fi3vofplYwCYo0dHOgZAVO%26return_scopes%3Dtrue%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7cbfc455-af79-4181-988d-f1e5037fb2c6%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tradingview.com%2Faccounts%2Fcomplete%2Ffacebook%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dwxf9ZqdNS4Fi3vofplYwCYo0dHOgZAVO%23_%3D_&display=page&locale=ko_KR&pl_dbl=0')
        explicitly_wait(driver, By.XPATH, "//input[@id='email']")
        driver.find_element(By.XPATH,"//input[@id='email']").send_keys('louisxv@nate.com')
        driver.find_element(By.XPATH,"//input[@id='pass']").send_keys('dkdp25dn')
        driver.find_element(By.XPATH,"//button[@name='login']").click()
        while True:
            time.sleep(1)
            if driver.current_url == "https://www.tradingview.com/accounts/redirect/#_=_":
                break
        driver.get('https://kr.tradingview.com/chart/uPDgd4FP/')
        explicitly_wait(driver, By.XPATH, "//div[contains(@class,'menu')]/div/div")
        driver.find_element(By.XPATH,"//div[contains(@class,'menu')]/div/div").click()
        explicitly_wait(driver, By.XPATH, "//span[contains(text(),'로그인')]")
        driver.find_element(By.XPATH, "//span[contains(text(),'로그인')]").click()
        explicitly_wait(driver, By.XPATH, "//span[@title='Facebook']")
        driver.find_element(By.XPATH, "//span[@title='Facebook']").click()
        explicitly_wait(driver, By.XPATH, "//div[contains(@class,'chart-gui-wrapper')]")

        print(driver.current_url)
        canvas = driver.find_elements(By.XPATH,
                                      "//td[contains(@class,'chart-markup-table price-axis-container')]/div[contains(@class,'price-axis')]")[
            1]


    except Exception as e:

        # h.insert_url(product, 1)
        # alert_text = driver.find_element(By.XPATH, '//*[@id]/div/div/strong').text
        # if alert_text.find('운영') > -1:
        #     # result = -1
        #     h.insert_result(target.idx, -1)
        #     driver.close()
        #     return True
        # if driver.find_element(By.XPATH, '//*[@id]/div/div/strong').text == '판매자의 사정에 따라 운영이 중지되었습니다.':
        #     h.insert_result(target.idx, -1)
        #     driver.close()
        #     return True
        print(e)
        #     con        print(e)
        #         driver.close()tinue


class TbS(Base):
    __tablename__ = 'tb_ss'

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
            pool_size=100, pool_recycle=9, encoding='utf-8', pool_pre_ping=True)
        SessionFactory = orm.sessionmaker(bind=self.engine, autoflush=True)
        self.session = orm.scoped_session(SessionFactory)

    def insert_url(self, url, category, result=None):
        # if idx % 1000 == 0:
        #     self.session.commit()
        insert_stmt = insert(TbS).values(
            url=url,
            cat=category,
            result=result
        ).prefix_with('IGNORE')

        # on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
        #
        # )
        self.session.execute(insert_stmt)
        self.session.commit()

    def check_url(self, url):
        # if idx % 1000 == 0:
        #     self.session.commit()
        return self.session.query(TbS).filter(TbS.url == url).all()

        # on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
        #
        # )

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

    # targets = h.get_target()
    # print(targets)

    # pool = Pool(processes=1)
    # pool.map(get_result,targets)

    get_result()
