isight = ximport("isight")
img = isight.grab(640, 480) # width and height are 320 x 240 by default
image(img,0,0)