# 비만도 계산기를 만들어 보시오.

'''
예시)
        BMI 계산기 입니다.
        신장 : (입력)
        몸무게 : (입력)
        BMI :

'''
print("BMI 계산기 입니다.")
height = input("신장: ")
weight = input("몸무게: ")
height = int(height)
weight = int(weight)

BMI = weight / (height*height) * 10000
print("BMI: ", BMI)