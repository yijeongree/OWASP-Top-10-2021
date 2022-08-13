from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from selenium import webdriver

text = input('주소를 입력하세요(www.test.com) : ')
url = 'https://'+text

#https 프로토콜을 사용하는지 확인
try:
    res = urlopen(url)
except HTTPError as e: #HTTP 상태코드 에러
    print('취약한 웹 프로토콜 사용')
except URLError as e: #URL 에러 (ex : err_timed_out)
    print('취약한 웹 프로토콜 사용')

#http로 접속 시 https로 자동 리다이렉트 되는지 확인
else:
    url = 'http://'+text
    driver = webdriver.Chrome("C:/chromedriver.exe")
    driver.get(url)

    variable = driver.current_url

    if variable.lower().startswith('https'):
        print('안전한 웹 프로토콜 사용')
    else :
        print('취약한 웹 프로토콜 사용')
