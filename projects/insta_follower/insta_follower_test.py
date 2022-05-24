import requests

headers = {
    'authority': 'i.instagram.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'x-ig-www-claim': 'hmac.AR0OxSIdtPPfJgRjT-7Y-3mxy6HChvHjqXv6q-HlepB1-E8y',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'accept': '*/*',
    'x-asbd-id': '198387',
    'sec-ch-ua-platform': '"Windows"',
    'x-ig-app-id': '936619743392459',
    'origin': 'https://www.instagram.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.instagram.com/',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'cookie': 'mid=YPfjngALAAHy8i9C5GaQF3qM2VUn; ig_did=7547DB42-D6AB-4A4C-A71A-59BB50A6A535; ig_nrcb=1; csrftoken=RzYB0U69svko5VLYS1Y7toP9vnqtCao5; ds_user_id=49231192988; sessionid=49231192988%3AoMfGNvGOyjANvM%3A26; rur="NAO\\05449231192988\\0541677912175:01f770aff8bce4ce8a0bbdd6b48fd6c62ce18e6594fbe018805e19d39a08ab684f46f690"',
}

params = (
    ('count', '12'),
    ('max_id', 'QVFBcDNqRkFCQ29sbThUbVRMWmlmeDNQSGhMYjRGVjVEdkNLMkI5RW5wRDFySlYzemxzeTl4d3FIc0JNT3JzN25mZWNxMVhnV3JWVFBDRnI2X3JiZVpwUg=='),
    ('search_surface', 'follow_list_page'),
)

response = requests.get('https://i.instagram.com/api/v1/friendships/647188401/followers/', headers=headers, params=params)

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
#response = requests.get('https://i.instagram.com/api/v1/friendships/647188401/followers/?count=12&max_id=QVFBcDNqRkFCQ29sbThUbVRMWmlmeDNQSGhMYjRGVjVEdkNLMkI5RW5wRDFySlYzemxzeTl4d3FIc0JNT3JzN25mZWNxMVhnV3JWVFBDRnI2X3JiZVpwUg%3D%3D&search_surface=follow_list_page', headers=headers)