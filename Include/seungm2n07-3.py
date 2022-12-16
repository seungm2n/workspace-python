# seungm2n07-3
'''
    리스트 내 원소 중에서 가장 큰 값의 인덱스(위치)를 찾아서 반환하는 함수를 작성하시오.

    data = [7, 1, 5, 9, 3, 2, 4]
'''


def find_index_largest(data):
    largest_index = 0
    for i in range(len(data)):
        # 더 큰 값은 경우
        if data[largest_index] < data[i]:
            largest_index = i
    return largest_index


data = [71, 1, 15, 9, 3, 2, 4]
largest_index = find_index_largest(data)
print(largest_index)

'''
    특정한 값을 가지는 원소의 인덱스를 찾는 함수를 작성해 보시오.
    [3, 5, 7, 9]
    찾는 원소가 없을 경우 => -1
    찾는 원소가 있는 경우 => index 값 리턴

    enumereate()
'''


def find_specific_value(lis, value):
    for i, x in enumerate(lis):
        if x == value:
            return i
    return -1   # 찾지 못한 경우


print(find_specific_value([3, 5, 7, 9], 7))
print(find_specific_value([3, 5, 7, 9], 2))

'''
    하나의 자연수가 주어졌을 때, 소수인지 아닌 지 판별하는 함수를 작성하시오.
    - 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수다.
'''


def determine_prime(x):
    # 1 이하인 경우 소수가 아님.
    if x <= 1:
        return False
    # 1 과 자기 자신 외의 자연수로 나누어지면 소수가 아님.
    for divisor in range(2, x):
        if x % divisor == 0:
            return False
    return True


print(determine_prime(1))
print(determine_prime(2))
print(determine_prime(3))
print(determine_prime(47))
print(determine_prime(74))
