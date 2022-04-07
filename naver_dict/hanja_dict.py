import datetime
import json
import re

import requests

headers = {
    'authority': 'hanja.dict.naver.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'accept': 'text/html, */*; q=0.01',
    'alldict-locale': 'ko',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://hanja.dict.naver.com/',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
}

params = {
    'query': '편안할 안',  # 검색어 수정 부분
    'm': 'pc',
    'range': 'letter',
    'page': '1',
    'hid': str(datetime.datetime.now().timestamp()).split('.')[0]
}

response = requests.get('https://hanja.dict.naver.com/api3/ccko/search', headers=headers, params=params)

results = json.loads(response.text)['searchResultMap']['searchResultListMap']['LETTER']['items'][:3]

for result in results:
    expEntry = result['expEntry']  # 한자
    expKoreanPron = result['expKoreanPron']  # 음, 한자
    exphanjaStroke = result['exphanjaStroke']  # 총 획수
    exphanjaRadical = result['exphanjaRadical']  # 부수 (한자)
    expHanjaRadicalKoreanName = result['expHanjaRadicalKoreanName']  # 부수(한글)
    means = " ".join([f"{value['order']}. {value['value']}" for value in result['meansCollector'][0]['means']])  # 뜻
    etcExplain = result['etcExplain'] if result['etcExplain'] else ''  # 설명

    # 결과값의 <strong>태그 제거
    expEntry, expKoreanPron, exphanjaStroke, exphanjaRadical, expHanjaRadicalKoreanName, means, etcExplain = \
        [re.sub("<[/]{0,}strong>", '', value) for value in
         [expEntry, expKoreanPron, exphanjaStroke, exphanjaRadical, expHanjaRadicalKoreanName, means, etcExplain]]

    print(expEntry, expKoreanPron)
    print(exphanjaRadical, expHanjaRadicalKoreanName, exphanjaStroke)
    print(means)
    print(etcExplain)
    print('=' * 100)
