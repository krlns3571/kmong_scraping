# coding: utf-8
import requests
import json

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
# options.add_argument("--lang=en-US")

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}


class TbS(Base):
    __tablename__ = 'tb_ss'

    idx = Column(BIGINT(20), primary_key=True)
    cat = Column(String(50), nullable=False, server_default=text("'0'"))
    url = Column(String(100), unique=True)
    result = Column(JSON)
    created_at = Column(DATETIME(fsp=3), server_default=text("CURRENT_TIMESTAMP(3)"))
    updated_at = Column(DATETIME(fsp=3), server_default=text("CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3)"))


def return_result():
    return {
        '링크': None,
        '카테고리': None,
        '강사': None,
        '제목': None,
        '할부': None,
        '가격': None,
        '찜': None,
        '커뮤니티': None,
        '클래스분량': None,
        '평균별점': None,
        '별점갯수': None,
    }


def get_result(target):
    driver = webdriver.Chrome(executable_path=CHROMEDRIVERPATH, chrome_options=options,
                              desired_capabilities=caps)
    return_dict = return_result()
    h = Handler()

    try:
        # target.url = 'https://smartstore.naver.com/whocaremall'

        driver.get(f'{target.url}')
        # print(target.url, target.idx)

        # if driver.current_url.find('brand.naver') > -1:
        #     target.url = driver.current_url
        #     driver.get(f'{target.url}')
        return_dict['링크'] = target.url

        x = driver.current_url
        # time.sleep(5)
        try:
            driver.find_element(By.XPATH, '//button[@aria-label="Close Message"]').click()
        except:
            pass

        try:
            cat_teacher = driver.find_element(By.XPATH,
                                              "//div[contains(@class,'fPCBAU')]//div[contains(@class,'sc-6d6bbb47-0 eHyubn')]/div[contains(@class,'gntHrH')]").text.split(
                '·')
            return_dict['강사'] = cat_teacher[-1].strip()
            return_dict['카테고리'] = "·".join(cat_teacher[:-1]).strip()

        except:
            try:
                cat_teacher = driver.find_element(By.XPATH,
                                                  "//p[@class='css-1j9t6oj']").text.split(
                    '·')
                return_dict['강사'] = cat_teacher[-1].strip()
                return_dict['카테고리'] = "·".join(cat_teacher[:-1]).strip()
            except:
                try:
                    cat_teacher = driver.find_element(By.XPATH,
                                              "//div[contains(@class,'cJEOdT')]//div[contains(@class,'ezJegD')]").text.split(
                        '·')
                    return_dict['강사'] = cat_teacher[-1].strip()
                    return_dict['카테고리'] = "·".join(cat_teacher[:-1]).strip()
                except:

                    pass
                pass

        try:
            return_dict['제목'] = driver.find_element(By.XPATH,
                                                    "//div[contains(@class,'fPCBAU')]//div[contains(@class,'sc-6d6bbb47-0 eHyubn')]/h2[contains(@class,'hpjlkc')]").text
        except:
            try:
                return_dict['제목'] = driver.find_element(By.XPATH,
                                                        "//h4[@class='css-20vu6v']").text
            except:
                try:
                    return_dict['제목'] = driver.find_element(By.XPATH,
                                              "//div[contains(@class,'cJEOdT')]//*[contains(@class,'hpjlkc')]").text
                except:
                    pass
                pass

        try:
            return_dict['할부'] = driver.find_element(By.XPATH,
                                                    "//div[contains(@class,'fPCBAU')]//div[contains(@class,'sc-6d6bbb47-0 eHyubn')]//div[contains(@class,'cBQXxg')]").text
        except:
            try:
                return_dict['할부'] = driver.find_element(By.XPATH,
                                                        "//div[contains(@class,'cJEOdT')]//div[contains(@class,'cBQXxg')]").text
            except:
                pass
            pass

        try:
            return_dict['가격'] = driver.find_element(By.XPATH,
                                                    "//div[contains(@class,'fPCBAU')]//div[contains(@class,'sc-6d6bbb47-0 eHyubn')]//h4[contains(@class,'bKXcYg')]").text
        except:
            try:
                return_dict['가격'] = driver.find_element(By.XPATH,
                                                        "//*[@class='css-16lfxhe']").text
            except:
                try:
                    return_dict['가격'] = driver.find_element(By.XPATH,
                                                            "//div[contains(@class,'cJEOdT')]//*[contains(@class,'bKXcYg')]").text
                except:

                    pass
                pass

        try:
            return_dict['찜'] = driver.find_element(By.XPATH,
                                                   "//div[contains(@class,'fPCBAU')]//div[contains(@class,'eHyubn')]//button[contains(@class,'jjFHla')]/span[contains(@class,'jwNHGa')]").text
        except:
            try:
                return_dict['찜'] = driver.find_element(By.XPATH,
                                                        "//button[@class='css-1rkm25z']//span[@class='css-2mddlw']").text
            except:
                try:
                    return_dict['찜'] = driver.find_element(By.XPATH,
                                              "//div[contains(@class,'cJEOdT')]//button[contains(@class,'gQyJNI')]/span[contains(@class,'jwNHGa')]").text
                except:

                    pass
                pass

        try:
            return_dict['커뮤니티'] = driver.find_element(By.XPATH,
                                                      "//div[contains(@class,'kXYKvP')][contains(text(),'커뮤니티')]/../span").text.split(
                '개')[0]
        except:
            pass

        try:
            return_dict['클래스분량'] = driver.find_element(By.XPATH, "//dd[contains(@class,'ecWtqs')]").text
        except:
            try:
                return_dict['클래스분량'] = driver.find_element(By.XPATH,
                                                        "//p[contains(text(),'분량')]/../..//p[@class='css-z9fmwo']").text
            except:
                try:
                    return_dict['클래스분량'] = driver.find_element(By.XPATH, "//dd[contains(@class,'hfRziK')]").text
                except:

                    pass
                pass
            pass

        try:
            star = driver.find_elements(By.XPATH,
                                        "//a[contains(@href,'reviews/list?klassId=')]//span[contains(@class,'sc-')]")
            try:
                return_dict['평균별점'] = star[0].text
                return_dict['별점갯수'] = star[1].text
            except:
                return_dict['평균별점'] = None
                return_dict['별점갯수'] = None
        except:
            pass

        try:
            driver.find_element(By.XPATH, "//div[contains(text(),'크리에이터')]").click()
            time.sleep(1)
            return_dict['SNS및외부링크'] = "\n".join([x.get_attribute('href') for x in
                       driver.find_elements(By.XPATH, "//div[contains(@class,'iqweXH')]/div//a")])
        except:
            try:
                driver.find_element(By.XPATH, "//a[contains(@href,'#creator')]").click()
                time.sleep(1)
                return_dict['SNS및외부링크'] = "\n".join([x.get_attribute('href') for x in
                                                     driver.find_elements(By.XPATH,
                                                                          "//div[@class='css-u4kbcl']//a")])
            except:

                pass
            pass

        # headers = {
        #     'authority': 'cdn-gql-prod2.class101.net',
        #     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        #     'apollographql-client-name': 'web-prod',
        #     'x-auid': '2c06f0ef-ad28-459c-ae31-c95dd7a29092',
        #     'accept-language': 'ko',
        #     'sec-ch-ua-mobile': '?0',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        #     'accept': '*/*',
        #     'environment': 'WEB',
        #     'x-transaction-id': 'b2697186-9ea1-4fb8-b6d4-815fe034f6da',
        #     'apollographql-operation-type': 'query',
        #     'sec-ch-ua-platform': '"Windows"',
        #     'origin': 'https://class101.net',
        #     'sec-fetch-site': 'same-site',
        #     'sec-fetch-mode': 'cors',
        #     'sec-fetch-dest': 'empty',
        #     'referer': 'https://class101.net/',
        #     'cookie': 'auid=2c06f0ef-ad28-459c-ae31-c95dd7a29092; _hackle_hid=64de051b-624c-46ef-a128-e35811a7cfee; ajs_anonymous_id=%223eb2f4b6-c59e-4879-8739-82e9b820ddd4%22; ab.storage.deviceId.2b3f474c-7aee-41a1-b6f9-c6be442dd067=%7B%22g%22%3A%22e2a7015b-4f2c-4c86-2424-031375ddaa3d%22%2C%22c%22%3A1646196232095%2C%22l%22%3A1646196232095%7D; _ga=GA1.2.2141157774.1646196232; _gid=GA1.2.1195301944.1646196232; ch-veil-id=09f6c9c3-d803-4a93-9bee-6001d5af468b; _gcl_au=1.1.324252291.1646196232; _gcl_aw=GCL.1646269009.CjwKCAiAyPyQBhB6EiwAFUuakt3bN_e5fICDFJ63uulHjPVBq8or_U0SetxNY7j38amMRTynyZXFVhoCBMIQAvD_BwE; _gac_UA-64561335-27=1.1646269010.CjwKCAiAyPyQBhB6EiwAFUuakt3bN_e5fICDFJ63uulHjPVBq8or_U0SetxNY7j38amMRTynyZXFVhoCBMIQAvD_BwE; cto_bundle=cOh8uF9YJTJGblBMN1hLJTJGWk90MVpLNnMzQW9kaHIxdFJ1QkVrbkk3JTJCcXBySCUyRiUyRnY5UnNBZGZUbkxrVFRLT3hYZll1RnV6c3dYTDBNaXlsNUdLVGtXaW5WRXJhbWF4JTJCOXhIMSUyRkslMkZucmVVTXpIWXdzcmZoU3ZBSXNBRDBxUWxob0xZM2FLWUVxQiUyQm8zJTJGNXNsNGFYVXAyeDRaM2d1dyUzRCUzRA; ch-session-4864=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiI0ODY0LTYyMWVmNjA4MTZkYjY4NWY3NzliIiwiaWF0IjoxNjQ2Mjg5MTY5LCJleHAiOjE2NDg4ODExNjl9.-_HnZXIOSn0kTB34g54UU3bSdJPW8ixsnCF-fKJZOVk; ab.storage.sessionId.2b3f474c-7aee-41a1-b6f9-c6be442dd067=%7B%22g%22%3A%2280dafb6b-e7aa-c6df-9b8c-33f9bf324d86%22%2C%22e%22%3A1646290967294%2C%22c%22%3A1646287901302%2C%22l%22%3A1646289167294%7D',
        # }
        # product_id = target.url.split('/')[-1]
        # json_data = [
        #     {
        #         'operationName': 'PostList',
        #         'variables': {
        #             'preFilter': {
        #                 'productId': f'{product_id}',
        #                 'excludeCheerMessages': True,
        #             },
        #             'offset': 0,
        #             'limit': 10,
        #         },
        #         'query': 'query PostList($preFilter: PrePostFilter!, $limit: Int, $offset: Int, $sort: [PrePostSorter!]) {\n  posts(prePostFilter: $preFilter, limit: $limit, offset: $offset, sort: $sort) {\n    ...PostSummary\n    __typename\n  }\n  postsCount(preFilter: $preFilter)\n}\n\nfragment PostSummary on Post {\n  _id\n  firestoreId\n  blindAt\n  createdAt\n  photoUrl\n  videoUUID\n  audioUUID\n  title\n  content\n  translatedContent\n  languageCode\n  userId\n  likedCount\n  type\n  important\n  missionId\n  disagreedCommentNotiUserIds\n  user {\n    _id\n    firestoreId\n    name\n    nickName\n    photoUrl\n    createdAt\n    __typename\n  }\n  files {\n    fileID\n    fileName\n    extension\n    __typename\n  }\n  __typename\n}\n',
        #     },
        # ]
        #
        # res = requests.post('https://cdn-gql-prod2.class101.net/graphql', headers=headers, json=json_data)
        #
        # offset = json.loads(res.text)[0]['data']['postsCount'] -1
        #
        # json_data = [
        #     {
        #         'operationName': 'PostList',
        #         'variables': {
        #             'preFilter': {
        #                 'productId': f'{product_id}',
        #                 'excludeCheerMessages': True,
        #             },
        #             'offset': int(f'{offset}'),
        #             'limit': 10,
        #         },
        #         'query': 'query PostList($preFilter: PrePostFilter!, $limit: Int, $offset: Int, $sort: [PrePostSorter!]) {\n  posts(prePostFilter: $preFilter, limit: $limit, offset: $offset, sort: $sort) {\n    ...PostSummary\n    __typename\n  }\n  postsCount(preFilter: $preFilter)\n}\n\nfragment PostSummary on Post {\n  _id\n  firestoreId\n  blindAt\n  createdAt\n  photoUrl\n  videoUUID\n  audioUUID\n  title\n  content\n  translatedContent\n  languageCode\n  userId\n  likedCount\n  type\n  important\n  missionId\n  disagreedCommentNotiUserIds\n  user {\n    _id\n    firestoreId\n    name\n    nickName\n    photoUrl\n    createdAt\n    __typename\n  }\n  files {\n    fileID\n    fileName\n    extension\n    __typename\n  }\n  __typename\n}\n',
        #     },
        # ]
        #
        # res = requests.post('https://cdn-gql-prod2.class101.net/graphql', headers=headers, json=json_data)
        # try:
        #     return_dict['마지막커뮤니티게시글시각'] = datetime.datetime.strptime(json.loads(res.text)[0]['data']['posts'][-1]['createdAt'],
        #                                '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S')
        # except:
        #     return_dict['마지막커뮤니티게시글시각'] = None


        for _, value in return_dict.items():
            if value is None or value == '':
                if (
                        _ != '평균별점' and
                        _ != '별점갯수' and
                        _ != 'SNS및외부링크' and
                        _ !='마지막커뮤니티게시글시각'\
                        and _ != '할부'
                        and _ != '클래스분량'
                and _ != '커뮤니티'):
                    print(target.url, _)
                    return True
        h.insert_result(target.idx, return_dict)
        driver.close()
        # time.sleep(1)
    except Exception as e:

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
        driver.close()
        print(e)
        #     con        print(e)
        #         driver.close()tinue


class Handler:
    def __init__(self):
        # dbinfo = get_dbinfo('attracker_scraping')
        # jdbc:mysql://15.164.152.174:3306/?serverTimezone=Asia/Seoul
        self.engine = create_engine(
            f'mysql+pymysql://nuvent_dev:nuvent1!@15.164.152.174:3306/account?charset=utf8mb4',
            pool_size=100, pool_recycle=9, encoding='utf-8', pool_pre_ping=True)
        SessionFactory = orm.sessionmaker(bind=self.engine, autoflush=True)
        self.session = orm.scoped_session(SessionFactory)

    def insert_url(self, url, cat):
        insert_stmt = insert(TbS).values(
            url=url,
            cat=cat
        )
        try:
            self.session.execute(insert_stmt)
        except:
            pass

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
        return self.session.query(TbS).filter(and_(TbS.result == -1)).all()


if __name__ == '__main__':
    h = Handler()

    targets = h.get_target()

    pool = Pool(processes=1)
    pool.map(get_result, targets)
