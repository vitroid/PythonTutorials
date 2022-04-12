#ライブラリを使う場合はここに並べます。
from math import *
#キャンバスの大きさ=movieファイルの大きさ。
size(400,400)
#毎秒最大何フレーム表示するか。これを指定するとアニメーションとみなされる。
speed(30)
#⌘.(ピリオド)を押して止めるまで更新しつづける。


def textring(cx,cy,radius,string,offset):
    #頭にuを付けると日本語の文字も使える。
    n = len(string)     #lenは文字数を返す関数。
    n = float(n)        #floatは整数を実数にする。
    fontsize(6*radius/n)
    rotate(90+offset*180/pi)
    for i in range(0,n):
        x = radius * cos(-2.0 * pi * i / n - offset)
        y = radius * sin(-2.0 * pi * i / n - offset)
        hue = i / n
        fill(hue, 1, 0.8, 0.5)	#0.5は不透明度
        c = string[i]           #stringのi番目の文字
        text(c,cx+x,cy+y)         
        rotate(360.0/n)


#setupは最初に一度だけ実行される関数。
#ここでは、全フレームで共通に使う(global)変数cntに初期値0を入れている。
def setup():
    global cnt,x,y
    cnt = 0.0

#1フレームを描く関数。
def draw():
    #色モードを指定。
    colormode(HSB)
    global cnt
    #cntを増やす。
    cnt += 0.03
    textring(MOUSEX,MOUSEY,100,u"じゅげむじゅげむごこうのすりきれ", cnt)