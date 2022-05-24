# coding: utf-8
import datetime

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time
from apscheduler.schedulers.blocking import BlockingScheduler

# 스케줄러를 활용하기위한 라이브러리
sched = BlockingScheduler()

# 프로그램 사용자의 크롬 버전에 맞게 다운로드 할 수 있도록 처리하는 라이브러리
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  # 크롬드라이버 버전 확인
path = chromedriver_autoinstaller.install(True)

# 결과폴더를 생성하기위한 datetime 설정
file_datetime = datetime.datetime.now().strftime('%y%m%d_%H%M')

# selenium에서 해당 element가 표현될 떄까지 대기하는 함수
def explicitly_wait(driver, by, name):
    try:
        return WebDriverWait(driver, WAITTIME).until(EC.presence_of_element_located((by, name)))
    except Exception as e:
        raise ValueError(by, name)


# selenium 사용을 위한 설정값
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

WAITTIME = 30
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--lang=en-US")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('user-agent={0}'.format(user_agent))

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
s = Service(path)

# selenium 사용하기 위한 driver 설정
def driver_setting():
    driver = webdriver.Chrome(service=s, options=options,
                              desired_capabilities=caps)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver


# decorator로 스케줄을 관리
# 해당 args에서 minute를 바꿔주면 매 시각 x분마다 동작
# 스케줄러 사용법은 https://hello-bryan.tistory.com/216 해당 링크에 잘 설명이 되어있습니다.
@sched.scheduled_job('cron', minute=0, id='job_1') # 매 시각 0분마다 실행
# @sched.scheduled_job('cron', minute=30, id='job_1') # 매 시각 30분마다 실행
# @sched.scheduled_job('cron', minute=5, id='job_1') # 매 시각 5분마다 실행
# @sched.scheduled_job('interval', minutes=5, id='job_1') # 5분마다 프로그램 실행
def get_data():
    driver = driver_setting()
    driver.get("https://nylottery.ny.gov/")
    print(f"수집시각 : {datetime.datetime.now().replace(microsecond=0)}")
    for x in ["MegaMillionHighJackpot", "PowerballHighJackpot"]:
        explicitly_wait(driver, By.XPATH, f"//p[contains(@class,'{x}')][contains(text(),'Next')]")
        line_one = [x.text for x in driver.find_elements(By.XPATH,
                                                         f"//div[contains(@class,'{x}')][contains(@class,'oval__Oval-sc-1i1etol-0')]")
                    if x.text]
        print(x)
        print(driver.find_element(By.XPATH, f"//p[contains(@class,'{x}')][contains(text(),'Next')]").text)
        print(driver.find_element(By.XPATH, f"//p[contains(@class,'{x}')][contains(text(),'Winning')]").text)
        print(line_one)
        print('\n')

    for x in ["QuickDrawJackpot", "Pick10Jackpot"]:
        line_one_ = []
        line_two_ = []

        all = [x.text for x in driver.find_elements(By.XPATH,
                                                    f"//div[contains(@class,'{x}')]//div[contains(@class,'Pick10Styles__Oval-reh4im-2')]")]
        line_one = all[:10]
        line_two = all[10:20]

        try:
            line_one_ = all[20]
            line_two_ = all[21]
            line_one.append(line_one_) if line_one_ else line_one.append('')
            line_two.append(line_two_) if line_two_ else line_two.append('')
        except:
            pass
        print(x)
        print(
            driver.find_element(By.XPATH, f"//div[contains(@class,'{x}')]//div[contains(text(),'Next')]").text.replace(
                '\n', ' '))
        print(driver.find_element(By.XPATH,
                                  f"//div[contains(@class,'QuickDrawJackpot')]//*[contains(text(),'Winning')]").text.split(
            '\nDRAW')[0].replace('\n', ' '))
        print(line_one)
        print(line_two)
        print('\n')

    driver.quit()


if __name__ == '__main__':
    # 시각마다 돌기 전 처음 실행
    get_data()

    # 스케줄러 실행
    sched.start()
    while True:
        # 0.5초마다 체크하면서 스케줄러를 실행ㅜ
        time.sleep(.5)
