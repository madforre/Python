# 시급계산하기 : 오버타임 페이, 레귤러 페이 구하기
# 주 40시간 이상 넘어갈 시 오버타임 페이

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
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
