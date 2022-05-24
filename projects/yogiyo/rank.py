import datetime
import time

import requests

headers = {
    'authority': 'www.yogiyo.co.kr',
    'accept': 'application/json',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'optimizelyEndUserId=oeu1624942839314r0.14955282078174448; _gcl_au=1.1.1625938704.1643270135; _ga_6HEHRFBP32=GS1.1.1649410164.46.1.1649410180.0; _gid=GA1.3.1157789152.1650333809; sessionid=9b40a2d938b5209721fd05870e620d7e; _gat_UA-42635603-4=1; _gat=1; _ga=GA1.3.1600766509.1624351175; wcs_bt=s_51119d387dfa:1650342044; RestaurantListCookieTrigger=true; _ga_6KMY7BWK8X=GS1.1.1650342040.11.1.1650342057.43',
    'referer': 'https://www.yogiyo.co.kr/mobile/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'x-apikey': 'iphoneap',
    'x-apisecret': 'fe5183cc3dea12bd0ce299cf110a75a2',
}

params = {
    'items': '60',
    'lat': '37.5073809376406',
    'lng': '127.056821236713',
    'order': 'rank',
    'page': '4',
    'search': '',
}



while True:
    response = requests.get('https://www.yogiyo.co.kr/api/v1/restaurants-geo/', headers=headers, params=params)
    print(response.status_code, datetime.datetime.now())
    time.sleep(.5)