import requests

# cookies = {
#     'WMONID': 'MeZNvrvyWSe',
#     'JSESSIONID': 'uDIvEAvJKYDrxEHD3EImGd8q0KLyQgsmvVrFJMOHbaEJ55lF7HHoKluOQyqxQDAI.W4CAP1_servlet_HPT',
#     'wcs_bt': '119292d7c73a734:1650955119|b2cf8fe9c1fd8:1650955119|911a88f6efff40:1650955119',
# }

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'WMONID=MeZNvrvyWSe; JSESSIONID=uDIvEAvJKYDrxEHD3EImGd8q0KLyQgsmvVrFJMOHbaEJ55lF7HHoKluOQyqxQDAI.W4CAP1_servlet_HPT; wcs_bt=119292d7c73a734:1650955119|b2cf8fe9c1fd8:1650955119|911a88f6efff40:1650955119',
    'Referer': 'http://www.w4c.go.kr/fcltEtcSrv/welfareMap.do',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

params = {
    'FCLT_CD': 'K0161',
}

response = requests.get('http://www.w4c.go.kr/fcltEtcSrv/welfareSchDetail.do', params=params, headers=headers, verify=False)