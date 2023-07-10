def pay(n,r):
    p = n*r
    return p
num = input("enter days:")
rate =  input("enter rate per day:")
n = int(num)
r = int(rate)
print('total pay = ',pay(n,r))
