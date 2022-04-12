import math
speed(30)
size(300,300)


hist = []

def history(nums,histlen):
    colormode(HSB)
    if len(hist) != 0 and len(hist[0]) != len(nums):
        print "Different number of data"
    else:
        hist.append(nums)
        if len(hist) > histlen:
            hist.remove(hist[0])
        for j in range(len(nums)):
            hue = j * 0.61803398875
            hue = hue % 1.0
            stroke(hue,1.0, 0.5)
            for i in range(1,len(hist)):
                line((i-1)*WIDTH/histlen, hist[i-1][j],
                     i*WIDTH/histlen, hist[i][j])


def draw():
    history([100.0,FRAME,100+100.0*math.sin(FRAME/20.0)],20)
