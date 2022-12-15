# seungm2n06-7
# 파이썬 함수 및 람다(lamda)

'''
    1. 함수 정의
    def function_name(parameter):
        code

    2. 함수 호출
    function_name()
'''

# 함수 1
def hello(world):
    print("Hello, ", world)

hello("NiceYear")

# 함수 
def hello_return(world):
    value = "Hello, " + str(world)
    return value

str = hello_return("seungmin")
print(str)

print()
# 함수 3 다중리턴
def func_mul(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return y1, y2, y3

val1, val2, val3 = func_mul(3)
print(val1, val2, val3)

print()
# 튜플 리턴
def func_mul2(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return y1, y2, y3

tup = func_mul2(4)
print(type(tup), tup, list(tup))
