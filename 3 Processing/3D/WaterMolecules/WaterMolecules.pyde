"""
Rotating water molecules
"""
from random import random

waterPos = [(500*random()-250,
             500*random()-250,
             500*random()-250,
             2*PI*random(),
             PI*random(),
             2*PI*random()) for i in range(10)]
BondLen = 100
rO      = 30
rH      = 15
angle = 104.5/2*PI/180
xH    = BondLen*sin(angle)
yH    = BondLen*cos(angle)


def setup():
    size(500,500,P3D)
    frameRate(30)


def draw():
    background(50)
    translate(250,250,0)
    rotateY(frameCount/30.0)
    #if you set lights here, lights also rotate with the model
    lights()
    for wp in waterPos:
        #temporary transformation
        with pushMatrix():
            x,y,z,a,b,c = wp
            translate(x,y,z)
            rotateZ(a)
            rotateY(b)
            rotateZ(c)
            Water()


def Water():
    noStroke()
    fill(255,0,0)
    sphere(rO)
    fill(0,255,255)
    #temporary transformation
    with pushMatrix():
        translate(+xH, yH, 0)
        sphere(rH)
    #temporary transformation
    with pushMatrix():
        translate(-xH, yH, 0)
        sphere(rH)
    stroke(200)
    strokeWeight(10)
    line(0,0,0,+xH, yH, 0)
    line(0,0,0,-xH, yH, 0)
    
