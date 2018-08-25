# 1부터 100까지 합을 구하시오.

value = input('1부터 입력하신 숫자까지의 합을 구합니다.')
try : value = float(value)
except : return print('숫자를 입력하세요.')

def hap(value):
    sum = value * (value + 1) / 2
    print(sum)

hap(value)

# 1부터 100까지의 합을 재귀로 구하시오.

n = input('1부터 입력하신 자연수까지의 합을 재귀로 구합니다.')
try : n = int(n)
except :
    print('숫자를 입력하세요.')
    quit()

def hap(n):
    if n%2 == 0: return n*(n+1)/2
    else: return hap(n-1) + n

print(hap(n))

# 팩토리얼을 재귀함수로 구현하시오.

n = input('입력하신 자연수의 팩토리얼을 재귀로 구합니다.')
try : n = int(n)
except :
    print('숫자를 입력하세요.')
    quit()

def factorial(n):
    if n==1: return 1
    else: return n * factorial(n-1)

print(factorial(n))
