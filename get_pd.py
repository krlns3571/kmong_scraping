import pandas as pd

from class101.get_result import Handler

h = Handler()

results = h.get_pd2()
# results2 = h.get_pd2()

# print(pd.DataFrame.from_dict([value.result for value in results]))
xx = [value.result for value in results]
cc = []
# for value in xx:
#     try:
#         cc.append({'링크'+str(x+1):y for  x,y in enumerate(value['SNS및외부링크'].split('\n'))})
#     except:
#         cc.append({'링크1':''})

# for x,c in zip(xx,cc):
#     x.update(c)

x1 = pd.DataFrame.from_dict(xx)
# x2 = pd.DataFrame.from_dict(xx[100000:200000])
# x3 = pd.DataFrame.from_dict(xx[200000:])
x1 = x1[
    ["스마트스토어 링크", "쇼핑몰명", "쇼핑몰 소개", "스토어 등급", "서비스만족", "스토어찜", "상호명", "사업자등록번호", "대표자", "사업장 소재지", "고객센터", "통신판매업번호",
     "e-mail", "카테고리", "방문자(투데이)", "수집시간", "방문자(통합)", "베스트", "카테고리별 상품수"]]
writer = pd.ExcelWriter('sample1.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})
# writer2 = pd.ExcelWriter('sample2.xlsx', engine='xlsxwriter', )
# writer3 = pd.ExcelWriter('sample3.xlsx', engine='xlsxwriter', )
# # # result = pd.concat(x1, axis=1)
# # # result = pd.concat([x, x1, x2, x3], axis=1)
x1.to_excel(writer)
# x2.to_excel(writer2)
# x3.to_excel(writer3)
writer.close()
# writer2.close()
# writer3.close()

# x1 = pd.DataFrame.from_dict(xx)
# # x2 = pd.DataFrame.from_dict([value.result for value in results])
#
# writer = pd.ExcelWriter('23123123.xlsx', engine='xlsxwriter', )
# # # # result = pd.concat(x1, axis=1)
# # # # result = pd.concat([x, x1, x2, x3], axis=1)
# x1.to_excel(writer)
# writer.close()

# writer2 = pd.ExcelWriter('sample5557.xlsx', engine='xlsxwriter', )
# # # # result = pd.concat(x1, axis=1)
# # # # result = pd.concat([x, x1, x2, x3], axis=1)
# x2.to_excel(writer2)
# writer2.close()

# df = pd.read_excel('./test1.xlsx', engine='openpyxl')
