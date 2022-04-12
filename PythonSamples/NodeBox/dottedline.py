size(300,300)
speed(30)
def setup():
    global pos
    pos = [[0,0]]
def draw():
    global pos
    x = MOUSEX
    y = MOUSEY
    dx = x - pos[-1][0]
    dy = y - pos[-1][1]
    if dx*dx+dy*dy > 10*10:
        pos.append([x,y])
    if len(pos) > 30:
        pos.remove( pos[0] )
    for i in range(0,len(pos)):
        x = pos[i][0]
        y = pos[i][1]
        oval( x-3, y-3, 6,6 )
