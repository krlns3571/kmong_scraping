import requests

# cookies = {
#     'NNB': 'PAQF2L7C6DFWA',
#     'AD_SHP_BID': '9',
#     'ASID': '36b4314a0000017aa8b13d1800005d61',
#     'MM_NEW': '1',
#     'NFS': '2',
#     'NDARK': 'Y',
#     'autocomplete': 'use',
#     '_ga_1BVHGNLQKG': 'GS1.1.1649754168.4.0.1649754196.0',
#     'NV_WETR_LAST_ACCESS_RGN_M': '"MTQxMTA2MzA="',
#     'NV_WETR_LOCATION_RGN_M': '"MTQxMTA2MzA="',
#     'nid_inf': '1764228022',
#     'NID_AUT': 'nA5vPlUxT/q10CWr843fmjLqVCMWoC4sod9BAogmDQpPKiJCfhmkPru+hihZMMqt',
#     'NID_JKL': 'viT11G2dDPUH7lXr1sbyCvZTa6lGIya977Nqbkh/Ino=',
#     '_ga': 'GA1.2.1439908789.1623999453',
#     '_ga_7VKFYR6RV1': 'GS1.1.1651198031.81.1.1651198039.52',
#     'nx_ssl': '2',
#     'page_uid': 'hFGQXdp0JXosscfX43VssssstlV-347157',
#     'BMR': 's=1652661592780&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dlsm_origin%26logNo%3D120210926900&r2=https%3A%2F%2Fwww.google.com%2F',
#     'sus_val': 'L1IYHqJdITRh7jwh+2+YL0OW',
#     'NID_SES': 'AAABoDtcStuc8EZYrUiXlv6ByoUBeuGqUUKamy+wnWZ3bTW6fYFLUR2PtFYdyY3QYIdY9kVyKHrf3Pkpjid7BO3fulxFtEB8wD4KNfUrMEOxTsvHlzpeJJYWdg7ioz64fRLYbWmGuDgLidiR5yjzeR+BV0+BycpVu2+YIPS3EEe7JapheGJ8o/FR0VEeSX7CfigQolHTEqZgI7FRqlCFNgaZqB6aEY9HmVAqQQCub73m9RWB4Q3YlkgOpPuU3/m3lW3RkFOrAkOwGR3Fa8kVo02v0pLF/ywBZz91T4JE0+4gSCK5SXQ/2jPvIOxWd7miFnaKy2dlq9I2RfmDpYjSdE5MqwCBpnWXOq0p0ihTYc0WWnwd9vwhviG8leI9RLkqlaBI0tbKY8P9DUWZ6jwBezqu+rwGy6o6zXvSS8iRidOi1L9cAt1ZpNK04Fn9RLVDB4zWKJYPVjLlW6v8ezSPN5J7vWt/BMJA7pNxct1Ra+ElExQ9ChR9Xz7Hb2gUKZny8QAZWC0UxRickzMqhJmvbrBKUC5wrihUDEk6+PAJpgURdeCF',
#     'spage_uid': 'hFGQXdp0JXosscfX43VssssstlV-347157',
# }

headers = {
    'authority': 'search.shopping.naver.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'NNB=PAQF2L7C6DFWA; AD_SHP_BID=9; ASID=36b4314a0000017aa8b13d1800005d61; MM_NEW=1; NFS=2; NDARK=Y; autocomplete=use; _ga_1BVHGNLQKG=GS1.1.1649754168.4.0.1649754196.0; NV_WETR_LAST_ACCESS_RGN_M="MTQxMTA2MzA="; NV_WETR_LOCATION_RGN_M="MTQxMTA2MzA="; nid_inf=1764228022; NID_AUT=nA5vPlUxT/q10CWr843fmjLqVCMWoC4sod9BAogmDQpPKiJCfhmkPru+hihZMMqt; NID_JKL=viT11G2dDPUH7lXr1sbyCvZTa6lGIya977Nqbkh/Ino=; _ga=GA1.2.1439908789.1623999453; _ga_7VKFYR6RV1=GS1.1.1651198031.81.1.1651198039.52; nx_ssl=2; page_uid=hFGQXdp0JXosscfX43VssssstlV-347157; BMR=s=1652661592780&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dlsm_origin%26logNo%3D120210926900&r2=https%3A%2F%2Fwww.google.com%2F; sus_val=L1IYHqJdITRh7jwh+2+YL0OW; NID_SES=AAABoDtcStuc8EZYrUiXlv6ByoUBeuGqUUKamy+wnWZ3bTW6fYFLUR2PtFYdyY3QYIdY9kVyKHrf3Pkpjid7BO3fulxFtEB8wD4KNfUrMEOxTsvHlzpeJJYWdg7ioz64fRLYbWmGuDgLidiR5yjzeR+BV0+BycpVu2+YIPS3EEe7JapheGJ8o/FR0VEeSX7CfigQolHTEqZgI7FRqlCFNgaZqB6aEY9HmVAqQQCub73m9RWB4Q3YlkgOpPuU3/m3lW3RkFOrAkOwGR3Fa8kVo02v0pLF/ywBZz91T4JE0+4gSCK5SXQ/2jPvIOxWd7miFnaKy2dlq9I2RfmDpYjSdE5MqwCBpnWXOq0p0ihTYc0WWnwd9vwhviG8leI9RLkqlaBI0tbKY8P9DUWZ6jwBezqu+rwGy6o6zXvSS8iRidOi1L9cAt1ZpNK04Fn9RLVDB4zWKJYPVjLlW6v8ezSPN5J7vWt/BMJA7pNxct1Ra+ElExQ9ChR9Xz7Hb2gUKZny8QAZWC0UxRickzMqhJmvbrBKUC5wrihUDEk6+PAJpgURdeCF; spage_uid=hFGQXdp0JXosscfX43VssssstlV-347157',
    'referer': 'https://search.shopping.naver.com/allmall',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}

params = {
    'page': '26',
    'sortingOrder': 'prodClk',
}

response = requests.get('https://search.shopping.naver.com/allmall/api/allmall', params=params, headers=headers)