import os

import pandas as pd

from main import Handler



h = Handler()

results = h.get_pd()
# results2 = h.get_pd2()

# print(pd.DataFrame.from_dict([value.result for value in results]))
xx = [value.result for value in results]
cc = [{'product':value.url} for value in results]
bb = [value.cat for value in results]
# for value in xx:
#     try:
#         cc.append({'링크'+str(x+1):y for  x,y in enumerate(value['SNS및외부링크'].split('\n'))})
#     except:
#         cc.append({'링크1':''})

for x,c in zip(xx,cc):
    x.update(c)

for c, b in zip(xx, bb):
    c['img_name'] = os.path.abspath(f".\\img\\{b}\\{c['img_name']}").split('\\fabric')[1]

x1 = pd.DataFrame.from_dict(xx)
# x2 = pd.DataFrame.from_dict([value.result for value in results])

writer = pd.ExcelWriter('312312.xlsx', engine='xlsxwriter', )
# # # result = pd.concat(x1, axis=1)
# # # result = pd.concat([x, x1, x2, x3], axis=1)
x1.to_excel(writer)
writer.close()

# writer2 = pd.ExcelWriter('sample5557.xlsx', engine='xlsxwriter', )
# # # # result = pd.concat(x1, axis=1)
# # # # result = pd.concat([x, x1, x2, x3], axis=1)
# x2.to_excel(writer2)
# writer2.close()

# df = pd.read_excel('./test1.xlsx', engine='openpyxl')