import requests


headers = {
    'authority': 'search.map.kakao.com',
    'accept': '*/*',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'TIARA=ABZFk3s6B2wEQeCxxGmePZ2HeNUhw8I5iPutRL9NpJcdMLCwxvrT179guFysJRkwAFJlhcRzVOuw.ouZaQ9.whaj_ukIeamgR3hOnXuZ1OQ0; _kadu=plll_LqH4aKQj2gb_1624869295339; webid=66fb84b0de3311eb9887000af759d260; webid_ts=1625559791739; _karb=RWlf_SpkSctdmdPg_1627367570399; _ga=GA1.2.156159128.1628830509; _kptid=d601630aa55e40e99bf310750a416915; kd_lang=ko; _kdt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkZXZlbG9wZXJJZCI6MjIwNzA4LCJ0b2tlbiI6ImMxNmY0ZjljY2ZmZmZmYmQ0ZjAwNmE0OWYxZTdiMDQ5ODFlYmRkYWE4M2VmNmViZGE4N2E1MjlkZWNmNWY2ZDgifQ.Z23fT0J8SZF1uq-z2t3I8GmZZyc5IZtgUZcNo5RP6Bk; _pfdl=y; _kahai=3db98e2c83b9621a93c2ced9925e19eacdef4548073f7d23fc345a67f4353cbb; _gapuser=true; _kawlt=liST6YVP5SOewCJQAq85vdgD9ONT9EQov0tyeXm8PiTxqgAvRJ2mP2zAccOEwnqXjS5f4pGBqU7IyRV5Wg1eWJsDPJPwQm9Div92lrrjbogQhTjc6LB6f4qbfr3geat_; _kawltea=1650316824; _karmt=9b3aKt3mreC9N2E4NzJ5P2RMqFSTCIjYCv0lsHGtknwOM0sd6VLDjs-SH6dyp4bk; _karmtea=1650327624; __T_=1; _T_ANO=BY/DDpzwzmnGvv6FF6x2I9dNJQ20w9LQPAaaOplFIEefcbsndNGZOcg/dpCOchTHBEgp+vHBx0kNrE/iak0viUNp3MaXqJ1lo6CDHiX6PUF0MdONmPk39RFAAoEvzsFoJnjVnsqHUWQmZo5LZ0HpdsoFGEMyY6UVbz1fPzA/39ZSchfG6nvCEoZWqYSBLJ9Cjq48qpaV6BRwHH8UvVt2yYJ2imeEezZqv+1QaKZWerhfDyOsMvw7QSt9oQGZfcNsK2ES8a6GQTfs96gfxrcswagGISj1A0Uc8/OGZGX9mg86SHcxDIbuCMdRL1+7nRb5bmm/trGcjks+SkVBu3r+GA==',
    'referer': 'https://map.kakao.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

params = {
    'callback': 'jQuery181040815182978995646_1650257106870',
    'q': '강남역 병원',
    'msFlag': 'S',
    'page': '1',
    'sort': '0',
}

response = requests.get('https://search.map.kakao.com/mapsearch/map.daum', headers=headers, params=params)