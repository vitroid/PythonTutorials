def circ(x,y,r):
     fill(random(),1.0,1.0)
     oval(x-r,y-r,r*2,r*2)
colormode(HSB)
def recirc(x,y,r):
    circ(x,y,r)
    if 1.0 < r:
        recirc(x-r*3.0/4.0,y,r/4.0)
        recirc(x+r/4.0,y,r*3.0/4.0)

recirc(100.0, 100.0, 100.0)