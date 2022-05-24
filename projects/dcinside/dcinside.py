import requests

# cookies = {
#     'adfit_sdk_id': '3fa2e525-bddb-4817-9ef1-0d35150ee8ea',
#     'trc_cookie_storage': 'taboola%2520global%253Auser-id%3D0752286d-258b-4bb5-afda-d443596cf575-tuct7c576ee',
#     '_cc_id': '44e0db08a42733722575248a2fec9276',
#     '_ga': 'GA1.2.648814482.1624951250',
#     '__gpi': '00000000-0000-0000-0000-000000000000',
#     'ck_img_view_cnt': '4',
#     'PHPSESSID': '928ce3ec3b668b6366e69bfef8457287',
#     'csid': '0a2af27bd7ee7cfeb672f12f3e56daca1935949e0cec8d6943abec02fcf3372a8e9fccf76b3ab7',
#     '__utmc': '118540316',
#     'alarm_popup': '1',
#     'alarm_new': '1',
#     'service_code': '21ac6d96ad152e8f15a05b7350a2475909d19bcedeba9d4face8115e9bc1fa4a7b8a78d2129bef64af5817b47070c72c97bc6790249ed583298ba2e98a4bae60e9f9f5e005940ad14825c04e36b19f42410c9d7ae28f663d1665bb0b875b50742783e06d81cb93f55c877edd5c877da628f6c1f7f738a9c29bbc5253bf1bd8dfea0d20cf87ed5b6aee51e532aed9aa0b1849153653b802fc123e5b25c859e841bd5cca32526a580743f1669bc2190226ea4df137ada8cfe06b994fe79840cc4a9ef2883859',
#     'panoramaId_expiry': '1652099218518',
#     'panoramaId': '78402e4017ca4439cc62c5eb5e744945a702d2e4b68f30f974886c715cc16527',
#     '_gid': 'GA1.2.580318012.1651728348',
#     '__utma': '118540316.648814482.1624951250.1651494413.1651728348.51',
#     '__utmz': '118540316.1651728348.51.45.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
#     '__utmt': '1',
#     'ci_c': '26bc1ca8fd3ff8d08b7859868c120869',
#     'remember_secret': 'GjVrgvqYVK',
#     'last_notice_no': '26106',
#     'last_alarm': '1651728573',
#     '_gat_gtag_UA_10723182_19': '1',
#     'ck_lately_gall': '5B%7CR9%7C1Qm%7CLj%7CzO',
#     'wcs_bt': 'f92eaecbc22aac:1651728589',
#     '__utmb': '118540316.46.10.1651728348',
# }

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'adfit_sdk_id=3fa2e525-bddb-4817-9ef1-0d35150ee8ea; trc_cookie_storage=taboola%2520global%253Auser-id%3D0752286d-258b-4bb5-afda-d443596cf575-tuct7c576ee; _cc_id=44e0db08a42733722575248a2fec9276; _ga=GA1.2.648814482.1624951250; __gpi=00000000-0000-0000-0000-000000000000; ck_img_view_cnt=4; PHPSESSID=928ce3ec3b668b6366e69bfef8457287; csid=0a2af27bd7ee7cfeb672f12f3e56daca1935949e0cec8d6943abec02fcf3372a8e9fccf76b3ab7; __utmc=118540316; alarm_popup=1; alarm_new=1; service_code=21ac6d96ad152e8f15a05b7350a2475909d19bcedeba9d4face8115e9bc1fa4a7b8a78d2129bef64af5817b47070c72c97bc6790249ed583298ba2e98a4bae60e9f9f5e005940ad14825c04e36b19f42410c9d7ae28f663d1665bb0b875b50742783e06d81cb93f55c877edd5c877da628f6c1f7f738a9c29bbc5253bf1bd8dfea0d20cf87ed5b6aee51e532aed9aa0b1849153653b802fc123e5b25c859e841bd5cca32526a580743f1669bc2190226ea4df137ada8cfe06b994fe79840cc4a9ef2883859; panoramaId_expiry=1652099218518; panoramaId=78402e4017ca4439cc62c5eb5e744945a702d2e4b68f30f974886c715cc16527; _gid=GA1.2.580318012.1651728348; __utma=118540316.648814482.1624951250.1651494413.1651728348.51; __utmz=118540316.1651728348.51.45.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; ci_c=26bc1ca8fd3ff8d08b7859868c120869; remember_secret=GjVrgvqYVK; last_notice_no=26106; last_alarm=1651728573; _gat_gtag_UA_10723182_19=1; ck_lately_gall=5B%7CR9%7C1Qm%7CLj%7CzO; wcs_bt=f92eaecbc22aac:1651728589; __utmb=118540316.46.10.1651728348',
    'Origin': 'https://gall.dcinside.com',
    'Referer': 'https://gall.dcinside.com/n',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'ci_t': '26bc1ca8fd3ff8d08b7859868c120869',
    'key': '22',
    'type': 'category',
    'cateName': '국내방송',
    'galltype': '1',
}

response = requests.post('https://gall.dcinside.com/ajax/gallery_main_ajax/search_gallmain/',  headers=headers, data=data)