import xmas2008
size(400,400)
speed(30)
def draw():
    myname = "matto"
    hisname = "imo"
    mystate = [MOUSEX,MOUSEY,mousedown]
    hisstate = xmas2008.proxy.query(myname,mystate,hisname)
    if hisstate != None:
        print hisstate
        if hisstate[2]:
            fill(1,0,0)
        else:
            fill(0,1,0)
        oval(hisstate[0]-20,hisstate[1]-20,40,40)
    if mystate[2]:
        fill(1,0,1)
    else:
        fill(0,1,1)
    oval(mystate[0]-20,mystate[1]-20,40,40)