import requests

headers = {
    'authority': 'www.coupang.com',
    'accept': '*/*',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'referer': 'https://www.coupang.com/vp/products/1583662111?itemId=2707103038&vendorItemId=71201388173&q=%ED%95%B8%EB%93%9C%ED%8F%B0%EA%B1%B0%EC%B9%98%EB%8C%80&itemsCount=36&searchId=e7aba656ee3344a79acd967b601d90aa&rank=34&isAddedCart=',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

response = requests.get('https://www.coupang.com/vp/products/1583662111/items/2707103038/vendoritems/71201388173', headers=headers, cookies=cookies)