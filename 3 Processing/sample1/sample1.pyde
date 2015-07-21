def setup():
    frameRate(30)
    size(500,500)

def draw():
    dx = 30 + 20*cos(frameCount/10.0)
    dy = 30 - 20*cos(frameCount/10.0)
    x = 250 + 100*cos(frameCount/70.0)
    y = 250 + 100*sin(frameCount/70.0)
    ellipse(x,y,dx,dy)


