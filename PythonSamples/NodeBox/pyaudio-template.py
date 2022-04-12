import pyaudio

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
outstream.write(data)

# close output stream
outstream.close()
# end using pyaudio library
p.terminate()