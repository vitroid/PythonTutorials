from myaudio import *
from math import *

def sinewave(freq,length, amp):
    data = []
    for i in range(0, int(length*44100)):
        data += [ int( amp * sin(2.0*pi*i*freq/44100)) ]
    return data

tone = sinewave( 440, 1, 10000)
print tone
show(tone)
play(tone)
