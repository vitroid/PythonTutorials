from myaudio import *
from math import *

def sinewave(freq,length, amp):
    data = []
    for i in range(0, int(length*44100)):
        data += [ int( amp * sin(2.0*pi*i*freq/44100)) ]
    return data

def show(data):
    beginpath(0,320)
    #全部は表示できないので、はじめの1000個だけ表示
    for i in range(0, min(1000,len(data))):
        lineto(i, data[i]/100+320)
    moveto(0,320)
    endpath()

tone = sinewave( 440, 1, 10000)
hightone = sinewave( 880, 1, 10000)
plays(tone,hightone)