import requests

cookies = {
    'WMONID': 'M-f4ASGhyaT',
    'JSESSIONID': 'zIK5KCXaWzWg0a4B0Df2oNEYMESRqJbcVx6LgarHFBVZ89Uo7aptW3aPKYeXEQN7.hostingwas2_servlet_engine8',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'WMONID=M-f4ASGhyaT; JSESSIONID=zIK5KCXaWzWg0a4B0Df2oNEYMESRqJbcVx6LgarHFBVZ89Uo7aptW3aPKYeXEQN7.hostingwas2_servlet_engine8',
    'Origin': 'https://seoul.sen.hs.kr',
    'Referer': 'https://seoul.sen.hs.kr/77702/subMenu.do',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'bbsId': 'BBSMSTR_000000011985',
    'bbsTyCode': 'dliv',
    'customRecordCountPerPage': '10',
    'pageIndex': '1',
    'searchCondition': '',
    'searchKeyword': '',
    'checkNttId': '',
    'mvmnReturnUrl': '',
}

response = requests.post('https://seoul.sen.hs.kr/dggb/module/board/selectBoardListAjax.do', headers=headers, cookies=cookies, data=data)