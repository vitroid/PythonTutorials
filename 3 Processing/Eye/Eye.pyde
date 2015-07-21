#an eye

class eye():
    def __init__(self,x,y,r,ir):
        self.x, self.y, self.r, self.ir = x,y,r,ir

    def update(self,x,y):
        fill(255)
        stroke(0)
        strokeWeight(1)
        ellipse(self.x,self.y,self.r,self.r)
        dx,dy = x - self.x, y - self.y
        dd = dx**2 + dy**2
        if dd > (self.r-self.ir)**2:
            ratio = (self.r-self.ir) / sqrt(dd)
            dx *= ratio
            dy *= ratio
        ellipse(self.x+dx,self.y+dy,self.ir,self.ir)


def setup():
    global e
    size(400,400)
    #e = eye(50,50,30,10)

def draw():
    global e
    #e.update(mouseX, mouseY)

