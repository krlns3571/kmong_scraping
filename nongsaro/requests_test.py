import pandas as pd
import requests


headers = {
    'Accept': '*/*',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'ACEUCI=1; JSESSIONID=Egb7jJajMHpZ9b2WE57fVbUnWSwts29L9y7qd2KOKlr4aMM07Z35a123rYzRLUS5.nongsaro-web_servlet_engine1; SCOUTER=z6q45e3mk7t7a; ACEUACS=1624611629429151824; ACEFCID=UID-6259438459BB930989D232E6',
    'Origin': 'https://www.nongsaro.go.kr',
    'Referer': 'https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfo.ps?menuId=PS03618&sYear=2012&sUnit=0&sAtpt=9900000000&sTest=&eqpCode=&totalSearchYn=',
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
    'sYear': '2012',
    'eqpCode': '05010001',
    'sAtpt': '9900000000',
}
x1 = pd.read_html(requests.post('https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfoDtl.ps', headers=headers, data=data).text)
response = requests.post('https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfoDtl.ps', headers=headers, data=data)