#for integer
def nshin(x,n):
    if x < 0:
        return "-" + nshin(-x,n)
    elif x < n:
        return str(x)
    return nshin(x / n, n) + "|" + str(x%n)


def frac(x,n,depth=0):
    if 17 <= depth < 17 or x == 0:
        return ""
    x *= n
    d = int(x)
    return str(d) + frac( x-d, n, depth + 1 )

def mshin(x,n):
    i = int(x)
    f = x - i
    if f < 0.0:
        f = -f    
    return nshin(i,n) + "." + frac(f,n)

    
print nshin(65535,16)
print mshin(1.5,16)

