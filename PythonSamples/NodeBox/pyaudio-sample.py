import pyaudio
import wave
import sys
import struct

# start using pyaudio library
p = pyaudio.PyAudio()

#preparation
chunk = 44100
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
data = instream.read(chunk)
    
# close stream
instream.close()

# open output stream
outstream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE*3/2,
                output = True)

# write data
outstream.write(data)
# repeat again
outstream.write(data)

# close output stream
outstream.close()

# end using pyaudio library
p.terminate()
