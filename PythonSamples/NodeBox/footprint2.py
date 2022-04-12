from math import *
size(300,300)
speed(30)
def setup():
    global pos,even
    pos = [[0,0,0]]
    even = 0
    
def leftfoot(x,y,dx,dy):
    len = sqrt(dx*dx+dy*dy)
    dx = 15.0*dx / len
    dy = 15.0*dy / len
    #go left
    sx = x - dy
    sy = y + dx
    line(x,y,sx,sy)
    strokewidth(2)
    line(sx,sy,sx+dx,sy+dy)
    line(sx,sy,sx+dx+dy*0.3,sy+dy-dx*0.3)
    line(sx,sy,sx+dx-dy*0.3,sy+dy+dx*0.3)
    
def rightfoot(x,y,dx,dy):
    len = sqrt(dx*dx+dy*dy)
    dx = 15.0*dx / len
    dy = 15.0*dy / len
    #go right
    sx = x + dy
    sy = y - dx
    line(x,y,sx,sy)
    strokewidth(2)
    line(sx,sy,sx+dx,sy+dy)
    line(sx,sy,sx+dx+dy*0.3,sy+dy-dx*0.3)
    line(sx,sy,sx+dx-dy*0.3,sy+dy+dx*0.3)

    
def draw():
    global pos,even
    stroke(0)
    strokewidth(2)
    x = MOUSEX
    y = MOUSEY
    dx = x - pos[-1][0]
    dy = y - pos[-1][1]
    if dx*dx+dy*dy > 20*20:
        even = 1 - even
        pos.append([x,y,even])
    if len(pos) > 30:
        pos.remove( pos[0] )
    for i in range(0,len(pos)-1):
        dx = pos[i+1][0] - pos[i][0]
        dy = pos[i+1][1] - pos[i][1]
        strokewidth(1)
        line(pos[i][0],pos[i][1],pos[i+1][0],pos[i+1][1])
        if pos[i+1][2] == 0:
            leftfoot(pos[i+1][0], pos[i+1][1], dx, dy)
        else:
            rightfoot(pos[i+1][0], pos[i+1][1], dx, dy)