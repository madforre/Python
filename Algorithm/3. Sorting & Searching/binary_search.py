# 문제 

# 리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어질 때, 
# x 와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요. 
# 만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다. 
# 리스트 L 은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정합니다. 
# 또한, 동일한 원소는 두 번 이상 나타나지 않습니다.

# 예를 들어,
# L = [2, 3, 5, 6, 9, 11, 15]
# x = 6
# 의 인자들이 주어지면, L[3] == 6 이므로 3 을 리턴해야 합니다.

# 또 다른 예로,
# L = [2, 5, 7, 9, 11]
# x = 4
# 로 주어지면, 리스트 L 내에 4 의 원소가 존재하지 않으므로 -1 을 리턴해야 합니다.

# 이 연습문제에서는 알고리즘의 효율성도 평가합니다. 
# 만약 순차 (선형) 탐색 알고리즘을 구현하는 경우에는 제한 시간 요구사항을 만족하지 못하여 
# 효율성 테스트 케이스들을 통과하지 못할 수도 있습니다.

# 내 풀이

def solution(L, x):
    # 초기 lower, upper 인덱스 설정
    lower = 0
    upper = len(L) - 1
    answer = -1
    while lower <= upper:
        # middle은 리스트의 가운데 인덱스를 의미. (리스트 길이가 홀수일 경우 2로 나눈뒤 버림)
        middle = ( lower + upper ) // 2
        if L[middle] == x:
            answer = middle
            return answer
        if L[middle] > x: 
            upper = middle - 1
        elif L[middle] < x: 
            lower = middle + 1
    return answer

# 코드 이해를 위한 복습 및 간단 설명
# 리스트에서 3 5 만 남은 경우

# lower 가 3 upper가 5 인 경우 5 찾으려면
# 인덱스 middle은 0 이 된다.
# x가 인덱스 미들의 값인 3보다 크므로
# 인덱스 middle 에서 + 1 더 해준 인덱스가 새로운 lower가 된다.
# lower 5 upper 5 인 경우.
# lower와 upper가 같은데도 x가 크다면
# 리스트 안에 x가 없는 것이므로 while문을 종료해야 한다.
# 일단 로직대로 lower에 1을 더해준다.
# 그리고 while문 루프를 돌고 조건을 만났을 때 lower가 upper보다 커지므로 종료된다.

# lower가 3 upper가 5인 경우 3 찾으려면
# 인덱스 middle은 0 되는데
# x가 곧 인덱스 미들의 값인 3이므로
# 바로 리턴한다.

# 리스트에서 3 4 5 남은 경우

# lower 가 3 upper 가 5 인데 3찾으려면
# 인덱스 middle은 4가 된다.
# 찾으려는 x가 인덱스 middle 값보다 작으므로
# 인덱스 미들 -1 을 upper로 설정한다.
# 즉 3이 upper가 되어
# lower 3 upper 3 이 된다.
# lower와 upper가 조건이 같으므로 3을 리턴한다.