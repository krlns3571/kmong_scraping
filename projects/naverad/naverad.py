# -*- coding: utf-8 -*-
import json
import urllib.request
import urllib.request
from datetime import datetime
from time import sleep

import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta
from powernad.API import RelKwdStat

dictionary_yester = {}
dictionary_now = {}

# 네이버 강고 API 키
KWD_API_CUSTOMER_ID_ID = 726614
KWD_API_ACCESS_LICCENSE = "0100000000a32791b0b22d898089e52054e050cef3484a0b0915a34ac04f012c0c15199152"
KWD_API_SECRET_KEY = "AQAAAACjJ5Gwsi2JgInlIFTgUM7zplfppOJbvH5/bY+q2emssQ=="
KRW_API_URL = "https://api.naver.com"

keyword_list = ["파이썬", "사과", "아이폰", "맥북", "커피"]  # 키워드 입력
client_ids = ["E0d5mdQ_0Tg0htfvjSMi"]  # client_id 입력
client_secrets = ["k0RaXGzW8q"]  # client_secret 입력

toda = datetime.now()
time_month = toda - relativedelta(months=1)
time_month = time_month.strftime('%Y-%m-%d')
time_month = str(time_month)

yesterday = toda - relativedelta(days=1)
yesterday = yesterday.strftime('%Y-%m-%d')
yesterday = str(yesterday)

today = str(datetime.now().date())

# 연간 월 비율 입력
time_year = '2021-01-01'
time_year2 = '2021-12-31'


# 네이버 광고 API
def naverKwdApi(keword):
    relKwdStat = RelKwdStat.RelKwdStat(KRW_API_URL,
                                       KWD_API_ACCESS_LICCENSE,
                                       KWD_API_SECRET_KEY,
                                       KWD_API_CUSTOMER_ID_ID)

    kwdDataList = relKwdStat.get_rel_kwd_stat_list(None, hintKeywords=keword, showDetail='1')
    kwd_result = (kwdDataList[0].relKeyword,  # 키워드
                  kwdDataList[0].monthlyPcQcCnt,  # 월간 검색수 (PC)
                  kwdDataList[0].monthlyMobileQcCnt,  # 월간 검색수 (Mobile)
                  kwdDataList[0].monthlyPcQcCnt + kwdDataList[0].monthlyMobileQcCnt)  # 월간 total

    return kwd_result[3]


def get_ratio():
    for client_id, client_secret in zip(client_ids, client_secrets):
        url = "https://openapi.naver.com/v1/datalab/search"

        # 월간 일별 비율
        # body = "{\"startDate\":\"" + time_month + "\",\"endDate\":\"" + today + "\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"" + keyword + "\",\"keywords\":[\"" + keyword + "\"]}]}"

        # 연간 월별 비율
        body = "{\"startDate\":\"" + time_year + "\",\"endDate\":\"" + time_year2 + "\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"" + keyword + "\",\"keywords\":[\"" + keyword + "\"]}]}"

        requested = urllib.request.Request(url)
        requested.add_header("X-Naver-Client-Id", client_id)
        requested.add_header("X-Naver-Client-Secret", client_secret)
        requested.add_header("Content-Type", "application/json")
        cnt = 3
        while cnt:
            try:
                response = urllib.request.urlopen(requested, data=body.encode("utf-8"))
                rescode = response.getcode()

                if rescode == 200:
                    response_body = response.read()
                    output_data = response_body.decode('utf-8')
                    result = json.loads(output_data)
                    return result
                else:
                    # print('Error code:' + rescode)
                    cnt -= 1
                    sleep(1)
                    continue
            except:
                cnt -= 1
                sleep(1)
                continue
    return None


if __name__ == '__main__':

    for keyword in keyword_list:
        a = naverKwdApi(keyword.replace(' ', ''))

        result = get_ratio()

        if result['timeUnit'] == 'month':
            print(result['results'][0]['title'])
            [print(x['period'] + '\n' + str(x['ratio'])) for x in result['results'][0]['data']]
            exit(1)

        if result:
            pass
        else:
            print('사용 가능한 client_id, client_secret을 모두 다 사용하셨습니다.')
            exit(1)

        date = [a['period'] for a in result['results'][0]['data']]

        aa = pd.DataFrame({'date': date,
                           keyword: [a['ratio'] for a in result['results'][0]['data']],
                           })

        # 일일 데이터 계산

        sleep(0.5)
        total = aa[keyword].sum()

        aa[keyword] = aa[keyword].apply(lambda x: ((x / total) * float(a)))

        try:
            if type(naverKwdApi(keyword)) != str:
                searchword = keyword.replace(" ", "")
                a = naverKwdApi(searchword)

                dt_index = pd.date_range(start=time_month, end=yesterday)
                dt_list = dt_index.strftime("%Y-%m-%d").tolist()

                date = pd.DataFrame(data=dt_list, columns=['날짜'])

                spred = pd.merge(date, aa, left_on='날짜', right_on='date', how='outer')
                spred.drop(['date'], inplace=True, axis=1)
                spred.replace(np.nan, 0, inplace=True)

                a = []

                for j in range(len(spred)):
                    a.append(today)

                spred['수집날짜'] = a
                spred = spred[['날짜', '수집날짜', keyword]]

                if keyword in dictionary_yester:
                    pass

                else:
                    dictionary_yester[keyword] = []

                dictionary_now[keyword] = spred

            else:
                pass

        except (TypeError, IndexError, KeyError, ValueError):
            pass

        sleep(0.5)
        try:
            if type(naverKwdApi(keyword)) != str:
                searchword = keyword.replace(" ", "")
                a = naverKwdApi(searchword)

                if dictionary_yester[keyword] == []:
                    dictionary_yester[keyword] = dictionary_now[keyword]
                else:
                    pass
            else:
                pass


        except (TypeError, IndexError, KeyError):
            pass


        except ValueError:

            yester_df = dictionary_yester[keyword]
            today_df = dictionary_now[keyword]

            yester_df.set_index('날짜', inplace=True)

            today_df.set_index('날짜', inplace=True)

            yester_df.update(today_df)

            tmpt = today_df.iloc[-1, :]

            yester_df = yester_df.append(tmpt)

            yester_df.reset_index(inplace=True)
            today_df.reset_index(inplace=True)
            dictionary_yester[keyword] = yester_df


        except:
            pass

        # print(dictionary_now[keyword])
        for idx, x in dictionary_now[keyword].iterrows():
            print(x['날짜'])
            print(x[keyword])
        print('=' * 100)

# print(1)
