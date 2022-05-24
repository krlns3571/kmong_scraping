import json

import requests

cookies = {
    'KHANUSER': 'z60gc3ne1s7oif',
    'JSESSIONID': 'koKEThn77tbhiO40AE51a1dqB4J9dRWSeY4lQeOr.doc24-13',
    'DOC24_MBER_SE': 'C',
    'DOC24_MBER_SE_ENTRPRS': 'CA',
    'DOC24_MBER_LOGINSESSIONID': 'koKEThn77tbhiO40AE51a1dqB4J9dRWSeY4lQeOr',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'Accept': '*/*',
    'Content-Type': 'application/json;charset=UTF-8',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://docu.gdoc.go.kr',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://docu.gdoc.go.kr/doc/wte/docWriteForm.do',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'KHANUSER=z60gc3ne1s7oif; JSESSIONID=koKEThn77tbhiO40AE51a1dqB4J9dRWSeY4lQeOr.doc24-13; DOC24_MBER_SE=C; DOC24_MBER_SE_ENTRPRS=CA; DOC24_MBER_LOGINSESSIONID=koKEThn77tbhiO40AE51a1dqB4J9dRWSeY4lQeOr',
}
result = []
data = '{"orderNm":1,"parentoucode":"0000000"}'

res = requests.post('https://docu.gdoc.go.kr/cmm/ldap/jstree/search', headers=headers, cookies=cookies, data=data)


def test1(res, cnt):
    for value in json.loads(res.text):
        result.append('\t'*cnt + value['text'])
        if value['children']:

            code = value['id']
            data = '{"orderNm":1,"parentoucode":"%s"}' % code
            res = requests.post('https://docu.gdoc.go.kr/cmm/ldap/jstree/search', headers=headers, cookies=cookies,
                                data=data)
            test1(res,cnt+1)
        else:
            pass

cnt = 0
test1(res, cnt)

print(result)
