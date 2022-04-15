import datetime
import time

import requests

headers = {
    'authority': 'www.coupang.com',
    'accept': '*/*',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}
while True:
    try:
        response = requests.get('https://www.coupang.com/vp/products/1322379253/items/2343793518/vendoritems/70376149163', headers=headers,timeout=3)
    except:
        continue

    print(response.status_code, datetime.datetime.now())
    time.sleep(.5)
