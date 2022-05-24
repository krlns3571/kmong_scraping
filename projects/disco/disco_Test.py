import requests

cookies = {
    'sessionid': 'tj0wcwhrikjfktqcqc06gcnaledfbvg1',
    '_gcl_au': '1.1.9813017.1646981616',
    '_gid': 'GA1.2.969495744.1646981617',
    'wcs_bt': 'bf679883a3dad0:1646981767',
    '_ga_G2RYCVJW11': 'GS1.1.1646981615.1.1.1646981769.0',
    '_ga': 'GA1.2.1476122092.1646981615',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary5aouj8eZbjf8gE8w',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://www.disco.re',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.disco.re/',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
}

data = {
  '------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name': '"pnu"\r\n\r\n0\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="address"\r\n\r\n\uC804\uAD6D\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="offset"\r\n\r\n20\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="sort_type"\r\n\r\ndate\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="sort_value"\r\n\r\nincrease\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="purchase"\r\n\r\nfalse\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="limit"\r\n\r\n20\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="center_lat"\r\n\r\n37.33138581348066\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="center_lng"\r\n\r\n131.71978521474233\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="req_from"\r\n\r\n2\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="estate_type"\r\n\r\n\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="rand_type"\r\n\r\n\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="dong_type"\r\n\r\n\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="deal_type"\r\n\r\n\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w\r\nContent-Disposition: form-data; name="add_type"\r\n\r\n\r\n------WebKitFormBoundary5aouj8eZbjf8gE8w--'
}

response = requests.post('https://www.disco.re/detail/get_area_sales_data/', headers=headers, cookies=cookies, data=data)