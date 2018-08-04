# 문제 : From으로 시작하는 줄을 찾아 세번째 단어를 추출해라.
# 원소가 없는 빈 Array 때문에 문제가 생길 수 있다!

fh = open('mbox-short.txt')

for line in fh:
    line = line.rstrip()
    wds = line.split()
    # guardian in a compound statement
    # 공백이면서 최소 3단어 이상이어야 한다. + 문장 앞글자가 From으로 시작해야 한다.
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])

    # or는 둘 다 참이거나 하나만 참이어도 참이다.
    # 코드를 왼쪽부터 순서대로 읽으므로 길이 조건을 먼저 걸려야 한다.
    # 아래처럼 첫글자가 From 이지만 3글자 미만인 경우도
    # print(wds[2])에서 실행되므로 트랙백 에러가 날 것이다.
    # 따라서 길이 조건으로 먼저 걸러 주어야 한다.
    # 길이 3글자 미만이 더 큰 영역이므로. 먼저 걸러주어야 한다.
    # 순서를 맞춰야 한다!

    # if  wds[0] != 'From' or len(wds) < 3 :
    #     continue
    # print(wds[2])

    # 가디언 패턴이 먼저오고 그 뒤에 or가 와야 한다.
    # 최단 평가(Short circuit evaluation)
