def E(T):
    return 6.11*10.0**(7.5*T/(T+237.3))*100.0

import math

def Pws(T):
    T += 273.15
    Pc=22120.0
    Tc=647.3
    x=1.0-T/Tc
    A=-7.76451
    B=1.45838
    C=-2.7758
    D=-1.23303
    return Pc*math.exp((A*x+B*x**1.5+C*x**3+D*x**6)/(1-x))*1000.0

print E(300.0),Pws(220.0)
