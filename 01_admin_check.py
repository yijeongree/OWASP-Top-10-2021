from urllib.request import * # 웹페이지 요청 + 데이터 가져오기
from urllib.error import * # 존재하는 url인지 확인

list = ['admin','administrator',
        'master','manager','management',
        'system','test','anonymous']
text = input('도메인 주소를 입력하세요(www.test.com) : ')

i = 0

for k in list:
    url = 'http://'+text+'/'+k
    try:
        res = urlopen(url) # url 열기
    except HTTPError as e: # HTTP 에러발생 -> 출력하지않기
        continue
    except URLError as e: # URL 에러발생 -> 출력하지않기
        continue
    else: # 예외처리 사항 없음 -> 출력
        i=i+1
        print('\n[',i,'] ',url)

if i>=1:
    print('\n관리자 페이지 노출 : 취약\n')
else:
    print('\n관리자 페이지 노출 : 양호\n')