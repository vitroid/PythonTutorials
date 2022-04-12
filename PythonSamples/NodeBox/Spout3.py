from math import *
size(300,300)
speed(10)


def setup():
    global pos,cnt
    pos = []
    cnt = 0

def draw():
    global pos,cnt
    cnt = cnt + 1
    colormode(HSB)
    x = MOUSEX - 150
    y = MOUSEY - 150
    x = x + 10.0 * cos( cnt * 0.5  )
    y = y + 10.0 * sin( cnt * 0.5 )
    str = u"©®℗℠™☺☻☹♠♣♥♦♤♧♡♢"
    pos = [[x,y , 1.0, 0.0, str[cnt%len(str)]]] + pos
    for i in pos:
        x = i[0]
        y = i[1]
        s = i[2]
        hue = i[3]
        c = i[4]
        rad = 2.0 * s
        hue = hue + 0.03
        hue = hue - int(hue)
        fill( hue,1.0, 1.0)
        push()
        rotate(hue*360.0)
        #oval(x-rad+150,y-rad+150,rad*2,rad*2)
        #star(x+150,y+150,5,rad/2,rad)
        fontsize(rad*3)
        text(c, x+150,y+150)
        pop()
        i[0]*=1.1
        i[1]*=1.1
        i[2]*=1.1
        i[3] = hue
    for i in pos:
        x = i[0]
        y = i[1]
        if x*x+y*y > 200*200:
            pos.remove(i)