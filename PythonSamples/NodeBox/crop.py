from myaudio import *
from math import *

left = loadwave("left.wav")
left = left[100000:1000000]
savewave("leftcrop.wav",left)

right = loadwave("right.wav")
right = right[100000:1000000]
savewave("rightcrop.wav",right)
