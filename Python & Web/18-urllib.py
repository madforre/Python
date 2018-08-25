# urllib 라이브러리를 사용하여 웹크롤링 하였다.
import urllib.request, urllib.parse, urllib.error, re

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
list = list()
for line in fhand:
  line = line.decode().strip()
  stuff = re.findall('<a href="(https?://.+)">' , line)
  if len(stuff) < 1:
    continue
  list.append(stuff[0])
print(list)
