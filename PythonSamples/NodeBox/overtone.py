from myaudio import *
from math import *

def sinewave(freq,length, amp):
    data = []
    for i in range(0, int(length*44100)):
        data += [ int( amp * sin(2.0*pi*i*freq/44100)) ]
    return data

def overtone(data):
    newdata=[]
    for i in range(0,len(data),2):
        newdata += [ data[i] ]
    return newdata
    
tone = sinewave( 400, 1, 10000)
hightone = overtone(tone)
play(hightone)
