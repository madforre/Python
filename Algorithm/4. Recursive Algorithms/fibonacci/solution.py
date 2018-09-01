# 문제

# 인자로 0 또는 양의 정수인 x 가 주어질 때, 
# Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 완성할 것.

# Fibonacci 순열은 아래와 같이 정의됩니다.
# F0 = 0
# F1 = 1
# Fn = Fn - 1 + Fn - 2, n >= 2

# 재귀함수 작성 연습을 의도한 것이므로, 재귀적 방법으로도 프로그래밍해 보고, 
# 반복적 방법으로도 프로그래밍해 보시기 바랍니다.

# 풀이

# 인자 n는 피보나치 수열의 인덱스를 의미한다.

import time # time 모듈 임포트

# Recursive version

def rec(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        answer = rec(n-1) + rec(n-2)
    return answer

# Iterative version

def iter(n):
    # n가 0, 1 일 때.
    if n <= 1: return n
    # n가 2이상
    else : 
        i = 2
        t0 = 0
        t1 = 1
        while i <= n: 
            # t0 = t1 할당하고 t1 = t0+t1 할당. 동시 선언.
            t0, t1 = t1, t0 + t1 
            i += 1
        return t1

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    
    ts = time.time()
    fibo = iter(nbr)
    ts = time.time() - ts
    print("Iterative version: %d (%.3f)" % (fibo, ts))
    ts = time.time()
    fibo = rec(nbr)
    ts = time.time() - ts
    print("Recursive version: %d (%.3f)" % (fibo, ts))

# 재귀적으로 함수를 구현했을 때에는 성능상의 불리함이 있다!