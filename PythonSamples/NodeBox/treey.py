from math import *
def branch(x,y,L,a,depth):
    strokewidth(depth)
    s = 8.0 - depth
    if s < 0.0:
        s = 0.0
    s *= 0.125
    stroke(0)
    if 1.0 < depth:
        ex = x + L * cos(radians(a))
        ey = y + L * sin(radians(a))
        line(x,y,ex,ey)
        ex1 = x + 0.5* L * cos(radians(a))
        ey1 = y + 0.5* L * sin(radians(a))
        branch(ex1,ey1,L*0.8, a - 24.0, depth - 1.0)
        branch(ex,ey,L*0.8, a,  depth - 1.0)
        branch(ex,ey,L*0.8, a + 24.0, depth - 1.0)
    else:
        ex = x + depth * L * cos(radians(a))
        ey = y + depth * L * sin(radians(a))
        line(x,y,ex,ey)
        nostroke()

def branch2(x,y,L,a,depth):
    strokewidth(depth)
    s = 8.0 - depth
    if s < 0.0:
        s = 0.0
    s *= 0.125
    stroke(0)
    if 1.0 < depth:
        ex = x + L * cos(radians(a))
        ey = y + L * sin(radians(a))
        line(x,y,ex,ey)
        ex1 = x + 0.5* L * cos(radians(a))
        ey1 = y + 0.5* L * sin(radians(a))
        branch2(ex,ey,L*0.8, a - 24.0, depth - 1.0)
        branch2(ex,ey,L*0.8, a,  depth - 1.0)
        branch2(ex,ey,L*0.8, a + 24.0, depth - 1.0)
    else:
        ex = x + depth * L * cos(radians(a))
        ey = y + depth * L * sin(radians(a))
        line(x,y,ex,ey)
        nostroke()


size(200,100)
colormode(HSB)
branch2(50.0, 100.0, 40.0, 270.0, 2.0)
branch(150.0, 100.0, 40.0, 270.0, 2.0)