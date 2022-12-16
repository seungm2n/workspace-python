# seungm2n07-2
'''
    * Default parameter (기본 인자)
        - 함수의 파라미터에 기본값을 지정할 수 있다.
        - 파라미터를 명시하지 않을 경우, 지정된 기본값으로 대체해서 호출이 되어진다.
        - 디폴트 파라미터 뒤에 일반 파라미터가 위치할 수 없다.
            - e.g) def test(a,b,c = 1)
                   def test(a,b = 1, c = 2)
                   def test(a = 1, b = 1, c = 3)
                
                올바르지 않은 예)
                    def test(a, b = 1, c)
                    def test(a = 1, b, c)
                    def test(a = 1, b = 1, c)
'''
print("test")
# help(print)


def plus_ver2(number1, number2=100):
    print(number1 + number2)


plus_ver2(11)
plus_ver2(number1=0, number2=77)

print()

'''
    *args : 함수를 호출할 때 아규먼트의 갯수를 특정지을 수 없을 때 사용한다.
            불특정한 수의 숫자들은 'args'라는 튜플에 추가된다.
'''


def plus_unlimited(*args):
    print(type(args), args)
    sum(args)
    print(sum(args))


plus_unlimited(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)

print()
'''
    **kwargs : 함수를 호출할 때 키워드 아규먼트의 갯수를 특정지을 수 없을 때 사용한다.
               불특정한 수의 키워드 아규먼트들은 'kwargs'라는 딕셔너리에 추가된다.
'''


def plus_unlimited(*args, **kwargs):
    '''
    *args와 **kwargs라는 딕셔너리의 형태로 값을 받는 함수
    전체의 합의 결과를 출력합니다.
    '''
    print(type(kwargs), kwargs)
    sum(kwargs.values())         # 키워드 아규먼트의 합
    sum(args)                   # 아규먼트의 합
    print(sum(args)+sum(kwargs.values()))


plus_unlimited(1, 2, 3, 4, num1=100, num2=3000, num3=20, num4=7)

print()
'''
    list를 함수의 파라미터로 넣어 실행하는 경우
'''
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plus_unlimited(*list_numbers)

'''
    딕셔너리를 함수의 파라미터로 넣어 실행하는 경우
'''
dict_heights = {'ezen_height':178,'ezenyoung_height':180,'sugiezen_height':176,'ezensun_height':180}
plus_unlimited(**dict_heights)

'''
    Docstring : 함수의 설명을 작성해놓은 기술문서
                수많은 파이썬 함수의 사용법과 정보를 나타냄.
'''

help(plus_unlimited)
help(print)
help(input)
