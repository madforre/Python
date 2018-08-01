sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

# 정상 검사 여부. 다룰 수 없는 입력 값이면 except로 처리
try :
    fh = float(sh)
    fr = float(sr)
except :
    print("숫자를 입력해주세요. Please enter numeric input.")
    quit() # 더 이상 실행하지 않고 멈춘다.

# print(fh,fr)
if fh > 40 :
    # print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    # print(reg,otp)
    xp = reg + otp
else :
    # print("Regular")
    xp = float(fh) * float(fr)
    print("Pay:",xp)
