# coding: utf-8
import datetime
import os
import time
import warnings

import chromedriver_autoinstaller
import numpy as np
import pandas as pd
import pymysql
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
from urllib.request import urlretrieve

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
chromedriver_autoinstaller.install(True)
warnings.simplefilter("ignore", category=pymysql.Warning)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'

WAITTIME = 5

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument('--incognito')
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-setuid-sandbox")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('user-agent={0}'.format(user_agent))

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}


driver = webdriver.Chrome(executable_path=f'./{chrome_ver}/chromedriver.exe', chrome_options=options,
                              desired_capabilities=caps)

imgs = []
names = []
prices = []
deliveries = []
page =1
refresh_cnt = 5
while True:

    print(page)
    driver.get(f"http://minishop.gmarket.co.kr/dalkkong/List?Title=Best%20Item&CategoryType=General&SortType=MostPopular&DisplayType=SmallImage&Page={page}&PageSize=60&IsFreeShipping=False&HasDiscount=False&HasStamp=False&HasMileage=False&IsInternationalShipping=False&IsTpl=False&MinPrice=14940&MaxPrice=1249690&Roles=System.String%5B%5D")


    elem = driver.find_element(By.TAG_NAME,"body")
    # cnt = 6
    # while cnt:
    #     elem.send_keys(Keys.PAGE_DOWN)
    #     time.sleep(.5)
    #     cnt -=1
    # cnt = 6
    # time.sleep(1)
    if len(driver.find_elements(By.XPATH, '//*[@id="ItemList"]/div[3]/ul/li/p/a/img')) == 0:
        break
    imgresult = ['http:'+x.get_attribute('data-original').split('/280')[0]+'/300' for x in driver.find_elements(By.XPATH, '//*[@id="ItemList"]/div[3]/ul/li/p/a/img')]
    # if 'http://image.gmarket.co.kr/challenge/neo_image/no_image.gif/300' in imgresult:
    #     elem.send_keys(Keys.HOME)
    #     if refresh_cnt > 0:
    #         refresh_cnt -=1
    #         continue
    #     else:
    #         refresh_cnt = 5
    #         pass
    [imgs.append(img) for img in imgresult]
    [names.append(y) for y in [x.get_attribute('alt') for x in
                               driver.find_elements(By.XPATH, '//*[@id="ItemList"]/div[3]/ul/li/p/a/img')]]
    [prices.append(y) for y in [x.text.replace('원', '').replace(',', '') for x in
                                driver.find_elements(By.XPATH, '//*[@id="ItemList"]/div[3]/ul/li/div/p[2]/em/strong')]]
    [deliveries.append(y) for y in
     [x.get_attribute('alt') for x in driver.find_elements(By.XPATH, '//*[@id="ItemList"]/div[3]/ul/li/div/p[3]/img')]]
    page += 1


for idx,img in enumerate(imgs):
    try:
        urlretrieve(img, f'.\\pictures\\{idx+1}.jpg')
    except:
        print(f'no image : {idx+1}')
print(imgs)
# try:
#     urlretrieve(src_link, f'.\\pictures\\{filename}')
# except:
#     pass
