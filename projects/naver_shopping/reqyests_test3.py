import time

import requests
headers = {
    'authority': 'smartstore.naver.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'NNB=PAQF2L7C6DFWA; ASID=36b4314a0000017aa8b13d1800005d61; MM_NEW=1; NFS=2; NID_AUT=O/8DyXjyduSuHUsCD55s+rGQjy1+713ePNRUs+IuD7QwzkWQIJMZ2tFLTTfQ224Z; NID_JKL=agp6JkLLOUVIoFkyM/gUUluy1E+wCqSOhiGThGcoIWI=; NV_WETR_LOCATION_RGN_M="MDkxNDAxMDQ="; NDARK=Y; _gcl_au=1.1.1790671045.1643863573; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDAxMDQ="; nx_ssl=2; _gid=GA1.2.209192482.1649729152; BMR=s=1649740170462&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dzltmwnffldpt%26logNo%3D221030587695&r2=https%3A%2F%2Fwww.google.com%2F; _ga_7VKFYR6RV1=GS1.1.1649745078.77.1.1649745082.56; _ga=GA1.1.1439908789.1623999453; loungesRecentlyVisited=Umamusume; _ga_1BVHGNLQKG=GS1.1.1649754168.4.0.1649754196.0; NID_SES=AAABpnPd4NijzbK+8nl7DczJVjpXudlKyxxcG7Ewu6izEH7SL3FCdBVGcE3o+e/H9Clc0SvG7+Icpman7Cp0Ug6gK1xvIo4KEp0PuKJ19TmuofRe2KErLxVD3Yu10ORky8gGzGvcX3Ky0Fzoq8uI3TeAr2aouqOEZjrl8W9hnu6Tm/Pf4384r3U4jiILEi/02uY9iUW4ZwbsHLX+O6NNxRGW1OnBok3VISsRGmdEM40s0G8yfMSSf1CoP7hxYb80NjVolDSrj/y2Jm9/hcVgNdbe71r4OelVRm2x2YtBfNRFJY288UG+hXreXvJ5mh6rxSv6Ua7G46ScDJxA59I+zaBuBno5OkFzIDWFru4N6muh2L2VJ75+iagdHsGeox/ox4MYjDE0wNrnTmr+5Ycth8oLEkJ+RFBGUYzCOjC4GjQYEif0KB3I8CoRCA+3VJ9ZO0ak6TgltqNtjR19c/AU75rQjDfccmufL9riaKc5hS9tMeDOcKTGrsiV4Q17oTWfWICUAudo9RtDsT9KSpxZULa8KpTL5moFoQrHEtwtfjnOh5P82mtHPBEhx0SudazLsdlqBA==; _naver_usersession_=X2XACJ0+iodNMwAWFLX64fZe; page_uid=hDhAvsprvTVssK39KcNssssst4h-331946',
    'referer': 'https://smartstore.naver.com/sgkmall/products/6540348883?NaPm=ct%3Dl1wvlgbc%7Cci%3Df62b538665ee26781a190c378c4286e26434f778%7Ctr%3Dslcc%7Csn%3D3998198%7Chk%3D65d506c63a5a53bbf25af4dc859bbd0177bbf5b1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

while True:
    response = requests.get('https://smartstore.naver.com/i/v1/smart-stores/101223103/best-products', headers=headers)
    print(response.status_code)
    time.sleep(1)