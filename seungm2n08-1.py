'''
    * 웹 크롤링
        - 웹 페이지에 있는 데이털들 요청하여 가져오는 방법 활용
        - request, bs4 라이브러리 활용
            - beautifulsoup4(bs4)
                - HTML source에서 tag별 계층 구조를 파악하기 쉽게 parse해서 tree 형태로 변환해주는 라이브러리다.
                - 손쉽게 HTML source에서 원하는 정보를 추출할 수 있다.
                    - find, find_all() 함수를 이용하면 원하는 tag와 속성에 맞는 모든 정보를 가져올 수 있다.

        - 해당 페이지의 page source를 직접 가져옴
        - 웹 페이지 우클릭 "페이지(프레임) 소스보기"로 같은 HTML 소스를 볼 수 있음
        - 마우스 우클릭을 하면 "검사" 기능 활용
'''

page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"
print(page_url)

import requests
source = requests.get(page_url).text
#print(source)

#beautifulsoup4(bs4)를 불러옴
import bs4
source = bs4.BeautifulSoup(source)
print(source)
