# Opening and Reading a File
fname = input('Enter your file name :')
try :
    fhand = open(fname)
except :
    print('불러오려는 파일명이 잘못되었습니다.')
    quit()
for cheese in fhand :
    if 'Author:' in cheese :
        cheese = cheese.rstrip().upper() # 오른쪽 끝 개행문자 제거 + 대문자로 바꾸기
        print(cheese)

# File Handle?
# 텍스트 파일을 읽는 하나의 표준화된 형태
# 순차적으로 텍스트 파일을 읽는다.
