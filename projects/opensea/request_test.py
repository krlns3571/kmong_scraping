import requests

headers = {
    'authority': 'opensea.io',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'cookie': '__cf_bm=g0vWreg6LI9BphCgbQkCsxbVzemcK4.LOF8E7ahvB2k-1647497790-0-AbqxDTBUvoGh0PpyzQgVHDl+qM4Ai8HfPH3gWjyJlXi3dOSt4dAhtVub94eKGrpZyXTG6SnvgmztR65gd+ESurk=; _gcl_au=1.1.1524993018.1647497786; _gid=GA1.2.1462819171.1647497786; _gat_UA-111688253-1=1; _gat_gtag_UA_111688253_1=1; _ga_9VSBF2K4BX=GS1.1.1647497786.1.1.1647498116.0; _ga=GA1.2.1341216135.1647497786; amp_ddd6ec=DkZa2dm93hswAPm9o1lJdE...1fub8acmp.1fub8kus7.i.g.12; _dd_s=rum=0&expire=1647499034961',
}

response = requests.get('https://opensea.io/activity', headers=headers)