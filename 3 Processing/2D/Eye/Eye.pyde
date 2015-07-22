"""
Eyes following you

Processingでは、マウスの位置をmouseX, mouseY変数
でいつでも取得できます。
以下では、目玉オブジェクトを作り、それを5つ並べてそれ
ぞれが独立に動くようになっています。
"""

class eye():
    def __init__(self,x,y,r,ir):
        self.x, self.y, self.r, self.ir = x,y,r,ir

    def update(self,x,y):
        fill(255)
        stroke(0)
        strokeWeight(1)
        ellipse(self.x,self.y,self.r*2,self.r*2)
        dx,dy = x - self.x, y - self.y
        dd = dx**2 + dy**2
        if dd > (self.r-self.ir)**2:
            ratio = (self.r-self.ir) / sqrt(dd)
            dx *= ratio
            dy *= ratio
        noStroke()
        fill(0)
        ellipse(self.x+dx,self.y+dy,self.ir*2,self.ir*2)


def setup():
    global eyes
    size(360,120)
    eyes = []
    for i in range(5):
        eyes.append(eye(60*(i+1),60,30,20))

def draw():
    global eyes
    for e in eyes:
        e.update(mouseX, mouseY)
