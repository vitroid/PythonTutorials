import pyaudio
import wave
import sys
import struct

def play(datalist):
    # start using pyaudio library
    p = pyaudio.PyAudio()
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    # open output stream
    outstream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    output = True)
    # write data
    length = len(datalist)
    data = ""
    for i in datalist:
        data += struct.pack( "1h", i )
    outstream.write(data)

    # close output stream
    outstream.close()
    # end using pyaudio library
    p.terminate()


def record(length):
    # start using pyaudio library
    p = pyaudio.PyAudio()

    #preparation
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    # open input stream
    instream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)

    # input data
    all = []
    s = int(length*RATE/chunk)
    for i in range(0, s):
        data = instream.read(chunk)
        l = len(data)/2
        all+=list(struct.unpack( str(l)+"h", data ) )
    # close stream
    instream.close()
    # end using pyaudio library
    p.terminate()
    return all

def plays(left,right):
    # start using pyaudio library
    p = pyaudio.PyAudio()
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    # open output stream
    outstream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    output = True)
    # write data
    length = len(left)
    data = ""
    for i in range(length):
        data += struct.pack( "2h", left[i], right[i] )
    outstream.write(data)

    # close output stream
    outstream.close()
    # end using pyaudio library
    p.terminate()


def savewave(filename, datalist):
    # start using pyaudio library
    p = pyaudio.PyAudio()
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    # open output stream
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    # write data
    length = len(datalist)
    data = ""
    for i in datalist:
        data += struct.pack( "1h", i )
    wf.writeframes(data)
    # close output stream
    wf.close()
    # end using pyaudio library
    p.terminate()

def loadwave(filename):
    global p
    wf = wave.open(filename, 'rb')
    chunk = 1024
    # read data
    data = wf.readframes(chunk)
    l = len(data)/2
    datalist = list(struct.unpack( str(l)+"h", data ) )

    # play stream
    while data != '':
        data = wf.readframes(chunk)
        l = len(data)/2
        datalist += list(struct.unpack( str(l)+"h", data ) )

    return datalist

def show(data):
    stroke(0)
    nofill()
    beginpath(0,320)
    #全部は表示できないので、はじめの1000個だけ表示
    for i in range(0, min(1000,len(data))):
        lineto(i, data[i]/100+320)
    moveto(0,320)
    endpath()

#1秒分を録音
data = record(1)
#再生
play(data)
#波形の表示
show(data)
#stereo再生
plays(data,data)
print data
#wave形式で保存
savewave("output.wav", data)
#もう一度読み込み
data = loadwave("output.wav")
#再生
play(data)