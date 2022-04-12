#ライブラリを使う場合はここに並べます。
from math import sin, cos
#キャンバスの大きさ=movieファイルの大きさ。
size(300,300)
#毎秒最大何フレーム表示するか。これを指定するとアニメーションとみなされる。
speed(10)
#⌘.(ピリオド)を押して止めるまで更新しつづける。

#setupは最初に一度だけ実行される関数。
#ここでは、全フレームで共通に使う(global)変数cntに初期値0を入れている。
def setup():
    global cnt
    cnt = 0.0

#1フレームを描く関数。
def draw():
    #色モードを指定。
    colormode(HSB)
    global cnt
    #cntを増やす。
    cnt += 0.01
    if cnt > 1:
        cnt = cnt - 1.0
    fill(cnt, 1.0, 0.8)
    oval(100,100,200,200)
