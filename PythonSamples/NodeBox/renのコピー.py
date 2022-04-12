def ren(x,acc=1.0):
    d = int(x)
    acc *= (d+1)
    if x - d < 1e-12 or acc > 1e17:
        return [d]
    return [d] + ren(1.0/(x-d),acc)
    

x = 3.141592653589 #793238462643383
x = 9.75285784283699 / 3.396304435362434 #ratio for ice 5
R = ren(x)
print x,R
