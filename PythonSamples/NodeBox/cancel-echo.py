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


#1秒間録音し
tone=loadwave("/Volumes/kkg2008/Ping.wav")
play(tone)
#0.1秒遅らせ
delayed = delay(tone, 0.1)
#音量を小さくして
weak = volume(delayed, 0.3)
#2つを重ねて
mixed = mix(tone,weak)
#反響入りの音を再生する。
play(mixed)
#savewave("Ping-echo.wav",mixed)

#mixedだけをもとに、エコーを消す。
#0.1秒遅らせ、
echo = delay(mixed, 0.1)
#反響音の強さにあわせ、波の上下を逆にして
echo = volume(echo, -0.3)
#重ねあわせる。
mixed = mix(mixed, echo)
play(mixed)

