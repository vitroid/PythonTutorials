#!/usr/bin/env python
from math import *
size(8180,4090)
nofill()
stroke(0)
first=1
for i in range(0,1000+1):
    a = 0.001*i*pi*2.0
    b = 0.001*i
    z = 1.5*(-cos(2.0*a)+0.1*cos(6.0*a)-0.01*cos(10.0*a))
    z = -2.0*cos(2.0*a)
    #y = (int((i+12.5)/25) % 2) * 2 - 1.0 
    x = sin(a)
    y = -cos(a)
    r = 1.0/sqrt(x**2+y**2+z**2)
    x*=r
    y*=r
    z*=r
    #print "t",x,y,z,i
    ph = WIDTH*(b+0.06*sin(a*4.0))
    th = HEIGHT*0.5+HEIGHT*0.3*cos(a*2.0)
    if first==1:
        beginpath(ph,th)
        first=0
    else:
        lineto(ph,th)
endpath()

    