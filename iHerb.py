import time

import requests


headers = {
    'authority': 'catalog.app.iherb.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ih-experiment=e30=; ih-preference=store=0&country=KR&language=ko-KR&currency=KRW; __cf_bm=y9PNd48pqq8uNjxuKFFO52.ZuYxUQLu3V1loEto0vm0-1649910969-0-ATaQtrO0ZHPVYk+p5k9jjIyOGj8iVuHmTGkAkL6SNXErNDjtf57tSY9y1fhOkEiCGdCf+4Gy5ir3e8M2LN/Ilm4RMs8h+ypYx9vIkq6+reM9; ih-cc-pref=eyJmdW5jdGlvbmFsIjowLCJhbmFseXRpY3MiOjB9; ForceTrafficSplitType=B; dscid=718ef5d6-8e82-4291-84ff-e1fedc81b850; notice_behavior=implied,eu; iher-pref1=storeid=0&sccode=KR&lan=ko-KR&scurcode=KRW&wp=2&lchg=1&ifv=1; FPLC=pnAMDeRvvaEoDVSMHxUN8kDvXOVP2z%2Boszf8zk9o60qNmSEk3gqFuAtERKi7LqSaX3ixX%2F%2FEVSC0yobhSMpcXTGoKHcIg4fDFnRs9UebAraZLBFUVmReYTsNpAZXKQ%3D%3D; FPID=FPID2.2.Xkk20mYFb%2BJ8goJD5TcvXUEPyz%2BxBZiiu8tthkK%2FnOw%3D.1649910969; _gid=GA1.2.1804824408.1649910965; ihr-temse=cc=KR&expires=14%20Apr%202022%2005:36:10Z; __cfruid=436da79b31d612f4dd7fe1d55122d5d9ef121be2-1649910971; _gcl_au=1.1.1446282701.1649910970; ih-exp-recs=2; _scid=7ab30700-cec8-4b3a-8e54-67e8ed7cb8ea; _wp_uid=2-3378008594d1799c305d38a0adba96aa-s1624599269.511801|windows_10|chrome-1m29nuo; _tt_enable_cookie=1; _ttp=4d820a4d-c68d-46c3-b9c9-479755b7fdb5; _sctr=1|1649862000000; ih-hp-vp=04; ih-hp-view=1; _pxvid=c499e9c1-bbac-11ec-86f3-5a4576737848; pxcts=c50b6291-bbac-11ec-b6c3-565a61784264; _pxhd=9RS5YFnO7zyxG5esCnFnqa3ZgEvC8jjC1-xHYWbCRI5yY2wFKqIUKuKmarsQadc2XkLHmbnVHf5oNk4rj8N95g; cto_bundle=PNLH9F9YbjBMVTdwdiUyQnAlMkJSa3FGbGk1ZGR2N1NRQzNWdVV0NGpTWnliRjY0SVQ1JTJCR0d6UVo5VlROemhkJTJGcm5XbFVzdlZjVmdGWkNzZXVMWCUyRnI2RksyeW44YVJKTkk1QSUyRkI1UWolMkZYVVppcmglMkYlMkJzSVVMU0RZSGs4QyUyRm9qaXZVVjVmZUZEU1lUamYzMk5tREklMkJHTUpXc1klMkJQY3clM0QlM0Q; iher-vps=77549.70317; srid=; __CG=u%3A532357331566796800%2Cs%3A1409184439%2Ct%3A1649912383744%2Cc%3A11%2Ck%3Akr.iherb.com%2F33%2F40%2F395%2Cf%3A1%2Ci%3A1; _uetsid=686067c0bbac11ecb33c89d1207d8f4f; _uetvid=34f63f604cfa11ec8ab4657fb01ebd7d; _gali=name; ihr-ds-vps=77549,70317; user-related={"HasNavigatedSite":{"timestamp":1649912618853}}; _ga_SW3NJP516F=GS1.1.1649910968.1.1.1649912619.58; _ga_06BXHBZ0RK=GS1.1.1649910968.1.1.1649912619.58; _px3=74fec69ecf0a7e58e0184437161edefc0b9343e64ddd4793887fa3b2c58c4120:K/JIv1GHQk88xsYNKDmOHpglJMOs7/czGDvhiCgoAhEwQgmQFA9b3WLYk+Lrj5CZvbLfCU5TuAe8Sjv2OV8xcg==:1000:YpXw+PQof+ufRaDGmM1ruSj5YKVtq6YmQKHPI5rK1bTjwEp31vDctqXbHCko97INbcX/xTgCYkxNQL6Bp00X97rehEl0JQ4uGRXBqiP9WzLNwxC984Nv3ZcPbqz6C11GLQhoQkEGq5u3QSf1U+jxiYJ4OejnRhB6EU2Y6UHe2CUCwCmFTYe2zKjlDYxiWNGQ6+u47gM8argNI0JyZ0STdA==; _ga=GA1.2.1007344394.1649910965',
    'origin': 'https://kr.iherb.com',
    'referer': 'https://kr.iherb.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}
while True:
    response = requests.get('https://catalog.app.iherb.com/product/77549', headers=headers,)
    print(response.status_code)
    # time.sleep(.5)