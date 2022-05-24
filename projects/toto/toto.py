import requests

# cookies = {
#     'CCN_VKEY': 'ztaaf2ldq2nhd',
#     '__smVisitorID': '5W9p3dNVual',
#     'JSESSIONID': '23j7OnuBWPkh6RRXum3Zj7hsIEqI11u1kfOWd5m2qOr5JDyR72PyChkCYwirOgM2.amV1c19kb21haW4vRGJldG1hbjI0',
# }

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'CCN_VKEY=ztaaf2ldq2nhd; __smVisitorID=5W9p3dNVual; JSESSIONID=23j7OnuBWPkh6RRXum3Zj7hsIEqI11u1kfOWd5m2qOr5JDyR72PyChkCYwirOgM2.amV1c19kb21haW4vRGJldG1hbjI0',
    'Origin': 'https://www.betman.co.kr',
    'Referer': 'https://www.betman.co.kr/main/mainPage/gamebuy/winrstDetlIFR.do?gmId=G101&gmTs=220037&sbx_gmCase=&sbx_gmType=G101&ica_fromDt=2022.02.09&ica_endDt=2022.05.09&rdo=month3&curPage=1&perPage=10&isIFR=Y',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'gmId': 'G101',
    'gmTs': 220037,
    '_sbmInfo': {
        '_sbmInfo': {
            'debugMode': 'false',
        },
    },
}

response = requests.post('https://www.betman.co.kr/gamebuy/winrst/inqWinrstDetlBody.do',  headers=headers, json=json_data)