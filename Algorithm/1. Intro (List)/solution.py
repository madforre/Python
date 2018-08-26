# 입력으로 주어지는 리스트 x 의 첫 원소와 마지막 원소의 합을 리턴하는 함수 solution()

# 내가 짠 코드
def solution(x):
    if len(x) > 0 : 
        answer = x[0] + x[len(x) - 1]
        return answer
    else :
        print('빈 리스트입니다.')