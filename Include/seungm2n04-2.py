# seungm2n04-2
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트 자료형 (순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Powerful', 'Health', 'Features']
e = [10, 100, ['Powerful', 'Health', 'Features']]

# 인덱싱
print()
print('d : ', type(d), d)
print('d : ', d[1])
print('d : ', d[0] + d[1] + d[1])
print('d : ', d[-1])
print('d : ', d[-2])
print('e : ', e[-1][1])
print('e : ', e[-1][1][4])

# 슬라이싱
print()
print('d : ', d[0:3])
print('d : ', d[2:])
print('e : ', e[2][1:3])

# 연산
print()
print('c + d : ', c + d)
print('c * 3 : ', c * 3)

#수정, 삭제
print()
c[0] = 4
print('c : ', c)
