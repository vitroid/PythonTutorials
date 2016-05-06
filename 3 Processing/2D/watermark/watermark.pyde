w = int(300 * 210 / 25.4)
h = int(300 * 298 / 25.4)


phi = (1+sqrt(5))/2
theta = 2*PI / phi


size(w,h)
textSize(400)
for i in range(4):
    for j in range(5):
        with pushMatrix():
            translate(i*w/3,j*h/4)
            rotate(-PI/5)
            text("VOID", 0, 0)

loadPixels()
background(255)
noStroke()
fill(0)
i = 0
th = 0
ratio = 4
while True:
    r = 3*sqrt(i)
    i += 1
    th = (theta*i)%(2*PI)
    x = int(r * cos(th) + w/2 )
    y = int(r * sin(th) + h/2 )
    if x**2 + y**2 > w**2+h**2:
        break
    if 0 <= x < w and 0 <= y < h:
        loc = x+y*w
        pix = pixels[loc]
        if pix != -1:
            rect(x,y,1,1)
i = 0
stroke(0)
fill(255)
while True:
    r = 3*ratio*sqrt(i)
    i +=  1
    th = (theta * i) % (2*PI)
    x = int(r * cos(th) + w/2 )
    y = int(r * sin(th) + h/2 )
    if x**2 + y**2 > w**2+h**2:
        break
    if 0 <= x < w and 0 <= y < h:
        loc = x+y*w
        pix = pixels[loc]
        if pix == -1:
            #rect(x,y,ratio,ratio)
            rect(x,y,4,4)

save("watermark.png")
