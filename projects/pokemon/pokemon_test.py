import requests

cookies = {
    # 'PHPSESSID': '62sh0l6nn45ioq9b2eu15cm8if',
    # '_ga': 'GA1.3.66795508.1646370375',
    # '_gid': 'GA1.3.2083248384.1646370375',
    # '_gat_gtag_UA_142581117_1': '1',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'Accept': '*/*',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryKM78zIa1A0IX04mu',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://pokemoncard.co.kr',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://pokemoncard.co.kr/cards',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
}

data = {
  '------WebKitFormBoundaryKM78zIa1A0IX04mu\r\nContent-Disposition: form-data; name': '"action"\r\n\r\nsearch_text_cards\r\n------WebKitFormBoundaryKM78zIa1A0IX04mu\r\nContent-Disposition: form-data; name="search_text"\r\n\r\n\r\n------WebKitFormBoundaryKM78zIa1A0IX04mu\r\nContent-Disposition: form-data; name="search_params"\r\n\r\nall\r\n------WebKitFormBoundaryKM78zIa1A0IX04mu\r\nContent-Disposition: form-data; name="limit"\r\n\r\n11\r\n------WebKitFormBoundaryKM78zIa1A0IX04mu--'
}

response = requests.post('https://pokemoncard.co.kr/v2/ajax2_dev2', headers=headers, cookies=cookies, data=data)