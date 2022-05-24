import requests
from bs4 import BeautifulSoup

# cookies = {
#     'NNB': 'VJOTCKFCLJGWE',
#     'page_uid': 'hC1jqsp0J1sssnvo+OCssssstO8-158620',
#     'nx_ssl': '2',
#     'BMR': 's=1649239514602&r=https%3A%2F%2Fm.blog.naver.com%2Foh_house%2F221292609420&r2=https%3A%2F%2Fwww.google.com%2F',
#     'sus_val': 'qdGkmTkWYhLlb4HwgPchNftN',
#     'autocomplete': 'use',
#     'AD_SHP_BID': '12',
#     'spage_uid': 'hC1jqsp0J1sssnvo%2BOCssssstO8-158620',
# }

headers = {
    'authority': 'search.shopping.naver.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'ko',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'NNB=VJOTCKFCLJGWE; page_uid=hC1jqsp0J1sssnvo+OCssssstO8-158620; nx_ssl=2; BMR=s=1649239514602&r=https%3A%2F%2Fm.blog.naver.com%2Foh_house%2F221292609420&r2=https%3A%2F%2Fwww.google.com%2F; sus_val=qdGkmTkWYhLlb4HwgPchNftN; autocomplete=use; AD_SHP_BID=12; spage_uid=hC1jqsp0J1sssnvo%2BOCssssstO8-158620',
}

params = {
    'frm': 'NVSHOVS',
    'origQuery': '캠핑의자',
    'pagingIndex': '1',
    'pagingSize': '20',
    'productSet': 'overseas',
    'query': '캠핑의자',
    'sort': 'rel',
    'timestamp': '',
    'viewType': 'list',
}
soup = BeautifulSoup(requests.get('https://search.shopping.naver.com/search/all', headers=headers, params=params).text, 'html.parser')
# response = requests.get('https://search.shopping.naver.com/search/all', headers=headers, params=params)