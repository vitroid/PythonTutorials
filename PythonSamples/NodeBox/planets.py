#planetary simulation

planets = [[1000000.0, [0.0, 0.0],  [0.0, 0.0], [0.0, 0.0],[],(20.0,)],
           [1.0,    [100.0, 0.0],[0.0, 10.0], [0.0, 0.0],[],(6.0,)],
           [1.0,    [200.0, 0.0],[0.0, 7.07], [0.0, 0.0],[],(6.0,)]]

planets = [[10000.0, [0.0, 0.0],  [0.0, 0.0], [0.0, 0.0],[],(20.0,)]]
#           [1.0,    [100.0, 0.0],[0.0, 10.0], [0.0, 0.0],[],(6.0,)],
#           [1.0,    [200.0, 0.0],[0.0, 7.07], [0.0, 0.0],[],(6.0,)]]



def step(dt):
    for p in planets:
        p[1][0] += p[2][0] * dt / 2
        p[1][1] += p[2][1] * dt / 2
        p[3][0] = 0.0
        p[3][1] = 0.0
    minx = [10000.0]*len(planets)
    for i in range(len(planets)):
        pi = planets[i]
        for j in range(i+1,len(planets)):
            pj = planets[j]
            dx = pj[1][0] - pi[1][0]                        
            dy = pj[1][1] - pi[1][1]
            d  = sqrt(dx**2 + dy**2)
            if d < minx[i]:
                minx[i] = d
            if d < minx[j]:
                minx[j] = d
            fx = g*pi[0]*pj[0] * dx / d**3
            fy = g*pi[0]*pj[0] * dy / d**3
            pi[3][0] += fx
            pi[3][1] += fy
            pj[3][0] -= fx
            pj[3][1] -= fy
    for p in planets:
        p[2][0] += p[3][0] * dt / p[0]
        p[2][1] += p[3][1] * dt / p[0]
    suggestdt = dt * 1.1
    if suggestdt > 1.0:
        suggestdt = 1.0
    for i in range(len(planets)):
        p = planets[i]
        p[1][0] += p[2][0] * dt / 2
        p[1][1] += p[2][1] * dt / 2
        disp = sqrt(p[2][0]**2 + p[2][1]**2) * dt
        if minx[i] < disp:
            ratio = minx[i] / disp * 0.7
            if ratio < suggestdt:
                suggestdt = ratio
    if suggestdt != 1.0:
        print suggestdt
    return suggestdt


def leap(t):
    global dt
    while t > dt:
        dt = step(dt)
        t -= dt
    step(t)



def trace(now,tracelen):
    #trace
    for p in planets:
        p[4].append(tuple(p[1]+[now]))
        while p[4][0][2] < now-tracelen:
            del p[4][0]


from math import *

speed(30)
size(1024,768)
g  = 1.0
#def setup():
tracelen = 500
zoom = 1.0
now = 0.0
dt = 1.0

def draw():
    global tracelen, g, zoom, now
    background(0)
    translate(WIDTH/2, HEIGHT/2)
    if FRAME < 300:
        leap(1.0)
        now += 1.0
    else:
        leap(3.0)
        now += 3.0
    trace(now,tracelen)
    #slant
    slant = 2
    #draw trace
    nofill()
    stroke(0.3)
    for p in planets:
        strokewidth(p[5][0]/2)
        beginpath(p[4][0][0]*zoom,p[4][0][1]/slant*zoom)
        for x in p[4]:
            lineto(x[0]*zoom,x[1]/slant*zoom)
        moveto(p[4][0][0]*zoom,p[4][0][1]/slant*zoom)
        endpath()
    #draw interaction
    if FRAME < 300:
        stroke(0.5)
        strokewidth(1)
        for i in range(len(planets)):
            pi = planets[i]
            for j in range(i+1,len(planets)):
                pj = planets[j]
                line(pj[1][0]*zoom,pj[1][1]/slant*zoom,pi[1][0]*zoom,pi[1][1]/slant*zoom)
    #draw planets
    fill(1)
    nostroke()
    rmax = 0.0
    for p in planets:
        r = p[5][0]
        oval((p[1][0]-r)*zoom,(p[1][1]/slant-r)*zoom,2*r*zoom,2*r*zoom)
        r = sqrt(p[1][0]**2 + p[1][1]**2)
        if rmax < r:
            rmax = r
    if rmax* zoom > 500:
        zoom *= 0.996
    elif rmax*zoom < 400:
        zoom *= 1.002
    #ejected planet
    for i in range(1,len(planets)):
        pi = planets[i]
        pj = planets[0]
        dx = pj[1][0] - pi[1][0]                        
        dy = pj[1][1] - pi[1][1]
        d  = sqrt(dx**2 + dy**2)
        ep = -g*pi[0]*pj[0] / d 
        ek = pi[0]*(pi[2][0]**2 + pi[2][1]**2)/2.0
        #print i,ep+ek
        if ep + ek > -10.0:
            print "WARNING:",i
            if d > 2000:
                print "EXTINCT:",i
                del planets[i]
                break
    if FRAME in (1, 100, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290):
        i = len(planets)
        r = i * 50
        v = sqrt(10000.0 / r) + random()*1.6 - 0.8
        theta = (i-1) * 1.0
        c = cos(theta)
        s = sin(theta)
        #[1.0,    [100.0, 0.0],[0.0, 10.0], [0.0, 0.0],[],(6.0,)],
        planets.append([10.0, [r*c,r*s],[v*s,v*-c],[0.0,0.0],[],(6.0,)])
        

        