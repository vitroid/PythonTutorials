import pyaudio
import wave
import sys
import math
import struct

chunk = 1024
p = pyaudio.PyAudio()
# open stream
stream = p.open(format = pyaudio.paInt16,
                channels = 1,
                rate = 44100,
                output = True)

# play stream
buf = [0] * 1024
t=0.0
for i in range(0,100):
    data = ""
    for j in range(0,1024):
        buf[j] = 32767.0 * math.sin(2.0*math.pi*t*400/44100)
        t+=1.0
        data += struct.pack("1h", int(buf[j]))
    stream.write(data)
    #data2 = struct.unpack( "1024h", data );
    #print data2


stream.close()
p.terminate()