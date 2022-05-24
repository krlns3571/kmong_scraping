import requests

headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'rrr_bn_h=1; m_gad_pos_passback_1=1; m_gad_pos_passback_4=1; m_gad_pos_passback_6=1; m_gad_pos_passback_8=1; m_gad_pos_passback_9=1; m_gad_pos_passback_10=1; m_gad_pos_passback_12=1; m_gad_pos_passback_15=1; m_gad_pos_passback_16=1; m_gad_pos_passback_17=1; m_gad_pos_passback_18=1; m_gad_pos_passback_21=1; m_gad_pos_passback_22=1; m_gad_pos_passback_25=1; m_gad_pos_passback_50=1; m_gad_pos_passback_51=1; m_gad_pos_passback_52=1; m_gad_pos_passback_55=1; m_gad_pos_passback_58=1; PHPSESSID=jncjt8g27aaua3u2e7muv3l0s1; nxc=nxc_1649656626; forum_recent_visit_list=gamer; _ga=GA1.3.659872633.1649656626; _gid=GA1.3.1429717520.1649656626; bbs_bn=22; bl_bn=25; mc_bn=11; mb_bn=5; t_bn=11; ts_bn=30; rrr_banner=28; m_gad_pos_1=39; m_gad_pos_4=37; m_gad_pos_6=32; m_gad_pos_8=23; m_gad_pos_9=25; m_gad_pos_10=37; m_gad_pos_12=34; m_gad_pos_15=37; m_gad_pos_16=40; m_gad_pos_17=24; m_gad_pos_18=39; m_gad_pos_21=25; m_gad_pos_22=25; m_gad_pos_25=36; m_gad_pos_50=41; m_gad_pos_51=25; m_gad_pos_52=41; m_gad_pos_55=36; m_gad_pos_58=35; last_comment_view_time=1649657296; _gali=page_list',
    'Referer': 'https://www.ppomppu.co.kr/zboard/view.php?id=gamer&page=4&divpage=10&no=52942',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': 'gamer',
    'no': '52942',
    'c_page': '1',
    'comment_mode': '',
}

response = requests.get('https://www.ppomppu.co.kr/zboard/comment.php', headers=headers, params=params)