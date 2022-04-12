from nodebox_wrapper import *
import math
import cmath

size(1000,1000)
zoom=100.0
k=1.76664

def circle(x,y,r):
    oval(x-r,y-r,r*2,r*2)

def sm(u):
    return u -u**4/6 +2*u**7/63 -13*u**10/2268 +23*u**13/22113

def cm(u):
    return 1 -u**3/3 +u**6/18 -23*u**9/2268 +25*u**12/13608

#projection from triangle to sphere
def projection(w):
    lhs = 2.0 *sm(w/2.0) * cm(w/2.0)
    arc = abs(lhs)
    sigma = 2.0*math.atan(arc/2.0**(5.0/6.0))
    azimuth = lhs/arc
    return (azimuth,sigma)

def recursew(w,c):
    const = [0.625, -0.223214, 0.069754, -0.020121, 0.005539,
             -0.001477, 0.000385, -0.000099, 0.000025]
    w3 = w*w*w * 0.1
    www = w
    sum =  1.791797*c
    for i in const:
        www *= w3
        sum += i*www
    return sum

def reverseproj(sigma,alpha):
    global lastw
    c = math.tan(sigma/2.0) * cmath.exp(1.0j * alpha)
    w = lastw
    lastw = c
    count=0
    while abs(lastw-w) > 1e-3:
        lastw = w
        w=recursew(lastw,c)
        print count,w
        colormode(HSB)
        h = (count%100)*0.01
        fill(h,1,1)
        circle(zoom*(w.real+0.5),4.0+zoom*(w.imag-1.5),2.0)
        count += 1
    print c,w,count
    return w


def projdraw():
    for theta in range(0,360,2):
        for ir in range(-9,200,10):
            r = ir * 0.01
            th = math.radians(theta)
            w = r * cmath.exp(1.0j * th)
            (azimuth,sigma) = projection(w)
            colormode(HSB)
            fill(r/2,theta/360.0,1) 
            #oval(100.0+r*cos(th),100.0+r*sin(th))
            #circle(200.0+azimuth.real*sigma*zoom,500.0+azimuth.imag*sigma*zoom,1)
            y = math.degrees(sigma)
            angle = math.atan(azimuth.imag/azimuth.real)
            if azimuth.real<0:
                angle = math.pi + angle
            while angle < 0.0:
                angle += math.pi * 2
            x = math.degrees(abs(angle))
            #if y > 90:
            #    y=180-y
            #    x=360-x   
            circle(x,
                   y+300,1)
            if y < 72:
                circle(200.0+zoom*w.real,100.0+zoom*w.imag,2)
def revdraw():
    global lastw
    lastw = -0.430131513757+1.64373254113j
    for alpha in range(117,118,1):
        for sigma in range(74,76,):
            print alpha,sigma
            w = reverseproj(math.radians(sigma),math.radians(alpha))
            fill(0,0,0)
            circle(200.0+zoom*w.real,100.0+zoom*w.imag,2)
            #oval(100.0+r*cos(th),100.0+r*sin(th))
            fill(1,0,0)
            circle(alpha, sigma+300.0, 1)

projdraw()
stroke(0)
nofill()
rect(0,300,360,180)

print sm(0.0),cm(0.0),sm(0.5*k),cm(0.5*k),2**(-1.0/3.0)
print sm(k),cm(k)
#added
wait_q()
