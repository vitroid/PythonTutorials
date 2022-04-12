from math import *
def branch(x,y,L,a,depth,snow):
    strokewidth(depth)
    s = 8.0 - depth
    if s < 0.0:
        s = 0.0
    s *= 0.125
    stroke(0.333, s,s)
    if 1.0 < depth:
        ex = x + L * cos(radians(a))
        ey = y + L * sin(radians(a))
        line(x,y,ex,ey)
        ex1 = x + 0.5* L * cos(radians(a))
        ey1 = y + 0.5* L * sin(radians(a))
        branch(ex1,ey1,L*0.5, a-random()*12.0 - 24.0, depth - 1.0,snow)
        branch(ex,ey,L*0.8, a+random()*12.0 - 6.0,  depth - 1.0,snow)
        branch(ex,ey,L*0.4, a+random()*12.0 + 24.0, depth - 1.0,snow)
    else:
        ex = x + depth * L * cos(radians(a))
        ey = y + depth * L * sin(radians(a))
        line(x,y,ex,ey)
        if snow:
            nostroke()
            fill(random()*0.3+0.2,0.0,s)
            star(ex,ey,6,2,8)

size(400,200)
colormode(HSB)
for x in range(100,200,50):
    branch(x, 200.0, 40.0, 270.0, 7.0,False)
for x in range(200,300,50):
    branch(x, 200.0, 40.0, 270.0, 7.0,True)