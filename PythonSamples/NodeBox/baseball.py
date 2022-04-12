#!/usr/bin/env python
from math import *
size(8180,4090)
fill(0)
first=1
for i in range(0,10000):
    a = 0.0001*i*pi*2.0

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
    if x!=0.0:
        ph = atan(y/x)
        if x<0:
            ph += pi
        th = atan(z/sqrt(x**2+y**2))
        #print "t",ph*10,0,th*10,i
        ph = (ph + pi/2)*4090/pi
        th = (th + pi/2)*4090/pi
        #th = y*90.0+90
        #ph = i*360.0/100.0
        #print ph,th,y
        if first==1:
            beginpath(ph,th)
            first=0
        else:
            lineto(ph,th)
endpath()

    