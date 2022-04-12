from math import floor,sqrt
phi = (1+sqrt(5))*0.5

def fibo(n):
    return 2+floor((n+1)*phi)-floor((n+2)*phi)


s = ""
for i in range(100):
    if fibo(i)==0.0:
        s+="A"
    else:
        s+="B"
print s

