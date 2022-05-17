from cmath import *
from nodebox_wrapper import *

def dx2d2phi(ix,phi,dx):
    xplus = ix + 1
    if len(phi) <= xplus:
        xplus -= len(phi)
    return ( phi[xplus] - 2.0*phi[ix] + phi[ix-1] )/dx**2

def rhs(ix,phi,dx):
    mass = 1.0
    hbar = 1.0
    k = 0.0
    x = ix * dx
    return (- hbar / mass) * dx2d2phi(ix,phi,dx) + pot[ix] * phi[ix]

def nextphi(ix,phi,dx,dt,pot,lastphi):
    hbar = 1.0
    if lastphi == None:
        return rhs(ix,phi,dx) * dt / (1.0j * hbar) + phi[ix]
    else:
        return rhs(ix,phi,dx) * 2.0 * dt / (1.0j * hbar) + lastphi[ix]

def normalize(phi,dx):
    sum = 0.0
    for i in range(0,len(phi)):
        sum += phi[i]*phi[i].conjugate()
    sum *= dx
    print(sum)
    sum = 1.0/sqrt(sum)
    for i in range(0,len(phi)):
        phi[i] *= sum

def setup():
    global phi,new,lastphi,dx,dt,pot
    dx = 0.1
    dt = 0.0001
    phi = [0.0 + 0.0j] * 100
    pot = [0.0] * 100
    for i in range(0,70):
        phi[i] = exp(1.0j * i*1.0) * exp(-((i-30.0)/6.0)**2)
    #wall
    for i in range(70,90):
        pot[i] =  200.0
    lastphi = None


def graphi(v,zoom):
    for i in range(0,len(v)):
        height = abs(v[i]) * zoom
        line(i,100,i,-height+100)

def graph(v,zoom):
    for i in range(0,len(v)):
        height = v[i] * zoom
        line(i,100,i,-height+100)

speed(10)
def draw():
    global phi,new,lastphi,dx,dt,pot
    for j in range(0,30):
        normalize(phi,dx)
        new = [0.0 + 0.0j] * len(phi)
        for i in range(0,len(phi)):
            new[i] = nextphi(i,phi,dx,dt,pot,lastphi)
        lastphi = list(phi)
        phi = list(new)
    stroke(1,0,0)
    graph(pot,0.1)
    stroke(0,0,0)
    graphi(phi,50)

# for nodebox_wrapper
size(512, 512)
animate(setup, draw)
