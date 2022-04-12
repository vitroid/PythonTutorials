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
    
def mute(data,ratio):
    result = []
    for i in range(0,len(data)):
        result.append( int(data[i]*ratio) )
    return result

#2つの波形の重なり積分を計算する関数
def overlap(data1,data2):
    sum=0.0
    #min(x,y)はx,yのうち小さいほうを返す関数。
    length = min(len(data1),len(data2))
    #長いほうのリストにあわせて積分する。
    for i in range(0,length):
        sum += data1[i]*data2[i]
    #積分値を返す。
    return sum

#1秒間録音し
tone=record(1)
#0.1秒のエコーを重ねる。
echo=sinewave(400,0.1,0) + mute(tone,0.2)
tone = mix(tone,echo)

#解析
#少しずつ(0.05sec〜1sec)ずらしながら、相関係数を求める。
A = overlap(tone,tone)
for t in range(0,100):
    delta = 0.01*t
    delayed = sinewave(400,delta,0) + tone
    corr = overlap(tone,delayed) / A
    print delta, corr