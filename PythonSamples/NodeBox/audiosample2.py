from myaudio import *

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
