import requests

headers = {
    'authority': 'api-cypress-v2.scope.klaytn.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'origin': 'https://scope.klaytn.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://scope.klaytn.com/',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'if-none-match': 'W/"b2b8-CniXGQrRJ308/Jxdu5KtE3RxZaE"',
}

params = {
    'page': '1',
    'version': 'v3',
}

response = requests.get('https://api-cypress-v2.scope.klaytn.com/v2/accounts/0xa9c34f7564b2b8390fea1f3e003a7873f67b2ce5/ftTransfers', headers=headers, params=params)