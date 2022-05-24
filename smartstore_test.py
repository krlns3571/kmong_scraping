import time

import requests
import json

headers = {
    'authority': 'search.shopping.naver.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://search.shopping.naver.com/allmall',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    # 'cookie': 'NNB=PAQF2L7C6DFWA; AD_SHP_BID=9; ASID=36b4314a0000017aa8b13d1800005d61; MM_NEW=1; NFS=2; _ga_1BVHGNLQKG=GS1.1.1638347769.3.1.1638347785.0; NID_AUT=O/8DyXjyduSuHUsCD55s+rGQjy1+713ePNRUs+IuD7QwzkWQIJMZ2tFLTTfQ224Z; NID_JKL=agp6JkLLOUVIoFkyM/gUUluy1E+wCqSOhiGThGcoIWI=; NV_WETR_LOCATION_RGN_M="MDkxNDAxMDQ="; NDARK=Y; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDAxMDQ="; nx_ssl=2; _gcl_au=1.1.1790671045.1643863573; _ga=GA1.2.1439908789.1623999453; _ga_7VKFYR6RV1=GS1.1.1644215815.60.1.1644215954.37; BMR=s=1644286394843&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dleonheart85%26logNo%3D221085795006&r2=https%3A%2F%2Fwww.google.com%2F; page_uid=hl4G1dp0YidssUYKd9wssssst/R-232441; NID_SES=AAABreQ+/qUxQehB22YFSiglCtTzD+Lt5Zthbkhi7pNS5YgfRI4O1mR0OCdZbkr8pFFmUpDUTw5PPf9zTEF517HlJpa0sj6JZEhU9pkSZT0jqaWrED+Wu5VrnB6Xox6co+HzCupG2xYddd5XYKB7dpxA7TSVohfH/vUXeye2YY4ReuuB3cFKXBVhy5N2gmmYwAuItQxkuWnRL5sjV5aSXhiUK65zBnT/HjWQgsvDxVFyEIBajRBlVFqzzmxksUbqg2K/HWVLE8A3uTXkwQpcK6NE37ZLvqzcK/0nOnQKllgxF1usRIMTy9HedgCMi49RICKpXQ2qiS3ec8qZtQBUHHtgT7Sl45cQUv2nlaVnYZd0l/I3iJEYXRVeYmRGoIMovyoGcj8a4ia7rTLI503O+JlVCNAFdsDaMipxjbCOz4+iQYSQRN4SroOtMAaEExuAUb7QHPkfoqPpX2+kAqRq8MIzMJ7P8+Yw6ZSEBkATkebtXjxtk5QGpDUnSCMu/r7Fa3mz5vMHx/cQGYoDY70Y2X8Xz5MLOo4JmKczj2ZupRMCNVZ+u0ui5adhky/nCxxDY7HlAQ==; spage_uid=hl4G1dp0YidssUYKd9wssssst%2FR-232441; sus_val=Z7DykDVHzvdio4BWTAkeTx4D; ncpa=186622|kzg95dn4|c84c49063292724113b98f0a19fede3fc91c5d28|s_2cde2c387ff92291|fcbbb1be0fb21522162d54014d13b2b478f4f7db:202062|kzg961k8|36ab0b57786a5c408730c54dbca018537e9c2ffa|s_407d1dea70a4b449|6572417eea72951572195daed31c9ce1ac9979ac:459610|kzg96eog|f714f9cf8d7e285543d2de878ffc7896ec900d25|s_4e0692ccc973c19|31d17a719556c5171278a149c666319c170b6f1e:1133061|kzg9a1uo|a6f8af9ed345bd6d8fa1e0280d6c02efdea29238|s_2873e6b6c155e|ce3f01a31f380188a1022d97f2ab5a29047b2496:24|kzg9d7a0|22ffee7a0efef2b05b99819a76133a96c2c9b515|s_419afe53a6bb|831ca8aa564971d226d1ae12ef853c2b4c788149:590782|kzg9eamo|8f44cc6cda1cdb1e72d501b12f00f56b8b727e6d|s_1d2910845386a|58a2f4d96a6fd2b9c23f474ae659d36edf860903:2247529|kzg9z0rs|c47100694e85e167532b811fead8d0fb016fbb67|s_12e6c3f2bcc95|cf094521359ad6812141ea8464e01193a5471045:290776|kzga11aw|21726275ba155099d8a3cad86bb6ba8c06dda835|s_369937874323599717|cb138bda988ade5c19e117f4a11cab2a5756dcba:4894324|kzga188w|8bac063f60dbb6ae5ad604186b20e40351925d96|s_3971ff5db2f8|c514f048b2ab004f04b50b948785ead7db4e6963:843396|kzga1mwo|6c2c95f6b1bcc80a64c92f891bf1c0a372cb7bd2|s_13b91ae913c7e|3de3541a7af6a1349d3856be808db738ba23e346',
}

for cnt in range(1,100):

    for page in range(1, 101):
        time.sleep(3)
        params = (
            ('page', f'{page}'),
            ('sortingOrder', 'prodClk'),
            ('isSmartStore', 'Y'),
            ('mallTpNm', 'SOHO'),
            ('repCatNm', 'ETC'),
        )
        response = requests.get('https://search.shopping.naver.com/allmall/api/allmall', headers=headers, params=params)
        try:
            print(f"count : {cnt}, page : {page}")
            print(json.loads(response.text)['mallList'][-1]['mallName'])
            import re

            xx = re.compile(r'PRELOADED_STATE__=(\{.*\})')

            cc = requests.get(json.loads(response.text)['mallList'][-1]['crUrl'] + '/profile').text

            vv = xx.search(cc).group(1)

        except:
            print(response)


# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://search.shopping.naver.com/allmall/api/allmall?page=19&sortingOrder=prodClk&isSmartStore=Y&mallTpNm=SOHO&repCatNm=ETC', headers=headers)
