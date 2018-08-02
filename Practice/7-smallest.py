# 내가 짠 코드
# 숫자의 제한이 많다. sm보다 큰데 양수이면 비교할 수가 없음.
# 즉 sm과 비교하는 코드일 뿐이다.
sm = -1
print('Before', sm)
for the_num in [-3, -5, 12, 3, 74, 15] :
    if the_num < sm :
        sm = the_num
    print(sm, the_num)
print('After', sm)


print('---------')

# Finding the smallest value
# 숫자의 제한이 없다. 변수를 자료형 None으로 설정한 뒤
# 루프에서 리스트의 첫번째 인덱스에 해당하는 값을 None 이였던 변수에 넣어준다.

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 2] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)
