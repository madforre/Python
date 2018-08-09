# XML 데이터를 파이썬에 읽어오기 위해 xml 모듈 사용

import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

# XML의 구조를 이해하고 있으면(트리구조) 다음과 같이 반복문을 활용해 XML의 데이터에 접근할
# 수도 있다.

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))

#User count: 2
#Name Chuck
#Id 001
#Attribute 2
#Name Brent
#Id 009
#Attribute 7
