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

def mix(data1,data2):
    #max(x,y)はx,yのうち大きいほうを返す関数。
    length = max(len(data1),len(data2))
    #長いほうにあわせる。
    data = [0] * length
    for i in range(0,len(data1)):
        data[i] += data1[i]
    for i in range(0,len(data2)):
        data[i] += data2[i]
    return data
    
tone = sinewave( 400, 1, 10000)
hightone = sinewave( 500, 1, 10000)
mixed = mix(tone,hightone)
play(mixed)
show(tone)
show(hightone)
show(mixed)