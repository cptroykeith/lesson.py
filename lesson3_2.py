sh = input ("enter hours: ")
sr = input ("enter rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

print(fh, fr)
if fh > 40 :
    #print("overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    #print(reg,otp)
    pay = reg + otp
else:
    #print("regular")
    pay = fh * fr
print("pay:",pay)