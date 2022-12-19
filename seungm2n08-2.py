'''
    * 웹 크롤링
        - 날짜 추출
            - td 태그 중에 원하는 정보만을 따로 가져와야함
            - 날짜 태그 규칙 찾아서 td 태그들 중에 날짜를 가져옴
            

'''
import bs4
import requests
page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"
print(page_url)

source = requests.get(page_url).text

source = bs4.BeautifulSoup(source)

dates = source.find_all('td', class_='date')
#print(dates)
#print(dates[0])
#print(dates[0].text)

date_list = []

# 날짜 크롤링
for date in dates:
    date_list.append(date.text)

print(date_list)

# 체결가 추출
prices = source.find_all('td', class_='number_1')
'''
    체결가 변동량(천주) 거래량(천주) 거래대금(백만) 들도 같은 태그(number_1)를 공유하고 있다.
    4개씩 증가하는 것을 알 수 있다.
    4의 배수로 건너뛰면서 추출하면 바로 체결가만 가져올 수 있다.
'''
# print(prices[::4])

price_list = []

for price in prices[::4]:
    price_list.append(price.text)

print(price_list)

print(len(date_list))
print(len(price_list))

