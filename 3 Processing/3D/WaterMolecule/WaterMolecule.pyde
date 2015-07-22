"""
Rotating water molecule
"""

def setup():
    size(500,500,P3D)
    frameRate(30)

def draw():
    BondLen = 100
    rO      = 30
    rH      = 15
    background(50)
    #Fixed lights
    ##lights()
    noStroke()
    #translation/rotation are reset in every draw()
    translate(250,250,0)
    rotateY(frameCount/10.0)
    #if you set lights here, lights also rotate with the model
    lights()
    angle = 104.5/2*PI/180
    xH    = BondLen*sin(angle)
    yH    = BondLen*cos(angle)
    fill(255,0,0)
    sphere(rO)
    fill(0,255,255)
    #part-time transformation
    with pushMatrix():
        translate(+xH, yH, 0)
        sphere(rH)
    #part-time transformation
    with pushMatrix():
        translate(-xH, yH, 0)
        sphere(rH)
    stroke(200)
    strokeWeight(10)
    line(0,0,0,+xH, yH, 0)
    line(0,0,0,-xH, yH, 0)

