import requests

cookies = {
    'ACEUCI': '1',
    'JSESSIONID': '8E4UoOZHRrAyvyGA1WY4zudiIEGErurt4cng81AaQRCSd6bh7cpfCGzWndQwvRRX.nongsaro-web_servlet_engine1',
    'SCOUTER': 'x68gtf766ialk',
    'ACEUACS': '1650329860371151824',
    'ACEFCID': 'UID-625E09033C7CD1EF97399203',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ko-KR,ko;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'ACEUCI=1; JSESSIONID=8E4UoOZHRrAyvyGA1WY4zudiIEGErurt4cng81AaQRCSd6bh7cpfCGzWndQwvRRX.nongsaro-web_servlet_engine1; SCOUTER=x68gtf766ialk; ACEUACS=1650329860371151824; ACEFCID=UID-625E09033C7CD1EF97399203',
    'Origin': 'https://www.nongsaro.go.kr',
    'Referer': 'https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfo.ps?menuId=PS03618&sYear=2013&sUnit=0&sAtpt=9900000000&sTest=&eqpCode=&totalSearchYn=',
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
    'sYear': '2013',
    'eqpCode': '05010001',
    'sAtpt': '9900000000',
}

response = requests.post('https://www.nongsaro.go.kr/portal/ps/psb/psbf/frmprdIncomeInfoDtl.ps', headers=headers, cookies=cookies, data=data)