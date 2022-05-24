# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
from powernad.API import RelKwdStat
import sqlite3
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


def call(c3):


    # 네이버 강고 API 키
    KWD_API_CUSTOMER_ID_ID = "726614"
    KWD_API_ACCESS_LICCENSE = "0100000000a32791b0b22d898089e52054e050cef3484a0b0915a34ac04f012c0c15199152"
    KWD_API_SECRET_KEY = "AQAAAACjJ5Gwsi2JgInlIFTgUM7zplfppOJbvH5/bY+q2emssQ=="
    KRW_API_URL = "https://api.naver.com";


# 네이버 광고 API
def naverKwdApi(keword):


    relKwdStat = RelKwdStat.RelKwdStat(KRW_API_URL,
                                       KWD_API_ACCESS_LICCENSE,
                                       KWD_API_SECRET_KEY,
                                       KWD_API_CUSTOMER_ID_ID)

    kwdDataList = relKwdStat.get_rel_kwd_stat_list(None, hintKeywords=keword, showDetail='1')

    total = []

    for outdata in kwdDataList:
        relKeyword = outdata.relKeyword  # 연관 키워드
        monthlyPcQcCnt = outdata.monthlyPcQcCnt  # 30일간 PC 조회수
        monthlyMobileQcCnt = outdata.monthlyMobileQcCnt  # 30일간 모바일 조회수
        # monthlyAvePcClkCnt = outdata.monthlyAvePcClkCnt # 4주간 평균 PC 클릭수
        # monthlyAveMobileClkCnt = outdata.monthlyAveMobileClkCnt # 4주간 평균 모바일 클릭수
        # monthlyAvePcCtr = outdata.monthlyAvePcCtr # 4주간 평균 PC 클릭율
        # monthlyAveMobileCtr = outdata.monthlyAveMobileCtr # 4주간 평균 모바일 클릭율
        # plAvgDepth = outdata.plAvgDepth # 4주간 평균 PC 광고수
        compIdx = outdata.compIdx  # PC 광고 기반 경쟁력

        print(relKeyword)
        print(monthlyPcQcCnt)
        print(monthlyMobileQcCnt)
        print(compIdx)
        if outdata in total:
            break
        else:
            total.append(outdata)

naverKwdApi(c3)

call(sys.argv[1])
