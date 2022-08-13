from selenium import webdriver

from urllib.request import *
from urllib.error import *

#xpath를 통한 오류구문 리스트 (xpath에 입력시에 발생하는 오류구문)
error_list1 = ['No results were found for the query', 'syntax error', '로 변환하지 못했습\
니다','변환하는 중 구문 오류가 발생했습니다.','따옴표가 짝이 맞지 않습니다.','You have \
an error in your SQL syntax','Unclosed quotation mark after the character string','Orac\
le Text error:']

text = input('에러페이지 확인 주소 입력(www.test.com) : ')
url = 'http://'+text

#xpath 모음
xpath_text = '//*[@id="query"]'
xpath_button = '//*[@id="frmSearch"]/table/tbody/tr[1]/td[2]/input[2]'

script = "'"

#크롬 브라우저 실행 -> url 열기
driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get(url)

#지정한 xpath에 값 넣고 실행하기
driver.find_element("xpath", xpath_text).send_keys(script)
driver.find_element("xpath", xpath_button).click()

html = driver.page_source #현재 페이지 html소스코드 가져오기

summ = 0

#html에 오류구문이 있는지 검사 
for i in error_list1:  
    if i in html:
        summ += 1

if summ != 0: #html에서 오류구문 발견
    print('에러페이지 정보노출 : 취약')

else: #html에서 오류구문 미발견
    error_list2 = ['Apache', 'nginx', 'IIS'] #url 직접 입력을 통한 오류구문 리스트
    url = url+'/errorpage_check'

    #크롬 브라우저 실행 -> url 열기
    driver = webdriver.Chrome("C:/chromedriver.exe")
    driver.get(url)
    
    try:
        res = urlopen(url) # url 열기
    except HTTPError as e: # HTTP 에러발생 -> 웹서버 정보 나오는지 검증
        summ = 0
        html = driver.page_source
        
        #html에 웹서버 정보가 나오는지 검사
        for j in error_list2:
            if j in html:
                print('에러페이지 정보노출 : 취약')
                break
            else:
                summ += 1
                if summ == int(len(error_list2)):
                    print('에러페이지 정보노출 : 양호')
