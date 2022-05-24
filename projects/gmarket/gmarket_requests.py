import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ko-KR,ko;q=0.9',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'width=1332; charset=enUS; shipnation=KR; cguid=11650002388033008562000000; pguid=21650002388033008562010000; sguid=31650002388033008562299000; PCUID=16500023879109797374506; WMONID=DNm-VEaJhAp; ssguid=3165000238803300856229900191',
    'Referer': 'http://minishop.gmarket.co.kr/dalkkong/List?Title=Best%20Item&CategoryType=General&SortType=MostPopular&DisplayType=SmallImage&Page=27&PageSize=60&IsFreeShipping=False&HasDiscount=False&HasStamp=False&HasMileage=False&IsInternationalShipping=False&IsTpl=False&MinPrice=14940&MaxPrice=1249690&Roles=System.String%5B%5D',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
}

params = {
    'Title': 'Best Item',
    'CategoryType': 'General',
    'SortType': 'MostPopular',
    'DisplayType': 'SmallImage',
    'Page': '1',
    'PageSize': '60',
    'IsFreeShipping': 'False',
    'HasDiscount': 'False',
    'HasStamp': 'False',
    'HasMileage': 'False',
    'IsInternationalShipping': 'False',
    'IsTpl': 'False',
    'MinPrice': '14940',
    'MaxPrice': '1249690',
    'Roles': 'System.String[]',
}

response = requests.get('http://minishop.gmarket.co.kr/dalkkong/List', headers=headers, params=params, verify=False)

# req = requests.get(url, headers=header, params=parms)  # 조건에 맞춰 프레임소스 가져오기
res = response.text
# print(res)

soup = BeautifulSoup(res, 'html.parser')
soup.select("#ItemList > div.prod_list > ul > li:nth-child(1) > p > a > img")