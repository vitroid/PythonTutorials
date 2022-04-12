speed(10)
coreimage=ximport("coreimage")

canvas = coreimage.canvas(150,150)
layer  = canvas.append(color(0))
canvas.draw()

pixels = layer.pixels()

def draw():
    for i in range(100):
        pixels.set_pixel(random()*150,random()*150,color(1,1,1))
    pixels.update()
    canvas.draw()
    print FRAME

