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

def get_target():
    driver = webdriver.Chrome(executable_path=CHROMEDRIVERPATH, chrome_options=options,
                              desired_capabilities=caps)

    driver.get('https://www.kci.go.kr/kciportal/po/search/poAccnSearList.kci')
    # elements = driver.find_elements(By.XPATH,"//td[contains(@data-cell-header,'제목')]/a")
    #
    # results = [x.get_attribute('href') for x in elements]
    results = []
    while True:
        names = [x.text for x in driver.find_elements(By.XPATH, '//*[@id="contents"]/div/div[2]/form/table/tbody/tr/td/a')]
        urls = [x.get_attribute('href') for x in driver.find_elements(By.XPATH, '//*[@id="contents"]/div/div[2]/form/table/tbody/tr/td[3]/ul/li[1]/a')]
        for name,url in zip(names,urls):
            try:
                driver.get(url)
                if driver.current_url.find('poInsiSearReinView')>-1:
                    homepage = driver.find_element(By.XPATH,'//*[@id="fulldivContents"]/table/tbody/tr[5]/td[1]').text

                else:
                    homepage = driver.find_element(By.XPATH, '//*[@id="fulldivContents"]/table/tbody/tr[4]/td[1]/a').text

            except Exception as e:
                homepage = ''

            results.append({'name': name,
                            'homepage': homepage
                            })
            driver.back()

        try:
            driver.find_element(By.XPATH, """//*[@id="contents"]/div/div[2]/div/a/i[contains(@class,'chevron-right')]/..""").click()
        except:
            driver.find_element(By.XPATH,
                                """//*[@id="contents"]/div/div[2]/div/a/i[contains(@class,'chevron-right')]/..""").click()
    driver.close()
    return



def get_result(target):
    driver = webdriver.Chrome(executable_path=CHROMEDRIVERPATH, chrome_options=options,
                              desired_capabilities=caps)
    return_dict = return_result()
    h = Handler()

    try:
        # target.url = 'https://smartstore.naver.com/whocaremall'

        driver.get(f'{target}')
        name = driver.find_element(By.XPATH, '//h5').text
        infos = driver.find_elements(By.XPATH, '//*[@id="Cont"]/div/ul/li')
        homepage = infos[0].text.split('홈페이지')[1]
        email = infos[1].text.split('Email')[1]
        tel = infos[4].text.split('Tel')[1]
        print(f'{name}\t{email}\t{tel}')
        with open('itfind.txt', 'a', encoding='utf8') as f:
            f.write(f'{name}\t{email}\t{tel}\n')
        driver.close()
        # time.sleep(1)
    except Exception as e:
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
    targets = get_target()
    # targets = h.get_target()
    # print(targets)

    pool = Pool(processes=1)
    pool.map(get_result, targets)
