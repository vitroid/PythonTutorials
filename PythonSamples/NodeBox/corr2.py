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
    length = min(len(data1),len(data2))
    #長いほうにあわせる。
    data = [0] * length
    for i in range(0,length):
        data[i] += data1[i]
    for i in range(0,length):
        data[i] += data2[i]
    return data
    
def delay(data,sec):
    #サンプリング周波数44100Hzなので、1秒遅延させるには
    #44100個の0をデータの先頭にくっつける。
    return [0] * int(sec*44100) + data

def volume(data,amp):
    result = []
    for i in range(0,len(data)):
        result.append( int(data[i]*amp) )
    return result

def overlap(data1,data2):
    sum=0.0
    #min(x,y)はx,yのうち小さいほうを返す関数。
    length = min(len(data1),len(data2))
    #長いほうにあわせる。
    for i in range(0,length):
        sum += data1[i]*data2[i]
    return sum

def maxcorr(tone):
    self = overlap(tone,tone)
    maxtime = 0.0
    maxcorr = 0.0
    for d in range(5,200):
        time = 0.005*d
        delayed = delay(tone,time)
        corr = overlap(tone,delayed) / self
        if maxcorr < corr:
            maxtime = time
            maxcorr = corr
    return (maxtime, maxcorr)


#1秒間録音し
tone=loadwave("/Users/matto/Shared/Sosumi-echo.wav")
#tone=loadwave("/Users/matto/Shared/obama.wav")
original = list(tone)

while 1:
    (delaytime, corr) = maxcorr(tone)
    print delaytime,corr
    #play(tone)
    if corr < 0.03:
        break
    delayed = delay(tone, delaytime)
    cancel  = volume(delayed, -corr)
    tone = mix(tone, cancel)
savewave("/Users/matto/Shared/Sosumi-unecho.wav", tone)