#bar graph
pi = 3.14

values = [[12,35,11],[3,23,4],[12,44,9]]

def setup():
    size(300,500)
    frameRate(30)

def draw():
    t = frameCount
    stroke(0)
    drawn = False
    for ix in range(3):
        for iy in range(3):
            if t < values[iy][ix]:
                drawn = True
                pushMatrix()
                translate(100,300-t*6)
                scale(1,0.5)
                rotate(30*pi/180)
                fill(50+ix*100,50+iy*100,0,80)
                rect(ix*50,iy*50,45,45)
                popMatrix()
    if not drawn:
        noLoop()

        
