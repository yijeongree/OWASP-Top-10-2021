from selenium import webdriver
from selenium.webdriver.common.alert import Alert

text = input('xss를 진단할 페이지를 입력하세요(www.test.com) : ')
url = 'http://'+text

#xpath 모음
xpath_text = '//*[@id="query"]'
xpath_button = '//*[@id="frmSearch"]/table/tbody/tr[1]/td[2]/input[2]'

script = "<script>alert('xss');</script>"

#크롬 브라우저 실행 -> url 열기
driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get(url)

#지정한 xpath에 값 넣고 실행하기
driver.find_element("xpath", xpath_text).send_keys(script)
driver.find_element("xpath", xpath_button).click()

#alert창이 뜨면 xss 취약점 확인
try:
    Alert(driver).accept()
    print('xss : 취약')
except:
    print('xss : 양호')    
