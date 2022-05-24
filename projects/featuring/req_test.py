import os
import requests

json_message = os.getenv('[[\"__json_message\"\0540\05425\054\"contact81')

cookies = {
    'ft_visitor_no': '1321763',
    '_gid': 'GA1.2.1337438964.1650506782',
    '_hjFirstSeen': '1',
    '_hjSession_2077791': 'eyJpZCI6IjI2YTY4YjM4LWMxZGYtNDg0My1iZGRhLTFhZDdhMmUxNTk3ZSIsImNyZWF0ZWQiOjE2NTA1MDY3ODE4MTIsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    'ch-veil-id': '09f6c9c3-d803-4a93-9bee-6001d5af468b',
    '_hjSessionUser_2077791': 'eyJpZCI6IjYyNWNhMmYwLTUwZTYtNTJkYy1iOGQ4LTNiZDcxYjMzODdkYSIsImNyZWF0ZWQiOjE2NTA1MDY3ODE1ODQsImV4aXN0aW5nIjp0cnVlfQ==',
    'messages': f"\"4af58b6af1bba6fc37e034d7b4ee6c874129415a{json_message} \\\\uc73c\\\\ub85c \\\\ub85c\\\\uadf8\\\\uc778 \\\\ub418\\\\uc5c8\\\\uc2b5\\\\ub2c8\\\\ub2e4.\\\"]]\"",
    'csrftoken': '34jdiTfQwPgv9UI0ZUuOzMGk1qJDOlhwz4HYZpTxwq3N28gF0dYD0l9MrTuqClGA',
    'sessionid': 'xkozqz0g166p9vub78rf0zpe30b0g26t',
    'feat_user_id': '9330',
    '_ga': 'GA1.2.1616702084.1650506782',
    'ch-session-19932': 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiIxOTkzMi02MjYwYmMxZjgxZDhjZjk0NTljOCIsImlhdCI6MTY1MDUwNjgxMiwiZXhwIjoxNjUzMDk4ODEyfQ.vJ_K0nWUQBTF4_H3K-VZy_yBMkwTCue5YxL6In9Pilg',
    '_ga_3DCCGMWD39': 'GS1.1.1650506781.1.1.1650507175.0',
}

headers = {
    'authority': 'featuring.co',
    'accept': '*/*',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': f"ft_visitor_no=1321763; _gid=GA1.2.1337438964.1650506782; _hjFirstSeen=1; _hjSession_2077791=eyJpZCI6IjI2YTY4YjM4LWMxZGYtNDg0My1iZGRhLTFhZDdhMmUxNTk3ZSIsImNyZWF0ZWQiOjE2NTA1MDY3ODE4MTIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; ch-veil-id=09f6c9c3-d803-4a93-9bee-6001d5af468b; _hjSessionUser_2077791=eyJpZCI6IjYyNWNhMmYwLTUwZTYtNTJkYy1iOGQ4LTNiZDcxYjMzODdkYSIsImNyZWF0ZWQiOjE2NTA1MDY3ODE1ODQsImV4aXN0aW5nIjp0cnVlfQ==; messages=\"4af58b6af1bba6fc37e034d7b4ee6c874129415a{[[\\\"__json_message\\\"\\0540\\05425\\054\\\"contact81} \\\\uc73c\\\\ub85c \\\\ub85c\\\\uadf8\\\\uc778 \\\\ub418\\\\uc5c8\\\\uc2b5\\\\ub2c8\\\\ub2e4.\\\"]]\"; csrftoken=34jdiTfQwPgv9UI0ZUuOzMGk1qJDOlhwz4HYZpTxwq3N28gF0dYD0l9MrTuqClGA; sessionid=xkozqz0g166p9vub78rf0zpe30b0g26t; feat_user_id=9330; _ga=GA1.2.1616702084.1650506782; ch-session-19932=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiIxOTkzMi02MjYwYmMxZjgxZDhjZjk0NTljOCIsImlhdCI6MTY1MDUwNjgxMiwiZXhwIjoxNjUzMDk4ODEyfQ.vJ_K0nWUQBTF4_H3K-VZy_yBMkwTCue5YxL6In9Pilg; _ga_3DCCGMWD39=GS1.1.1650506781.1.1.1650507175.0",
    'referer': 'https://featuring.co/featapp/apps/discover/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.get('https://featuring.co/featapp/wrapper/Discover/', headers=headers, cookies=cookies)

"https://featuring.co/featapp/apps/discover/?follower=2&category=11&language=1&page_num=1"