from selenium import webdriver #크롤링을 위한 모듈
from bs4 import BeautifulSoup

text = 'https://cve.mitre.org/cve/search_cve_list.html'

#xpath 모음
xpath_search = '//*[@id="CenterPane"]/form/div[1]/input'
xpath_button = '//*[@id="CenterPane"]/form/div[2]/input'

search = input('점검할 서비스 입력 ( ex : ubuntu 20.04 ) : ')

#크롬 브라우저 실행 -> url 열기
driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get(text)

#지정한 xpath에 값 넣고 실행하기
driver.find_element("xpath", xpath_search).send_keys(search)
driver.find_element("xpath", xpath_button).click()

variable = driver.current_url #현재 페이지 출력 (로그인 성공 여부 확인 가능)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
td_tag = soup.find_all('td') #td태그 다 가져오기

count = 0
for i in td_tag:
    count+=1

if int(count)>=21:
    print('버전 업데이트 또는 변경이 필요합니다.')
else:
    print('안전합니다')