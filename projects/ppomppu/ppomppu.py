import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'rrr_bn_h=1; m_gad_pos_passback_1=1; m_gad_pos_passback_4=1; m_gad_pos_passback_6=1; m_gad_pos_passback_8=1; m_gad_pos_passback_9=1; m_gad_pos_passback_10=1; m_gad_pos_passback_12=1; m_gad_pos_passback_15=1; m_gad_pos_passback_16=1; m_gad_pos_passback_17=1; m_gad_pos_passback_18=1; m_gad_pos_passback_21=1; m_gad_pos_passback_22=1; m_gad_pos_passback_25=1; m_gad_pos_passback_50=1; m_gad_pos_passback_51=1; m_gad_pos_passback_52=1; m_gad_pos_passback_55=1; m_gad_pos_passback_58=1; PHPSESSID=jncjt8g27aaua3u2e7muv3l0s1; nxc=nxc_1649656626; forum_recent_visit_list=gamer; _ga=GA1.3.659872633.1649656626; _gid=GA1.3.1429717520.1649656626; bbs_bn=19; last_comment_view_time=1649656646; bl_bn=18; _gat=1; ts_bn=16; rrr_banner=14; m_gad_pos_1=25; m_gad_pos_4=23; m_gad_pos_6=18; m_gad_pos_8=9; m_gad_pos_9=11; m_gad_pos_10=23; m_gad_pos_12=20; m_gad_pos_15=23; m_gad_pos_16=26; m_gad_pos_17=10; m_gad_pos_18=25; m_gad_pos_21=11; m_gad_pos_22=11; m_gad_pos_25=22; m_gad_pos_50=27; m_gad_pos_51=11; m_gad_pos_52=27; m_gad_pos_55=22; m_gad_pos_58=21',
    'Referer': 'https://www.ppomppu.co.kr/search_bbs.php?bbs_cate=&keyword=%B8%C7%BD%C3%C6%BC+%B8%AE%B9%F6%C7%AE',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.ppomppu.co.kr/search_bbs.php?bbs_cate=&keyword=%B8%C7%BD%C3%C6%BC+%B8%AE%B9%F6%C7%AE', headers=headers)