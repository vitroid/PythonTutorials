# coding: utf-8
from pygame import *
from pygame.locals import *
screen=display.set_mode((400,400),0,24)
black=Color(0,0,0)
back =Color(0)

frames = 0
while True:
    event.get()					#キーボードイベントを読む
    pressed = key.get_pressed()
    if pressed[K_q]:					#もしqキーが押されたら
        break
    x,y = mouse.get_pos()			#マウスの座標を読む
    back.hsva = (frames % 360, 100, 100, 100)
    frames += 1
    screen.fill(back)					#画面を塗る
    draw.circle(screen, black, (x,y), 100, 1)	#半径100の円を描く
    display.flip()				#紙芝居を切り替える。
    time.wait(10)				#10ミリ秒だけ待つ