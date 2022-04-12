#Free-rotating dipoles as a sample of vdW force
#for nloop frames

from math import pi,sin,cos
def angle(t,a,b,c,d):
    return sin(t*2*pi/a)+sin(t*2*pi/b)+sin(t*2*pi/c)+d


speed(30)
offset = 1
nloop = 300
size(400+offset*2,200+offset*2)
def setup():
    pass
    
def draw():
    global offset,nloop
    t = FRAME
    R = 100
    particle = "A"
    model    = "II"  #direct or induced
    if particle == "A":
        A1 = angle(t, nloop/10., nloop/7., nloop/5.,10)  #A
    else:
        A1 = angle(t, nloop/9., nloop/6., nloop/4.,10)   #B
    RR = 10
    x = RR * cos(3*A1)
    y = RR * sin(3*A1)
    r = 10
    if model == "D":
        nofill()
        stroke(0.75,0,0.75)
        oval(0+offset,0+offset,R*2,R*2)
        nostroke()
        fill(1,0,0)
        oval(x-r+R+offset,y-r+R+offset,r*2,r*2)
        fill(0,0,1)
        oval(-x-r+R+offset,-y-r+R+offset,r*2,r*2)
    if model == "I":
        strokewidth(3)
        for i in range(0,360,2):
            lx = R*3*cos(i*2*pi/360+3*A1)
            ly = R*3*sin(i*2*pi/360+3*A1)
            C = abs(i/360.-0.5)*2
            D = 1-C
            stroke(C,0,D)
            line(R+offset,R+offset,R+offset+lx, R+offset+ly)
        stroke(1,1,1)
        strokewidth(3)
        fill(1,0,0)
        oval(x-r+R+offset,y-r+R+offset,r*2,r*2)
        fill(0,0,1)
        oval(-x-r+R+offset,-y-r+R+offset,r*2,r*2)

#RIMs
        nofill()
        stroke(0.75,0,0.75)
        oval(0+offset,0+offset,R*2,R*2)
        nofill()
        stroke(0.75,0,0.75)
        oval(0+R*2+offset,0+offset,R*2,R*2)

        strokewidth(3)
        fill(1,1,1)
        stroke(1,0,0)
        oval(x-r+3*R+offset,y-r+R+offset,r*2,r*2)
        stroke(0,0,1)
        oval(-x-r+3*R+offset,-y-r+R+offset,r*2,r*2)
    if model == "II":
        strokewidth(2)
        for i in range(0,360,5):
            lx = R*3*cos(i*2*pi/360+3*A1)
            ly = R*3*sin(i*2*pi/360+3*A1)
            C = abs(i/360.-0.5)*2
            D = 1-C
            stroke(C,0,D)
            line(R+offset,R+offset,R+offset+lx, R+offset+ly)
            line(R*3+offset,R+offset,R*3+offset+lx, R+offset+ly)

#RIMs
        nofill()
        stroke(0.75,0,0.75)
        oval(0+offset,0+offset,R*2,R*2)
        nofill()
        stroke(0.75,0,0.75)
        oval(0+R*2+offset,0+offset,R*2,R*2)

        strokewidth(3)
        fill(1,1,1)
        stroke(1,0,0)
        oval(x-r+3*R+offset,y-r+R+offset,r*2,r*2)
        stroke(0,0,1)
        oval(-x-r+3*R+offset,-y-r+R+offset,r*2,r*2)
        fill(1,1,1)
        stroke(1,0,0)
        oval(x-r+1*R+offset,y-r+R+offset,r*2,r*2)
        stroke(0,0,1)
        oval(-x-r+1*R+offset,-y-r+R+offset,r*2,r*2)
