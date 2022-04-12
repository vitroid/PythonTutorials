size(300,300)
speed(30)


def setup():
    global pos
    pos = []

def draw():
    global pos
    colormode(HSB)
    if FRAME % 3 == 0:
        pos = [[MOUSEX-150, MOUSEY-150, 1.0, 0.0]] + pos
    for i in pos:
        x = i[0]
        y = i[1]
        s = i[2]
        hue = i[3]
        rad = 5.0 * s
        hue = hue + 0.01
        hue = hue - int(hue)
        stroke( hue,1.0, 1.0)
        nofill()
        push()
        rotate(hue*360)
        star(x+150,y+150,5,rad*0.5,rad)
        #oval(x-rad+150,y-rad+150,rad*2,rad*2)
        pop()
        i[0]*=1.04
        i[1]*=1.04
        i[2]*=1.04
        i[3] = hue
    for i in pos:
        x = i[0]
        y = i[1]
        if x*x+y*y > 200*200:
            pos.remove(i)