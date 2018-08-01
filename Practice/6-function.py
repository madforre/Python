hours = input('Enter the hours :')
rate = input('Enter the rate :')

def pay(hours, rate):
    fh = float(hours)
    fr = float(rate)
    # print(fh,fr)
    if fh > 40 :
        # print("Overtime")
        reg = fr * fh
        otp = (fh - 40.0) * (fr * 0.5)
        # print(reg,otp)
        pay = reg + otp
    else :
        # print("Regular")
        pay = float(fh) * float(fr)
    return pay

print('your pay is $', pay(hours, rate))
