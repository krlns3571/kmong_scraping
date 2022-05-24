import requests
import json

# coding: utf-8
import datetime
import os
import time

import pandas as pd

file_datetime = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
try:
    os.mkdir(f'./{file_datetime}')
except:
    pass

# cookies = {
#     # 'NNB': 'CMKGSOMBEFYWE',
#     'NNB': 'IQ3U4HJCV5XWE',
# }

headers = {
    'authority': 'shopping.naver.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko',
    # 'cookie': 'NNB=CMKGSOMBEFYWE',
    'referer': 'https://shopping.naver.com/outlet/branch/10217001',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

params = {
    '_nc_': '1651503600000',
    'subVertical': 'OUTLET',
}


def print_xlsx(list_, path, header, header_size):
    df = pd.DataFrame(list_, )
    writer = pd.ExcelWriter(f"./{file_datetime}/{path}.xlsx", engine='xlsxwriter', engine_kwargs={'options': {'strings_to_urls': False}})
    df.to_excel(writer, header=header, index=False)
    for column, column_length in zip(df, header_size):
        col_idx = df.columns.get_loc(column)
        writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_length)
    writer.close()


options = json.loads(
    requests.get('https://shopping.naver.com/v1/menu-aggregations/0/standard-option-filters', params=params).text)

