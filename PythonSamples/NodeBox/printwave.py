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

#1秒間録音し
tone=loadwave("/Volumes/kkg2008/Sosumi-echo.wav")
for t in range(0,22100,20):
    print t/44100.0,tone[t]
