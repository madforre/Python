# 조합의 수를 재귀적으로 계산하기
# 파스칼 삼각형 이용 nCm
# trivial case는 n==m 과 m==0

def combi(n,m):
    if n == m:
        return 1
    elif m == 0:
        return 1
    else:
        return combi(n-1, m) + combi(n-1, m-1)

# 위의 재귀함수는 효율성 측면에서는 좋지 않다.
# 사람이 생각하는 방식대로 옮길 수 있기 때문에 쓸모있는 경우도 많다.