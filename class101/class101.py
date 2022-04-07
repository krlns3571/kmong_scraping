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

    def insert_url(self, url, cat):
        insert_stmt = insert(TbS).values(
            url=url,
            cat=cat
        )
        on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
            url=url,
            cat=cat
        )
        # time.sleep(.1)
        try:
            self.session.execute(on_duplicate_key_stmt)
        except Exception as e:
            print(e)

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


headers = {
    'authority': 'cdn-gql-prod2.class101.net',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'apollographql-client-name': 'web-prod',
    'x-auid': '2c06f0ef-ad28-459c-ae31-c95dd7a29092',
    'accept-language': 'ko',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'environment': 'WEB',
    'x-transaction-id': '5fe8d66b-338f-4052-b9ce-7ab0fed95775',
    'apollographql-operation-type': 'query',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://class101.net',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://class101.net/',
    'cookie': 'auid=2c06f0ef-ad28-459c-ae31-c95dd7a29092; _hackle_hid=64de051b-624c-46ef-a128-e35811a7cfee; ajs_anonymous_id=%223eb2f4b6-c59e-4879-8739-82e9b820ddd4%22; ab.storage.deviceId.2b3f474c-7aee-41a1-b6f9-c6be442dd067=%7B%22g%22%3A%22e2a7015b-4f2c-4c86-2424-031375ddaa3d%22%2C%22c%22%3A1646196232095%2C%22l%22%3A1646196232095%7D; _ga=GA1.2.2141157774.1646196232; _gid=GA1.2.1195301944.1646196232; ch-veil-id=09f6c9c3-d803-4a93-9bee-6001d5af468b; _gcl_au=1.1.324252291.1646196232; ab.storage.sessionId.2b3f474c-7aee-41a1-b6f9-c6be442dd067=%7B%22g%22%3A%224773d9da-a05f-7829-238e-85894304c581%22%2C%22e%22%3A1646270808326%2C%22c%22%3A1646269008335%2C%22l%22%3A1646269008335%7D; _gcl_aw=GCL.1646269009.CjwKCAiAyPyQBhB6EiwAFUuakt3bN_e5fICDFJ63uulHjPVBq8or_U0SetxNY7j38amMRTynyZXFVhoCBMIQAvD_BwE; _gac_UA-64561335-27=1.1646269010.CjwKCAiAyPyQBhB6EiwAFUuakt3bN_e5fICDFJ63uulHjPVBq8or_U0SetxNY7j38amMRTynyZXFVhoCBMIQAvD_BwE; _gat_UA-64561335-27=1; ch-session-4864=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiI0ODY0LTYyMWVmNjA4MTZkYjY4NWY3NzliIiwiaWF0IjoxNjQ2MjY5MDExLCJleHAiOjE2NDg4NjEwMTF9.XV0RgnbZ6GUtunj3scBiy1zLNRJPDATOdfWg8K4TrZE; _gali=wrapper; idToken=null; cto_bundle=CIILaF9YJTJGblBMN1hLJTJGWk90MVpLNnMzQW9kckFPODF6Q2RaMmpqR3RKQlRsWlhjZVoyU2YzNTJjV0tFb1pFY1BlM3VlbjNtcDhlMlVTOHBPZ2dZbjVtaXhNUEk1QUNmVVZFS1c4d1VVelM2UEliOVhLUmFJdSUyRmNDMnY5YWg1OFdIS1c1NGdGOEFhVHRDOWM1JTJCRGtnZkt6VkIlMkZ3JTNEJTNE',
    'if-none-match': 'W/"d702-cJOm7TqSa3jBr6W0SeuMptS2S9o"',
}

