from nodebox_wrapper import *
from math import *
def branch(x,y,L,a,depth):
    strokewidth(depth*5)
    s = 8.0 - depth
    if s < 0.0:
        s = 0.0
    s *= 0.125
    stroke(0.333, s,1.3-s)
    if 1.0 < depth:
        ex = x + L * cos(radians(a))
        ey = y + L * sin(radians(a))
        line(x,y,ex,ey)
        branch(ex,ey,L*0.8, a-random()*12.0 - 18.0, depth - 1.0)
        branch(ex,ey,L*0.6, a+random()*12.0 - 6.0,  depth - 1.0)
        branch(ex,ey,L*0.8, a+random()*12.0 + 18.0, depth - 1.0)
    else:
        ex = x + depth * L * cos(radians(a))
        ey = y + depth * L * sin(radians(a))
        line(x,y,ex,ey)
        nostroke()
        fill(random()*0.1+0.333,s,s/2)
        oval(ex-4,ey-4,8,8)

size(200,200)
colormode(HSB)
branch(100.0, 200.0, 40.0, 270.0, 6.0)
#added
wait_q()
