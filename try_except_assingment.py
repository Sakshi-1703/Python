num = input("enter days:")
rate =  input("enter rate per day:")
try:
    n = int(num)
    r = int(rate)
except:
    print("Error, please enter numeric input")
p = n*r
print('total pay = ',p)