if __name__ == '__main__':


    h = Handler()
    cates = [
        '604f1c9756c3676f1ed0030e',
        '613070fa5b76158cac88344a',
        '6114891dfe1ca7f7b31b4a23',
        '613070fa5b76158cac88344b',
        '613070fa5b76158cac88344c',
        '613070fa5b76158cac88344d',
        '613070fa5b76158cac88344e',
        '613070fa5b76158cac88344f',
        '613070fa5b76158cac883450',
        '604f1c9756c3676f1ed00304',
        '604f1c9756c3676f1ed00305',
        '604f1c9756c3676f1ed00306',
        '604f1c9756c3676f1ed00307',
        '604f1c9756c3676f1ed00308',
        '604f1c9756c3676f1ed00309',
        '604f1c9756c3676f1ed00309',
        '604f1c9756c3676f1ed0030a',
        '604f1c9756c3676f1ed0030b',
        '604f1c9756c3676f1ed0030c',
        '604f1c9756c3676f1ed00312',
        '604f1c9756c3676f1ed0030d',
        '604f1c9756c3676f1ed00317',
        '604f1c9756c3676f1ed00321',
        '604f1c9756c3676f1ed00326',
        '604f1c9756c3676f1ed00319',
        '604f1c9756c3676f1ed00318',
        '604f1c9756c3676f1ed0032c',
        '604f1c9756c3676f1ed00342',
        '613070fa5b76158cac883455',
        '604f1c9756c3676f1ed0033c',
        '604f1c9756c3676f1ed00337',
        '604f1c9756c3676f1ed0033e',
        '604f1c9756c3676f1ed00341',
        '604f1c9756c3676f1ed00346',
        '604f1c9756c3676f1ed0034e',
        '604f1c9756c3676f1ed0034f',
        '613070fa5b76158cac88345a',
        '613070fa5b76158cac88345b',
        '604f1c9756c3676f1ed00351',
        '613070fa5b76158cac88345c',
        '604f1c9756c3676f1ed00356',
        '604f1c9756c3676f1ed00357',
        '613070fa5b76158cac88345d',
        '604f1c9756c3676f1ed0035a',
        '604f1c9756c3676f1ed00355',
        '604f1c9756c3676f1ed0035e',
        '604f1c9756c3676f1ed00362',
        '613070fa5b76158cac88345e',
        '613070fa5b76158cac88345f',
        '604f1c9756c3676f1ed00363',
        '613070fa5b76158cac883460',
        '604f1c9756c3676f1ed00364',
        '604f1c9756c3676f1ed00365',
        '604f1c9756c3676f1ed00366',
        '604f1c9756c3676f1ed00371',
        '604f1c9756c3676f1ed00372',
        '604f1c9756c3676f1ed00373',
        '604f1c9756c3676f1ed00374',
        '604f1c9756c3676f1ed00375',
        '604f1c9756c3676f1ed00376',
        '604f1c9756c3676f1ed00377',
        '604f1c9756c3676f1ed00378',
        '604f1c9756c3676f1ed00379',
        '604f1c9756c3676f1ed0037b',
        '604f1c9756c3676f1ed0037c',
        '604f1c9756c3676f1ed0037d',
        '604f1c9756c3676f1ed0037e',
        '604f1c9756c3676f1ed0037f',
        '604f1c9756c3676f1ed00380',
        '604f1c9756c3676f1ed00381',
        '604f1c9756c3676f1ed00382',
        '604f1c9756c3676f1ed00383',
        '604f1c9756c3676f1ed00384',
        '604f1c9756c3676f1ed00385',
        '604f1c9756c3676f1ed00386',
        '604f1c9756c3676f1ed00387',
        '604f1c9756c3676f1ed00388',
        '604f1c9756c3676f1ed00389',
        '604f1c9756c3676f1ed0038a',
        '604f1c9756c3676f1ed0038b',
        '604f1c9756c3676f1ed003b3',
        '604f1c9756c3676f1ed003b4',
        '604f1c9756c3676f1ed003b5',
        '604f1c9756c3676f1ed003b6',
        '604f1c9756c3676f1ed003b7',
        '604f1c9756c3676f1ed003bc',
        '604f1c9756c3676f1ed003bd',
        '604f1c9756c3676f1ed003ba',
        '604f1c9756c3676f1ed003b9',
        '604f1c9756c3676f1ed003b8',
        '604f1c9756c3676f1ed003be',
        '604f1c9756c3676f1ed003bf',
        '604f1c9756c3676f1ed003c0',
        '604f1c9756c3676f1ed003c1',
        '604f1c9756c3676f1ed003c2',
        '604f1c9756c3676f1ed003c3',
        '604f1c9756c3676f1ed0038e',
        '604f1c9756c3676f1ed0038f',
        '604f1c9756c3676f1ed00393',
        '604f1c9756c3676f1ed00395',
        '604f1c9756c3676f1ed00392',
        '604f1c9756c3676f1ed00394',
        '604f1c9756c3676f1ed00391',
        '604f1c9756c3676f1ed00390',
        '604f1c9756c3676f1ed00396',
        '604f1c9756c3676f1ed00397',
        '604f1c9756c3676f1ed00398',
        '604f1c9756c3676f1ed00399',
        '604f1c9756c3676f1ed0039a',
        '604f1c9756c3676f1ed0039b',
        '604f1c9756c3676f1ed0039c',
        '604f1c9756c3676f1ed0039d',
        '613070fa5b76158cac883461',
        '604f1c9756c3676f1ed003a0',
        '604f1c9756c3676f1ed003a1',
        '604f1c9756c3676f1ed003a2',
        '604f1c9756c3676f1ed003a3',
        '604f1c9756c3676f1ed003a9',
        '604f1c9756c3676f1ed003ad',
        '604f1c9756c3676f1ed003b0',
        '604f1c9756c3676f1ed003b1',
        '604f1c9756c3676f1ed003c4',
        '604f1c9756c3676f1ed003c5',
        '604f1c9756c3676f1ed003c6',
        '604f1c9756c3676f1ed003c7',
        '604f1c9756c3676f1ed003c9',
        '604f1c9756c3676f1ed003cc',
        '604f1c9756c3676f1ed003cd',
        '604f1c9756c3676f1ed003ce',
        '604f1c9756c3676f1ed003d3',
        '604f1c9756c3676f1ed003d4',
        '604f1c9756c3676f1ed003d5',
        '604f1c9756c3676f1ed003d6',
        '604f1c9756c3676f1ed003d7',
        '604f1c9756c3676f1ed003d8',
        '604f1c9756c3676f1ed003d9',
        '604f1c9756c3676f1ed003da',
        '604f1c9756c3676f1ed003db',
        '604f1c9756c3676f1ed003dc',
        '604f1c9756c3676f1ed003dd',
        '604f1c9756c3676f1ed003de',
        '604f1c9756c3676f1ed003df',
    ]
    for cat in cates:
        idx = 0
        offset = -30
        while True:
            offset += 30
            params = (
                ('operationName', 'ProductKeywordSearch'),
                ('variables',
                 '{"limit":30,"offset":' + f'{offset}' + ',"productFilter":{"isHidden":false,"categoryIds": ' + f'"{cat}"' + '},"productOrder":{"orderBy":"recommendOrder","direction":-1}}'),
                ('extensions',
                 '{"persistedQuery":{"version":1,"sha256Hash":"d2cb8bb61881fbd7b06d43a3713eb82de534da6181af8da107f33dfe5a049bad"}}'),
            )

            res = requests.get('https://cdn-gql-prod2.class101.net/graphql', headers=headers, params=params)
            while True:
                try:
                    res_json = json.loads(res.text)
                    total = res_json['data']['productsSearch']['foundTotal']
                    print(cat, total)
                except Exception as e:
                    print(e)
                if total:
                    break

            try:
                links = [['https://class101.net/products/' + x['firestoreId'], x['categoryId']] for x in
                         res_json['data']['productsSearch']['products'] if
                         x['state'] == 'sales']
            except Exception as e:
                links = []
            for x, y in links:
                idx += 1
                print(x, y, idx)
                h.insert_url(x, y)

            if offset > total:
                h.session.commit()
                break
            # time.sleep(5)

            h.session.commit()

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://cdn-gql-prod2.class101.net/graphql?operationName=ProductKeywordSearch&variables=%7B%22limit%22%3A30%2C%22offset%22%3A0%2C%22productFilter%22%3A%7B%22isHidden%22%3Afalse%2C%22categoryIds%22%3A%22604f1c9756c3676f1ed0030e%22%7D%2C%22productOrder%22%3A%7B%22orderBy%22%3A%22recommendOrder%22%2C%22direction%22%3A-1%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22d2cb8bb61881fbd7b06d43a3713eb82de534da6181af8da107f33dfe5a049bad%22%7D%7D', headers=headers)
