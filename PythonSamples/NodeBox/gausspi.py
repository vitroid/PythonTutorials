import math


def set(x):
    return x*10**1000
def mul(a,b):
    return a*b / 10**1000
def div(a,b):
    return a*10**1000 / b
def atan(x):
    xx = mul(x,x)
    sum = 0
    i = 1
    while 0 != x:
        sum += x / i
        x = -mul(x,xx)
        i += 2
    return sum

x = div(set(1),set(18))
print 4*(12*atan(div(set(1),set(18))) 
         +8*atan(div(set(1),set(57)))
         -5*atan(div(set(1),set(239))))

