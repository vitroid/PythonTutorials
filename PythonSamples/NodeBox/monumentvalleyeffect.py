size(300,300)
speed(30)
from math import cos,sin,pi

def setup():
    global pos
    pos = [[0,0]]

def draw():
    global pos
    colormode(HSB)
    background(0)
    stroke(1)
    nofill()
    lastpos = pos[-1]
    x = MOUSEX-WIDTH/2
    y = MOUSEY-HEIGHT/2
    dx = lastpos[0] - x
    dy = lastpos[1] - y
    if dx**2 + dy**2 > 10:
        pos.append((x,y))
    if len(pos) > 50:
        pos.pop(0)
    translate(WIDTH/2, HEIGHT/2)
    for i in range(5):
        c = cos(2*i*pi/5)
        s = sin(2*i*pi/5)
        for j in (-1,1):
            beginpath()
            x,y = pos[0][0], pos[0][1]
            x *= j
            rx,ry = x*c+y*s,-x*s+y*c
            moveto(rx,ry)
            for p in pos:
                x = p[0]
                y = p[1]
                x *= j
                rx,ry = x*c+y*s,-x*s+y*c
                lineto(rx,ry)
            endpath()
