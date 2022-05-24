import json

import requests

headers = {
    'authority': 'search.shopping.naver.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'logic': 'PART',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://search.shopping.naver.com/search/all?frm=NVSHOVS&origQuery=%EC%BA%A0%ED%95%91%EC%9D%98%EC%9E%90&pagingIndex=1&pagingSize=40&productSet=overseas&query=%EC%BA%A0%ED%95%91%EC%9D%98%EC%9E%90&sort=rel&timestamp=&viewType=list',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'NNB=PAQF2L7C6DFWA; AD_SHP_BID=9; ASID=36b4314a0000017aa8b13d1800005d61; MM_NEW=1; NFS=2; _ga_1BVHGNLQKG=GS1.1.1638347769.3.1.1638347785.0; NID_AUT=O/8DyXjyduSuHUsCD55s+rGQjy1+713ePNRUs+IuD7QwzkWQIJMZ2tFLTTfQ224Z; NID_JKL=agp6JkLLOUVIoFkyM/gUUluy1E+wCqSOhiGThGcoIWI=; NV_WETR_LOCATION_RGN_M="MDkxNDAxMDQ="; NDARK=Y; _gcl_au=1.1.1790671045.1643863573; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDAxMDQ="; nx_ssl=2; BMR=s=1649223704822&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dreinstate10%26logNo%3D130182479444&r2=https%3A%2F%2Fwww.google.com%2F; _ga=GA1.2.1439908789.1623999453; _gid=GA1.2.653525205.1649226271; _ga_7VKFYR6RV1=GS1.1.1649226270.73.0.1649226275.55; page_uid=hCGxwsprvmZssL5AUwdssssstsC-301161; autocomplete=use; spage_uid=hCGxwsprvmZssL5AUwdssssstsC-301161; NID_SES=AAABpUsZcKvsKcGs85ec3uEdILHk3wkTY68BSP8WixSLdYYCy0RNomSnaXHQ65o83VDz3AD51wlQWrliSF1xgNZhtG2HG2PusGs5A0O6P6OgdbQohWoev0nPyORv/wOWSflCLxaUOOx7DWYbuR+2VJn6BnssdDz9hr3LmyGniI1XhRKvy2zljbT6uh/QGg2wEMxY46KJFferPzuiO4oM/GqVZcn1AxOy/VNQN94fyt6GGU/tQCmiWdalyX4NB0p6PxHnW4xP6hzg3+0XSEwj3ASRqi+XUZmBW8HHOkc8sLdz9tzjXt3gIvxTVOjGMvrJW7PV7ujyvBIBQ4fAIOmWd0j/LOm2Ihfj5x5xDJcNZfIy0MOrGDix52KoYiKPjhg/NceS2q9N5izImflgsORsQwnPtz5sXTA/bI1CtQ1YF+pepsk4Q3nWrNR6y4QWJ6o/DGJoCnbhr/QPY0eJeGJiMCZIkTtQxW0i3UfQuwoDTZz6Q0Da9D3ou+4mz0ZBHIAunm457NwuRdBQx9McnskwXvSKdIPTmGPCE0dSomu4JKtLzFF+aiR6E78UL0ZpLERjmc7EzQ==; sus_val=x3FIKhZmOHPtJsMGGY29KF8Q',

}

lists = ['캠핑의자','에어랩','텀블러','핸드폰','커피','세제']

for value in lists:
    for x in range(1,21):
        params = {
            'sort': 'rel',
            'pagingIndex': f'{x}',
            'pagingSize': '40',
            'viewType': 'list',
            'productSet': 'overseas',
            'deliveryFee': '',
            'deliveryTypeValue': '',
            'frm': 'NVSHOVS',
            'query': f'{value}',
            'origQuery': f'{value}',
            'iq': '',
            'eq': '',
            'xq': '',
            'window': '',
        }
        print(x)
        res = requests.get('https://search.shopping.naver.com/api/search/all', headers=headers, params=params)
        print(json.loads(res.text)['shoppingResult']['products'][0]['imageUrl'])