# re 라이브러리를 사용하여 파일을 불러와서 정규표현식 라이브러리의
# 메소드인 findall와 내장 메소드인 max를 사용하여
# 추출한 패턴의 최댓값을 찾아주자.
# 패턴은 X-DSPAM-Confidence: 가 앞에 있는 .을 포함하는 숫자여야 한다.

# 코드
import re
fname = input('txt 파일명을 입력해주세요. (입력 안하면 mbox-short.txt) :')
if len(fname) < 1 : fname = 'mbox-short.txt'
fh = open(fname)
list = list()
for line in fh:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([\d.]+)' , line)
    if len(stuff) != 1 : continue
    list.append(stuff[0])
print(max(list))

# 정규표현식에서는 ()로 추출할 부분을 지정할 수 있다! 이것을 기억하자.
