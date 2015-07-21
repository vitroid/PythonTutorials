#A useful template for manual rotation
#last mouse position
lastx = 0

#callback
def mousePressed():
    global lastx
    lastx = mouseX  #mouseX and Y are system-defined

#callback
def mouseDragged():
    global lastx
    popMatrix()
    rotx = mouseX - lastx
    lastx = mouseX
    rotateY(rotx/100.0)
    pushMatrix()

def setup():
    size(500, 500, P3D)        #ウィンドウのサイズ。P3Dをつけると3次元モードに
    translate(250,250,0)       #center of the screen
    pushMatrix()

#draw()で1コマを描きます。
def draw():
    popMatrix()  #recover the last rotation matrix
    pushMatrix() #and remember it

    #draw as you like
    background(200)
    noFill();
    stroke(0)
    box(140, 120, 150)            #そこに箱を描きます。
    #line(0,0,0,100,100,100)
    translate(100,20,10)
    box(140, 120, 150) 


    
