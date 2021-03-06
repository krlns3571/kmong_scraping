import requests

cookies = {
    'searchConfigBody': 'null',
    '__utmc': '155360100',
    'INFO21CSESSID': 'hk26tglbo79u75alhthf5d43b3',
    'SVRIP': '200',
    '__INFO21C__USERNAME': 'uirim',
    'uid': 'uirim',
    '_csrf-frontend': '13fa45a804e6e444922f176ff112925f39801cc47d493c97ac44d374b25e26a7a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22aJi-ioMK4rEVdPHsj77EJT-EADHsTCmV%22%3B%7D',
    '__utma': '155360100.1377155290.1653011370.1653017394.1653022429.3',
    '__utmz': '155360100.1653022429.3.2.utmcsr=infose.info21c.net|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__utmt': '1',
    'pageSize': '15',
    '__utmb': '155360100.8.10.1653022429',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'searchConfigBody=null; __utmc=155360100; INFO21CSESSID=hk26tglbo79u75alhthf5d43b3; SVRIP=200; __INFO21C__USERNAME=uirim; uid=uirim; _csrf-frontend=13fa45a804e6e444922f176ff112925f39801cc47d493c97ac44d374b25e26a7a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22aJi-ioMK4rEVdPHsj77EJT-EADHsTCmV%22%3B%7D; __utma=155360100.1377155290.1653011370.1653017394.1653022429.3; __utmz=155360100.1653022429.3.2.utmcsr=infose.info21c.net|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; pageSize=15; __utmb=155360100.8.10.1653022429',
    'Referer': 'https://infose.info21c.net/info21c/bids/list/index?mode=&page=1&bid_suc=bid&division=5&searchtype=&userid=uirim&searchWord=&bidtype=con&g2bcode=&itemcode=&keyword=&location=&locationLoc=&whereis=&bid_opt=&contract=&delay=&cancel=&ulevel=&contract_sys=&convention=&sort=-writedt&bid_kind=&word_type=&subWord=&itemcodeAll=&keywordAll=&g2bcodeAll=&whereisAll=&locationAll=&bid_optAll=&conlevel=&pageSize=15&conlevel=',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = [
    ('mode', ''),
    ('page', '1'),
    ('bid_suc', 'bid'),
    ('division', '5'),
    ('searchtype', ''),
    ('userid', 'uirim'),
    ('searchWord', ''),
    ('bidtype', 'con'),
    ('g2bcode', ''),
    ('itemcode', ''),
    ('keyword', ''),
    ('location', ''),
    ('locationLoc', ''),
    ('whereis', ''),
    ('bid_opt', ''),
    ('contract', ''),
    ('delay', ''),
    ('cancel', ''),
    ('ulevel', ''),
    ('contract_sys', ''),
    ('convention', ''),
    ('sort', '-writedt'),
    ('bid_kind', ''),
    ('word_type', ''),
    ('subWord', ''),
    ('itemcodeAll', ''),
    ('keywordAll', ''),
    ('g2bcodeAll', ''),
    ('whereisAll', ''),
    ('locationAll', ''),
    ('bid_optAll', ''),
    ('conlevel', ''),
    ('pageSize', '100'),
    ('conlevel', ''),
]

response = requests.get('https://infose.info21c.net/info21c/bids/list/index', params=params, cookies=cookies, headers=headers)