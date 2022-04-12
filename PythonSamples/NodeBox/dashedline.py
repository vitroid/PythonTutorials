size(300,300)
speed(30)
def setup():
    global pos,even
    pos = [[0,0]]
    even = 0
def draw():
    global pos,even
    stroke(0)
    strokewidth(5)
    x = MOUSEX
    y = MOUSEY
    dx = x - pos[-1][0]
    dy = y - pos[-1][1]
    if dx*dx+dy*dy > 10*10:
        pos.append([x,y])
        even = 1-even
    if len(pos) > 30:
        pos.remove( pos[0] )
    for i in range(even,len(pos),2):
        line( pos[i][0],pos[i][1], pos[i+1][0], pos[i+1][1] )