# url = "https://shopping.naver.com/outlet/branch/10217001?menu=10000462"
try:
    url = input('url을 입력해주세요 ex) "https://shopping.naver.com/outlet/branch/10217001?menu=10000462" : \n')

    if url.find("shopping.naver.com/")<0:
        raise ValueError('유효하지 않은 url입니다.')
        # exit(1)

    page = 0
    cate_id = url.split('/')[-1].split('?')[0]

    try:
        menu_id = url.split('/')[-1].split('?')[-1].split('menu=')[1]
    except:
        menu_id = 0
    result = []
    result2 = []
    while True:
        page += 1
        print(f'\r{page} 페이지 진행중', end='')
        time.sleep(.2)
        response = requests.get(
            f'https://shopping.naver.com/v1/products?_nc_=1651503600000&subVertical=OUTLET&page={page}&pageSize=10&sort=RECENT&filter=ALL&displayType=CATEGORY_HOME&includeZzim=true&includeViewCount=true&includeStoreCardInfo=true&includeStockQuantity=true&includeBrandInfo=false&includeBrandLogoImage=false&includeRepresentativeReview=false&includeListCardAttribute=false&includeRanking=false&includeRankingByMenus=false&includeStoreCategoryName=false&includeIngredient=false&menuId={menu_id}&storeCategoryId={cate_id}&standardSizeKeys\\[\\]=&standardColorKeys\\[\\]=&optionFilters\\[\\]=&attributeValueIds\\[\\]=&attributeValueIdsAll\\[\\]=&certifications\\[\\]=&filterTodayDelivery=false&filterFreeReturnInsurance=false&filterHopeDelivery=false',
            headers=headers)
        products = json.loads(response.text)['products']
        if not products:
            response = requests.get(
                f'https://shopping.naver.com/v1/products?_nc_=1651503600000&subVertical=OUTLET&page={page}&pageSize=10&sort=RECENT&filter=ALL&displayType=CATEGORY_HOME&includeZzim=true&includeViewCount=true&includeStoreCardInfo=true&includeStockQuantity=true&includeBrandInfo=false&includeBrandLogoImage=false&includeRepresentativeReview=false&includeListCardAttribute=false&includeRanking=false&includeRankingByMenus=false&includeStoreCategoryName=false&includeIngredient=false&menuId={menu_id}&storeId={cate_id}&standardSizeKeys\\[\\]=&standardColorKeys\\[\\]=&optionFilters\\[\\]=&attributeValueIds\\[\\]=&attributeValueIdsAll\\[\\]=&certifications\\[\\]=&filterTodayDelivery=false&filterFreeReturnInsurance=false&filterHopeDelivery=false',
                headers=headers)
            products = json.loads(response.text)['products']
        if not products:
            response = requests.get(
                f'https://shopping.naver.com/v1/products?_nc_=1651762800000&subVertical=DEPARTMENT&page={page}&pageSize=10&sort=RECENT&filter=ALL&displayType=CATEGORY_HOME&includeZzim=true&includeViewCount=true&includeStoreCardInfo=true&includeStockQuantity=true&includeBrandInfo=false&includeBrandLogoImage=false&includeRepresentativeReview=false&includeListCardAttribute=false&includeRanking=false&includeRankingByMenus=false&includeStoreCategoryName=false&includeIngredient=false&menuId={menu_id}&storeCategoryId={cate_id}&standardSizeKeys\\[\\]=&standardColorKeys\\[\\]=&optionFilters\\[\\]=&attributeValueIds\\[\\]=&attributeValueIdsAll\\[\\]=&certifications\\[\\]=&filterTodayDelivery=false&filterFreeReturnInsurance=false&filterHopeDelivery=false',
                headers=headers)
            products = json.loads(response.text)['products']
            if not products:
                response = requests.get(
                    f'https://shopping.naver.com/v1/products?_nc_=1651762800000&subVertical=DEPARTMENT&page={page}&pageSize=10&sort=RECENT&filter=ALL&displayType=CATEGORY_HOME&includeZzim=true&includeViewCount=true&includeStoreCardInfo=true&includeStockQuantity=true&includeBrandInfo=false&includeBrandLogoImage=false&includeRepresentativeReview=false&includeListCardAttribute=false&includeRanking=false&includeRankingByMenus=false&includeStoreCategoryName=false&includeIngredient=false&menuId={menu_id}&storeId={cate_id}&standardSizeKeys\\[\\]=&standardColorKeys\\[\\]=&optionFilters\\[\\]=&attributeValueIds\\[\\]=&attributeValueIdsAll\\[\\]=&certifications\\[\\]=&filterTodayDelivery=false&filterFreeReturnInsurance=false&filterHopeDelivery=false',
                    headers=headers)
                products = json.loads(response.text)['products']
                if not products:
                    break
        products_info = [
            [str(datetime.datetime.strptime(products[0]['createdAt'].split('.')[0],'%Y-%m-%dT%H:%M:%S')), x['channel']['name'], x['name'], x['salePrice'], x['pcDiscountPrice'], x['naverShoppingCategory']['wholeName'],
             f"https://shopping.naver.com/outlet/stores/{x['channel']['_id']}/products/{x['_id']}"] for x in
            products]
        products_info2 = [
            [str(datetime.datetime.strptime(products[0]['createdAt'].split('.')[0],'%Y-%m-%dT%H:%M:%S')), x['channel']['name'], x['name'], x['salePrice'], x['pcDiscountPrice'], x['naverShoppingCategory']['wholeName'],
             f"https://shopping.naver.com/outlet/stores/{x['channel']['_id']}/products/{x['_id']}"] for x in
            products]
        try:
            brandname = products[0]['channel']['name']
        except:
            pass
        colors = [[xx['key'] for xx in x['standardColors']] for x in products]
        sizes = [x['standardSizes'] for x in products]

        cc = [[]] * len(products)
        cc2 = [[]] * len(products)
        xx = [[]] * len(products)
        xx2 = [[]] * len(products)

        for idx, size in enumerate(sizes):
            op = []
            for s in size:
                for option in options:
                    if s == option['key']:
                        op.append(option['name'])
                cc[idx] = ",".join(op)
                cc2[idx] = op

        for idx, size in enumerate(colors):
            op = []
            for s in size:
                for option in options:
                    if s == option['key']:
                        op.append(option['name'])
                xx[idx] = ",".join(op)
                xx2[idx] = op

        [_.append(xx[idx] if xx[idx] else '') for idx, _ in enumerate(products_info)]
        [_.append(cc[idx] if cc[idx] else '') for idx, _ in enumerate(products_info)]

        [_.extend(xx2[idx] if xx[idx] else '') for idx, _ in enumerate(products_info2)]
        [_.extend(cc2[idx] if cc[idx] else '') for idx, _ in enumerate(products_info2)]
        [result.append(x) for x in products_info]
        [result2.append(x) for x in products_info2]

    print_xlsx(result, '결과물', ['생성일', '브랜드', '상품명', '소비자가격', '판매가', '카테고리', 'url', '색상', '사이즈'], [20,10, 20, 10, 10, 20, 20, 20, 20])
    print_xlsx(result2, '결과물2',
               ['생성일', '브랜드', '상품명', '소비자가격', '판매가', '카테고리', 'url'] + ['색상or사이즈'] * (
                           max([len(x) for x in result2]) - 7),
               [20, 10, 20, 10, 10, 20, 20])
    print(f"\n{os.path.abspath(f'./{file_datetime}')} 에 모든 결과가 저장되었습니다.\n해당 창은 꺼주셔도 좋습니다.")
    exit(1)
except Exception as e:
    print(e)
    with open(r'error.txt', 'w', encoding='utf8') as f:
        f.write(str(e))
    time.sleep(10)
