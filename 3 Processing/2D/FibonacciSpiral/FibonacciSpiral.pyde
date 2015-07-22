from math import *

phi = (1+sqrt(5))/2
theta = 2*pi / phi

def setup():
    size(1000,1000)
    frameRate(100)

def draw():
    #strokewidth(1)
    noFill()
    stroke(0)
    i = frameCount
    r = 10*sqrt(i)
    x = r * cos(theta*i)
    y = r * sin(theta*i)
    ellipse(x-2+500,y-2+500,10,10)

