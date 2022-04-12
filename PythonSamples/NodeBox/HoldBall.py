size(300,300)
speed(30)

def setup():
    global pos,counter
    pos = []
    counter = 0.0
def draw():
    global pos,counter
    translate(150,150)
    x = MOUSEX - 150
    y = MOUSEY - 150
    if mousedown:
        counter= counter + 1.0
        oval(x-counter, y-counter, counter*2, counter*2)
    else:
        if counter > 0.0:
            pos = pos + [[x,y,counter]]
        counter = 0.0
    for i in range(0,len(pos)):
        for j in range(0,3):
            pos[i][j]*=1.1
        x = pos[i][0]
        y = pos[i][1]
        r = pos[i][2]
        oval( x-r, y-r, 2*r,2*r )
    for p in pos:
        x = p[0]
        y = p[1]
        if x*x+y*y > 200*200:
            pos.remove( p )