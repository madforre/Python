# 문제
# 딕셔너리의 히스토그램을 값을 기준으로 Top 10를 내림차순 정렬하고 싶다?

# 내가 짠 코드
fname = input('파일이름을 입력해주세요. (입력을 안하실 경우 clone.txt로 자동 세팅됩니다.) : ')
if len(fname) < 1 : fname = 'clone.txt'
try : fh = open(fname)
except :
    print('입력하신 파일이 없거나 텍스트 파일 형식이 아닙니다.')
    quit()

di = dict()
for line in fh :
    # print(line)
    words = line.rstrip().split()
    # print(words)
    for word in words :
        di[word] = di.get(word, 0) + 1

# print(di)
x = sorted([(value, key) for (key, value) in di.items()],reverse=True)[:10]
print('------------------')
print('반복된 문자 Top 10')
print('------------------')
for (v,k) in x:
    print(k+' :',v,'번')

# 리스트와 딕셔너리, 튜플을 이용하여 히스토그램을 값을 기준으로 내림차순 정렬하였다.
