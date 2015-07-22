"""
ソーティング(並べ替え)のプロセスを可視化したものです。
"""

def bubblesort(data):
    for x in range(len(data)):
        for y in range(x+1,len(data)):
            if data[x] > data[y]:
                data[x],data[y] = data[y],data[x]
                yield data



pix = 8
import random
data = [random.random() for i in range(50)]
iter = bubblesort(data)

def setup():
    size(pix*len(data),pix*len(data))
    #frameRate(3)

def draw():
    d = next(iter, None)
    if d == None:
        noLoop()
    else:
        background(0)
        fill(255)
        noStroke()
        textSize(24)
        text("{0}".format(frameCount+1),10,20)
        noFill()
        drawone(d)

def drawone(d):
    noFill()
    stroke(255)
    strokeWeight(2)
    for i in range(len(d)):
        line(0,pix*i,d[i]*width,pix*i)
