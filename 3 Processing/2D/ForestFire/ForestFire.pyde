# Forest Fire
import random
desert = 0
tree   = 1
burning= 2
burnt  = 3

dens = 0.59
pix  = 10
forestsize = 80
forest = [[desert for i in range(forestsize)] for j in range(forestsize)]
for i in range(forestsize):
    for j in range(forestsize):
        if random.random() < dens:
            forest[i][j] = tree 


def drawone(i,j,f):
    if f[i][j] == desert:
        fill(255,128,0)
    elif f[i][j] == tree:
        fill(0,128,0)
    elif f[i][j] == burning:
        fill(255,0,0)
    else:
        fill(0)
    rect(i*pix,j*pix,pix-1,pix-1)

def setup():
    global forest
    size(forestsize*pix,forestsize*pix)
    noStroke()
    frameRate(30)
    for i in range(forestsize):
        for j in range(forestsize):
            drawone(i,j,forest)
                
def draw():
    global forest#,forestsize
    modify = []
    for i in range(forestsize):
        for j in range(forestsize):
            if forest[i][j] == burning:
                modify.append((i,j,burnt))
            elif forest[i][j] == tree:
                ip = (i+1) % forestsize
                jp = (j+1) % forestsize
                if ( forest[i][j-1] == burning or
                     forest[i][jp]  == burning or
                     forest[i-1][j] == burning or
                     forest[ip][j]  == burning ):
                    modify.append((i,j,burning))
    if len(modify) == 0:
        noLoop()
        print("no loop")
    else:
        for m in modify:
            i,j,val = m
            forest[i][j] = val
            drawone(i,j,forest)

def mousePressed():
    global forest
    x = mouseX // pix
    y = mouseY // pix
    if 0 <= x < forestsize and 0 <= y < forestsize:
        if forest[x][y] == tree:
            #ignite
            forest[x][y] = burning
            loop()
            print("Loop")

