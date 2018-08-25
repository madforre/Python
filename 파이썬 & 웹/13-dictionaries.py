# 입력 안할시 기본 파일은 clone.txt / 테스트용으로는 intro.txt를 사용하자.
fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clone.txt'
handle = open(fname)

# 딕셔너리 생성
dict = {} # 또는 dict = dict()

# 파일 핸들을 통해 각 라인을 split, rstrip 처리, 리스트 생성
for line in handle:
    list = line.rstrip().split()
    for hou in list:
        # get() 메서드 이용
        dict[hou] = dict.get(hou, 0)+1
        # 메서드 이용 안할 시
        # if hou not in dict:
        #     dict[hou] = 1
        # else:
        #     dict[hou]= dict[hou]+1
        test = 'hou'

# 딕셔너리를 다시 리스트로, 가장 많은 문자 구하기
biggest = 0
for key,value in dict.items():
    # print(key, value)
    if biggest < value :
        biggest = value
        name = key
print('파일에서 가장 많이 반복된 문자는', name+'입니다.', '횟수는',biggest)
