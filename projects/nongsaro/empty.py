import os

import requests
import win32com.client as w3c

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ko-KR,ko;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'ACEUCI=1; JSESSIONID=DxPI6C2WhtZqev2OkkT1oZqFa7UBr2jr4cJYIjKIWBx8HfCn7wlAAdN05QsHhGmM.nongsaro-web_servlet_engine1; SCOUTER=z2kcu53pee8t16; ACEUACS=1650341957977151824; ACEFCID=UID-625E38451EBBCA3F95388B8D',
    'Origin': 'https://www.nongsaro.go.kr',
    'Referer': 'https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfo.ps?menuId=PS03618&sYear=2000&sUnit=0&sAtpt=4200000000&sTest=&eqpCode=&totalSearchYn=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'sYear': '2000',
    'eqpCode': '05010001',
    'sAtpt': '4200000000',
}

r = requests.post('https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfoDtl.ps', headers=headers, data=data)
with open(r'qwer.html', 'wb') as f:
    f.write(r.content)

excelApp = w3c.Dispatch('Excel.Application')
book = excelApp.Workbooks.Open(os.path.abspath('qwer.html'))
book.SaveAs(f'./test' + '.xlsx', 51)
excelApp.Quit()
