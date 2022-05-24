import requests

# cookies = {
#     'NNB': 'PAQF2L7C6DFWA',
#     'ASID': '36b4314a0000017aa8b13d1800005d61',
#     'MM_NEW': '1',
#     'NFS': '2',
#     '_ga_1BVHGNLQKG': 'GS1.1.1638347769.3.1.1638347785.0',
#     'NID_AUT': 'O/8DyXjyduSuHUsCD55s+rGQjy1+713ePNRUs+IuD7QwzkWQIJMZ2tFLTTfQ224Z',
#     'NID_JKL': 'agp6JkLLOUVIoFkyM/gUUluy1E+wCqSOhiGThGcoIWI=',
#     'NV_WETR_LOCATION_RGN_M': '"MDkxNDAxMDQ="',
#     'NDARK': 'Y',
#     '_gcl_au': '1.1.1790671045.1643863573',
#     'NV_WETR_LAST_ACCESS_RGN_M': '"MDkxNDAxMDQ="',
#     '_ga': 'GA1.2.1439908789.1623999453',
#     '_ga_7VKFYR6RV1': 'GS1.1.1648460920.72.0.1648461448.60',
#     'nx_ssl': '2',
#     'bk_language': 'ko',
#     'booking_access_615267': 'true',
#     'booking_access_538469': 'true',
#     'booking_access_551084': 'true',
#     'booking_access_497454': 'true',
#     'booking_access_406456': 'true',
#     'NID_SES': 'AAABqz3cIUFxQdCshE/7z2m0AdUfrR9yQB8HCz30BWcmndOvdkB6WNvOUJwOSToLssS16ANxCOnkMTqmH+sN4P4/5wPUVgZYObEllgvNtzCPJOniFa0C4hi1SL15i2DVdl2QxhVG3AuqZvAdRFWJ7TvE9Rb7xJbXGYHKcNVoGaoaMXH0dDjSbGoYWTPmks2FmOZdGeI3n2tcBBcTld+w5Qdu4YmV4j13lRzc/Rg0m8ze4dIkaVB5lWWYrOBwBdxBPFaDdqTiBSPbT3XfOwWoqNDsoAAZhS6AI5EdCJGG5aZ6nldhQxL8f4QUa/hXNpKO2heJ2imNql/8tUEG049gTj73mmJUyLYWSpl4c4GM+zXoF2/cx2dOYLbWBNEG0qosl0donG1iDSMP35tSQll7Bp+q8gD6Gju6c5zDCGXpU9xM4iL6PNSV251gnLX6DQ+AER6VlJ09Sy6j+8J/ojln14ZnK+ygq/37bKXkkZGSEK6UZReCWtR3atzA8LWNIQ5NowRrfNnimz3v5Zjq+cKMijlnn6eOi0KYSViouILVo3HBv+ZTJ26Ma6pu8F+YGu7Bjiulaw==',
#     'csrf_token': 'e8a64ed09c3fefebaed9d95c17bfe72b0f8b338059d84c27c656e0486ddb8aa7cb0e1528662e30825d437edd492bcef87de3ae72f78dce3a5d0cf12a2a24fc78',
# }

headers = {
    'authority': 'api.booking.naver.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    # 'x-csrf-token': 'd8dde07aa2b23a9ec38b0e5fc6e07bba0f8b338059d84c27c656e0486ddb8aa7cb0e1528662e30825d437edd492bcef87de3ae72f78dce3a5d0cf12a2a24fc78',
    'accept-language': 'ko',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'NONE',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://m.booking.naver.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://m.booking.naver.com/booking/6/bizes/538469/items/3963761?area=bmp&service-target=map-pc',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'NNB=PAQF2L7C6DFWA; ASID=36b4314a0000017aa8b13d1800005d61; MM_NEW=1; NFS=2; _ga_1BVHGNLQKG=GS1.1.1638347769.3.1.1638347785.0; NID_AUT=O/8DyXjyduSuHUsCD55s+rGQjy1+713ePNRUs+IuD7QwzkWQIJMZ2tFLTTfQ224Z; NID_JKL=agp6JkLLOUVIoFkyM/gUUluy1E+wCqSOhiGThGcoIWI=; NV_WETR_LOCATION_RGN_M="MDkxNDAxMDQ="; NDARK=Y; _gcl_au=1.1.1790671045.1643863573; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDAxMDQ="; _ga=GA1.2.1439908789.1623999453; _ga_7VKFYR6RV1=GS1.1.1648460920.72.0.1648461448.60; nx_ssl=2; bk_language=ko; booking_access_615267=true; booking_access_538469=true; booking_access_551084=true; booking_access_497454=true; booking_access_406456=true; NID_SES=AAABqz3cIUFxQdCshE/7z2m0AdUfrR9yQB8HCz30BWcmndOvdkB6WNvOUJwOSToLssS16ANxCOnkMTqmH+sN4P4/5wPUVgZYObEllgvNtzCPJOniFa0C4hi1SL15i2DVdl2QxhVG3AuqZvAdRFWJ7TvE9Rb7xJbXGYHKcNVoGaoaMXH0dDjSbGoYWTPmks2FmOZdGeI3n2tcBBcTld+w5Qdu4YmV4j13lRzc/Rg0m8ze4dIkaVB5lWWYrOBwBdxBPFaDdqTiBSPbT3XfOwWoqNDsoAAZhS6AI5EdCJGG5aZ6nldhQxL8f4QUa/hXNpKO2heJ2imNql/8tUEG049gTj73mmJUyLYWSpl4c4GM+zXoF2/cx2dOYLbWBNEG0qosl0donG1iDSMP35tSQll7Bp+q8gD6Gju6c5zDCGXpU9xM4iL6PNSV251gnLX6DQ+AER6VlJ09Sy6j+8J/ojln14ZnK+ygq/37bKXkkZGSEK6UZReCWtR3atzA8LWNIQ5NowRrfNnimz3v5Zjq+cKMijlnn6eOi0KYSViouILVo3HBv+ZTJ26Ma6pu8F+YGu7Bjiulaw==; csrf_token=e8a64ed09c3fefebaed9d95c17bfe72b0f8b338059d84c27c656e0486ddb8aa7cb0e1528662e30825d437edd492bcef87de3ae72f78dce3a5d0cf12a2a24fc78',
}

response = requests.get('https://api.booking.naver.com/v3.0/businesses/538469/biz-items/3963761/hourly-schedules?lang=ko&endDateTime=2022-04-05T00:00:00&startDateTime=2022-04-05T00:00:00', headers=headers,
                        # cookies=cookies
                        )

#//*[contains(@class,'none')]