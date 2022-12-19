# seungm2n02 - 1
# 파이썬 기초 코딩
'''
  python -m venv 가상환경이름

    Scripts\activate.bat (활성화)                 가상환경 진입
      Scripts\deactivate.bat (비활성화)           가상환경 해제
  
  pip install simplejson
    show
    uninstall
    list
'''


# 파이썬 기본 입출력
'''
  1. print(값)
     print(값1, 값2, ...)
      - end 속성
      - sep 속성
      
'''

data = "Hello World!"
print(data)

print('Hello World')
print("Hello World")
print("""Hello World!""")
print('''Hello World!!''')

print()

data1 = 7
data2 = 6
data3 = 8
print(data1, data2, data3)
print(data1, data2, data3, sep=", ")
print(data1, data2, data3, end="[END]")

print()

print('2022', '12', '07', sep='-')
print('niceyear', 'gmail.com', sep='@')


# f-string을 사용하면 간단히 문자열을 출력할 수 있음
score = 80
print(f"학생의 점수는 {score}점 입니다.")


print("Test1: %5d, Price: %4.2f" % (776, 6534.123))


'''
  2. input()을 이용한 표준 입력
    1) input() : 키보드로부터 문자열을 입력 받음
    2) int() : 사용자로부터 입력받은 정보를 정수 형태로 처리하기 위함

'''

#data = input()
# print(data)

#name = input("당신의 이름은??")
#print("입력된 값 : ", name)
