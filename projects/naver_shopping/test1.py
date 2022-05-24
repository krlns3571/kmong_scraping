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
#     'page_uid': 'hFvltlp0JXVsskRIy+8ssssssM4-457497',
#     'NA_CO': 'ct%3Dl2q6bfs5%7Cci%3Dshoppingwindow%7Ctr%3Dswl%7Chk%3D42906f675ec1ab37cb5c294304adba2367fa99ba%7Ctrx%3D',
#     'spage_uid': 'hFvltlp0JXVsskRIy%2B8ssssssM4-457497',
#     'ncpa': '95694|l2ontn2g|5a753e745efad48f05e5a02eb87c3b6e8c461505|null|b85c5b628021b140005ba7351f6d35c841eb2321:5670634|l2pebqag|52f4e1ccb94164870cd8325aaabc28dda5f81ef7|s_502f6a55e6d8|d21c59da1a43a5a3f1cc07fbe4fde90b1d0e4c08:24|l2r4p1b4|36bf28f8a9641fd67c3ec505815ba140ddea0d18|s_419afe53a6bb|9d0601224595f91beca9421a16aa1635205969c7',
#     'BMR': 's=1651641927374&r=https%3A%2F%2Fm.blog.naver.com%2Fwideeyed%2F221541104629&r2=https%3A%2F%2Fwww.google.com%2F',
#     'NID_SES': 'AAABqsiOTwExzkDNUGx/dCsod9ejmaIgWU+6dtDmFac2QP+To9r0PfhxQ4qTFMTgRBFSFMqrZNEeIKXIZzBz+jBBqLT04iua8tUvupRLijd4hi7hrniyk37AHyWv1Q/ApAmzsdwjjtp4RrNiVmY0V8FsqvTA8btavY8+utTWDiTIB+y1yxtt1dmxWCW0QhJNAacSkhUBvY1thE3Wxy0wP0dc2SbndXKo1x+eQVOtKdjUVTAy0NeIfSFklVT/Xt8aUYLqvHBg5/peIjIcz7mFAcQMby/6a9EYB/AZf7OjdwbOTqRBeSIllAbWFlcPxMDXq1aYLUE3kUwfVQsH9A9Ab820IHj8uoWRvahVAIbYa4d2hS+mp0bE/odINgGf/y9/5jbHTJ2hEUjTgFETcGXUZfFQ9AmZhFaguGqmc0AUlJTBUea11Ucr525ooigoUu5iaaHtmXXm37KBMU4l3kjft03v4F/+5EIyLjWyIoO58Ye/tSC5XZwqP9hHe9yJfKDa4HSB/mrMH4DUwV5Cz5TCTUKPZt+2v/99pwmk381EwbVUCTdve5k18OCg1Wgb2YpajM0/1g==',
#     'wcs_bt': 'sc_2bd6f0d33777d_epqua:1651761864|sc_25d3d61ffb145_kyn:1651761860|sc_2898182826729_ydt:1651761858|sc_13a254b497e07_zhv:1651761856|sc_13c9f70915e42_niepg:1651645718|sc_bff570689296_raiga:1651645128|sc_b4730e3b8892_uajxw:1651643581|sc_2fac329d4d650_l7yma:1651564579|sc_db50d7874966_eefz8:1651455196|sc_31ee7e467aaba_jyaax:1651213473',
# }

