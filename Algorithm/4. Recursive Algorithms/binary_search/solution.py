# L은 리스트 x는 타겟인 정수
# l은 lower index u 는 upper index

def solution(L, x, l, u):
    if l > u: 
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid-1)
    else:
        return solution(L, x, mid+1, u)

