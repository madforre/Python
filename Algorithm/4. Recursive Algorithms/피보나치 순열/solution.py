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

# 인자 x는 피보나치 수열의 인덱스를 의미한다.

# Recursive version

def solution(x):
    if x == 0: return 0
    elif x == 1: return 1
    else:
        answer = solution(x-1) + solution(x-2)
    return answer

# Iterative version

def solution(x):
    # x가 0, 1 일 때.
    if x < 2: return x
    # x가 2이상
    else : 
        a = 0
        b = 1
        count = 0
        while count <= x: 
            old_a = a
            a = b
            b = old_a + b
            count += 1
        return old_a

# 나중에 시간이 되면 for 문으로도 해볼 것, 반복적 방법은 이해가 완벽하게 되진 않았음.