headers = {
    'authority': 'shopping.naver.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'NNB=PAQF2L7C6DFWA; AD_SHP_BID=9; ASID=36b4314a0000017aa8b13d1800005d61; MM_NEW=1; NFS=2; NDARK=Y; autocomplete=use; _ga_1BVHGNLQKG=GS1.1.1649754168.4.0.1649754196.0; NV_WETR_LAST_ACCESS_RGN_M="MTQxMTA2MzA="; NV_WETR_LOCATION_RGN_M="MTQxMTA2MzA="; nid_inf=1764228022; NID_AUT=nA5vPlUxT/q10CWr843fmjLqVCMWoC4sod9BAogmDQpPKiJCfhmkPru+hihZMMqt; NID_JKL=viT11G2dDPUH7lXr1sbyCvZTa6lGIya977Nqbkh/Ino=; _ga=GA1.2.1439908789.1623999453; _ga_7VKFYR6RV1=GS1.1.1651198031.81.1.1651198039.52; nx_ssl=2; page_uid=hFvltlp0JXVsskRIy+8ssssssM4-457497; NA_CO=ct%3Dl2q6bfs5%7Cci%3Dshoppingwindow%7Ctr%3Dswl%7Chk%3D42906f675ec1ab37cb5c294304adba2367fa99ba%7Ctrx%3D; spage_uid=hFvltlp0JXVsskRIy%2B8ssssssM4-457497; ncpa=95694|l2ontn2g|5a753e745efad48f05e5a02eb87c3b6e8c461505|null|b85c5b628021b140005ba7351f6d35c841eb2321:5670634|l2pebqag|52f4e1ccb94164870cd8325aaabc28dda5f81ef7|s_502f6a55e6d8|d21c59da1a43a5a3f1cc07fbe4fde90b1d0e4c08:24|l2r4p1b4|36bf28f8a9641fd67c3ec505815ba140ddea0d18|s_419afe53a6bb|9d0601224595f91beca9421a16aa1635205969c7; BMR=s=1651641927374&r=https%3A%2F%2Fm.blog.naver.com%2Fwideeyed%2F221541104629&r2=https%3A%2F%2Fwww.google.com%2F; NID_SES=AAABqsiOTwExzkDNUGx/dCsod9ejmaIgWU+6dtDmFac2QP+To9r0PfhxQ4qTFMTgRBFSFMqrZNEeIKXIZzBz+jBBqLT04iua8tUvupRLijd4hi7hrniyk37AHyWv1Q/ApAmzsdwjjtp4RrNiVmY0V8FsqvTA8btavY8+utTWDiTIB+y1yxtt1dmxWCW0QhJNAacSkhUBvY1thE3Wxy0wP0dc2SbndXKo1x+eQVOtKdjUVTAy0NeIfSFklVT/Xt8aUYLqvHBg5/peIjIcz7mFAcQMby/6a9EYB/AZf7OjdwbOTqRBeSIllAbWFlcPxMDXq1aYLUE3kUwfVQsH9A9Ab820IHj8uoWRvahVAIbYa4d2hS+mp0bE/odINgGf/y9/5jbHTJ2hEUjTgFETcGXUZfFQ9AmZhFaguGqmc0AUlJTBUea11Ucr525ooigoUu5iaaHtmXXm37KBMU4l3kjft03v4F/+5EIyLjWyIoO58Ye/tSC5XZwqP9hHe9yJfKDa4HSB/mrMH4DUwV5Cz5TCTUKPZt+2v/99pwmk381EwbVUCTdve5k18OCg1Wgb2YpajM0/1g==; wcs_bt=sc_2bd6f0d33777d_epqua:1651761864|sc_25d3d61ffb145_kyn:1651761860|sc_2898182826729_ydt:1651761858|sc_13a254b497e07_zhv:1651761856|sc_13c9f70915e42_niepg:1651645718|sc_bff570689296_raiga:1651645128|sc_b4730e3b8892_uajxw:1651643581|sc_2fac329d4d650_l7yma:1651564579|sc_db50d7874966_eefz8:1651455196|sc_31ee7e467aaba_jyaax:1651213473',
    'referer': 'https://shopping.naver.com/outlet/stores/100222653',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

response = requests.get('https://shopping.naver.com/v1/products?_nc_=1651676400000&subVertical=OUTLET&page=3&pageSize=10&sort=RECENT&filter=ALL&displayType=CATEGORY_HOME&includeZzim=true&includeViewCount=true&includeStoreCardInfo=true&includeStockQuantity=true&includeBrandInfo=false&includeBrandLogoImage=false&includeRepresentativeReview=false&includeListCardAttribute=false&includeRanking=false&includeRankingByMenus=false&includeStoreCategoryName=false&includeIngredient=false&menuId=0&storeId=100222653&standardSizeKeys\\[\\]=&standardColorKeys\\[\\]=&optionFilters\\[\\]=&attributeValueIds\\[\\]=&attributeValueIdsAll\\[\\]=&certifications\\[\\]=&filterTodayDelivery=false&filterFreeReturnInsurance=false&filterHopeDelivery=false',  headers=headers)