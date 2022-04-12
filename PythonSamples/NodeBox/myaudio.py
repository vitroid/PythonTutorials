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
    p.terminate()
    
def loadwave(filename):
    # start using pyaudio library
    p = pyaudio.PyAudio()
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
    p.terminate()
    return datalist
