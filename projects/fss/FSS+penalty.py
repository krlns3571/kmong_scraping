import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import time
import sqlite3
import datetime

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}

url = 'https://www.fss.or.kr/fss/job/openInfo/list.do?menuNo=200476'
url2 = 'https://www.fss.or.kr/fss/job/openInfo'
url3 = 'https://www.fss.or.kr/'
penalty = []
downloads = list()

# DB에 연결
conn = sqlite3.connect('FSS.sqlite')
cur = conn.cursor()
cur.execute(
    '''CREATE TABLE IF NOT EXISTS FSS_PNT_2022_1Q (corp_nm TEXT, date TEXT, type TEXT, institution TEXT, director TEXT, employee TEXT, url TEXT)''')

page = 0

while True:

    page = page + 1

    print("Processing page", page)

    if page > 5:
        break

    parms = {'pageIndex': page,
             'sdate': '20220101',
             'edate': '20220318',
             'searchCnd':'3',
             'searchWrd':''
             }

    time.sleep(0.5)

    req = requests.get(url, headers=header, params=parms)  # 조건에 맞춰 프레임소스 가져오기
    res = req.text
    # print(res)

    soup = BeautifulSoup(res, 'html.parser')
    tags = soup.findAll('a', {'href':re.compile(r'[ ]*(examMgmtNo)[ ]*')})

    for tag in tags:
        a = url2 + tag.get('href', None)[1:]
        penalty.append(a)

k = 0

for j in penalty:
    k = k + 1
    print("processing2", k)

    time.sleep(0.3)

    req2 = requests.get(j)
    res2 = req2.text

    # print(res2)

    soup = BeautifulSoup(res2, 'html.parser')  # html용어로 파싱해서 soup으로
    tags = soup.findAll('dl')

    # tags2 = soup.findAll('a')
    rm_url = url3 + str(soup.select('.file-list__set__item a')[0]['href'])
    # for tag2 in tags2:
    #     if re.search(".+다운로드\"", str(tag2)):
    #         print(tag2.get('href', None))
    #         rm_url = url2 + str(tag2.get('href', None))

    # print(tags)

    names = [x.text for x in soup.select('#content > div > dl > dt')]
    values = [x.text.replace('\n','') for x in soup.select('#content > div > dl > dd')]

    print("-" * 30)
    [print(x+ ' : '+ y) for x,y in zip(names, values)]


    corp_nm = values[0]
    type = "제재"
    date = values[1]
    institution = values[3]
    director = values[4]
    employee = values[5]
    print(corp_nm, date, institution, director, employee)

    cur.execute('SELECT corp_nm, date,url FROM FSS_PNT_2022_1Q WHERE corp_nm =? AND date = ? AND url = ?',
                (corp_nm, date, rm_url))
    chk = cur.fetchone()
    # fetchone 조회된 결과(Record Set)로부터 데이터 1개를 반환

    if chk is None:
        cur.execute(
            '''INSERT INTO FSS_PNT_2022_1Q (corp_nm, date, type, institution, director, employee, url) VALUES (?,?,?,?,?,?,?)''',
            (corp_nm, date, type, institution, director, employee, rm_url))
        conn.commit()



    # for tag in tags:
    #     # tables = pd.read_html(str(tag))
    #     # table = tables[0]
    #     print("-" * 30)
    #     print(table)
    #
    #     table.columns = range(len(table.columns))
    #
    #     for m in list(range(0, len(table.columns))):
    #         if m < 2:
    #             continue
    #
    #         col = table[m]
    #         corp_nm = col[0]
    #         type = "제재"
    #         date = col[1]
    #         institution = col[4]
    #         director = col[5]
    #         employee = col[6]
    #         print(corp_nm, date, institution, director, employee)
    #
    #         cur.execute('SELECT corp_nm, date,url FROM FSS_PNT_2022_1Q WHERE corp_nm =? AND date = ? AND url = ?',
    #                     (corp_nm, date, rm_url))
    #         chk = cur.fetchone()
    #         # fetchone 조회된 결과(Record Set)로부터 데이터 1개를 반환
    #
    #         if chk is None:
    #             cur.execute(
    #                 '''INSERT INTO FSS_PNT_2022_1Q (corp_nm, date, type, institution, director, employee, url) VALUES (?,?,?,?,?,?,?)''',
    #                 (corp_nm, date, type, institution, director, employee, rm_url))
    #             conn.commit()

# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
#
# import pandas as pd
#
# driver = webdriver.Chrome (r'C:\Users\KCGS 분석3팀\PycharmProjects\untitled\venv\Lib\site-packages\chromedriver')
#
# url = "http://www.fss.or.kr/fss/kr/bsn/announce/openinfo_list.jsp"
# driver.get(url)
# # driver = webdriver.Chrome()
# # driver.get(주소 넣기)
#
# driver.find_element_by_id("date_start").send_keys("20190101")
# driver.implicitly_wait(1)
# driver.find_element_by_id("date_end").send_keys("20191231")
# driver.find_element_by_xpath('//*[@alt="검색"]').click()
# #
# #
#
# html = driver.page_source # page_source는 함수 아님. requests 등을 사용한 정적 수집에서 최초로 획득하는 raw html 코드와 같음
# soup = BeautifulSoup(html, 'html.parser')
#
# df = pd.DataFrame(columns=("금융기관명","제재조치일","관련부서","기관","임원","직원","첨부파일"))
#
# list = soup.select('dl>dt')
#
# for page in range(1,30):
#    for l in list:
#        company = l.select_one('dl>dt>a.first').text
#        mk = l.select_one('dl>dt>a.img')
#        date = l.select_one('dl>dt>dd>dd>span')
#        reportnm = l.select_one('dl>dt>a.second').text
#        summ = l.select_one('dl>dt>dd').text
#
#        print("="*50)
#        print("회사명:",company)
#        print("시장:",mk)
#        print("날짜:",date)
#        print("보고서명:",reportnm)
#        print("내역:",summ)
#
#    driver.find_element_by_xpath('//*[@id="listContents"]/div[3] / input[11]//*[@id="listContents"]/div[3]/input[11]').click()# 페이지 넘기기
#    #
#        df.loc[len(df)] = [company,mk,date,reportnm,summ]
#
#    df.to_excel("shareholder resolution 2019.xlsx")
#
#    # ############# 성공한 동적 방법 수집############
#    # companies = driver.find_elements_by_css_selector('dl>dt>a.first')
#    # for company in companies:
#    #     print(company.text)
#
# //*[@id="listContents"]/div[3]/input[2]
# '//*[@id="pageingWrap"]/div/div[1]/a[%s]' %page)
# //*[@id="listContents"]/div[3]/a[2]/span
#
