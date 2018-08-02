# 실습 문제

# 사용자에게 반복해서 숫자를 물어보면서
# 입력한 값이 done이면 종료하고, 지금까지 입력했던 값들의 총합과
# 갯수, 그리고 입력했던 값들의 평균을 출력하고 싶다?
# 숫자가 아니거나 done이 아니면 에러를 출력해야한다.
# * 또한 try except를 이용하여 유효성 검사를 해야한다.

count = 0
sum = 0
while True :
    value = input('Enter a number: ')
    if value == 'done' :
        break;
    try :
        number = float(value)
    except :
        print(value,'는 잘못된 입력 값입니다')
        continue
    # 카운팅 + 덧셈
    count = count + 1
    sum = sum + number

# done으로 빠져나왔을 경우
if count == 0 :
    print('입력한 숫자가 없습니다.')
else :
    print('입력횟수:' + str(count) + ' 합계:'+ str(sum) + ' 평균:'+ str(sum/count))
