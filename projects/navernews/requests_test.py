import json
import time

import pandas as pd
import requests

# pd.date_range(start="2018-09-09",end="2020-02-02")


headers = {
    'authority': 'm.news.naver.com',
    'accept': '*/*',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'NNB=PAQF2L7C6DFWA; ASID=36b4314a0000017aa8b13d1800005d61; MM_NEW=1; NFS=2; paneOrderNewsHome=today_main_news%2Csection_politics%2Csection_economy%2Csection_society%2Csection_life%2Csection_world%2Csection_it; top_paperheadline=032; NDARK=Y; _gcl_au=1.1.1790671045.1643863573; nx_ssl=2; _ga_1BVHGNLQKG=GS1.1.1649754168.4.0.1649754196.0; NV_WETR_LAST_ACCESS_RGN_M="MTQxMTA2MzA="; NV_WETR_LOCATION_RGN_M="MTQxMTA2MzA="; nid_inf=1756600562; NID_JKL=Hif7BJJ/RThY1brNMba16kfVvtUrk4TfdD0l5lu5YV0=; _ga=GA1.2.1439908789.1623999453; _ga_7VKFYR6RV1=GS1.1.1650871056.80.0.1650871061.55; page_uid=hEAdgsprvh8ssKywUvVsssssssK-165658; BMR=',
    'referer': 'https://m.news.naver.com/opinion/todayColumn',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
links = []
params = {
    'date': '20211231',
    'page': '6',
}
for date in pd.date_range(start="2021-01-01", end="2021-12-31"):
    page = 0
    time.sleep(5)
    while True:
        page += 1
        params = {
            'date': date.date().strftime('%Y%m%d'),
            'page': page,
        }
        pagelink = [x['linkUrl'] for x in json.loads(
            requests.get('https://m.news.naver.com/opinion/moreTodayColumn.json', params=params, headers=headers).text)[
            'message']['contents']['articles']]
        if len(pagelink) > 0:
            [links.append(link) for link in pagelink]
        else:
            break
        time.sleep(.5)

print(links)

from bs4 import BeautifulSoup

res = requests.get(links[0]).text
soup = BeautifulSoup(res, 'html.parser')

title = soup.select('h2.media_end_head_headline')[0].text
content = soup.select('div.newsct_article._article_body')[0].text
