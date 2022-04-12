#coding: utf-8
import pygame
from pygame.locals import *
screen=pygame.display.set_mode((400,400),0,24)
white=[255,255,255]    #色をRGB(Red/Green/Blue)で指定する。255が最も明るい。
black=[0,0,0]

while True:                  #無限ループ
    pygame.event.get()
    pressed = pygame.key.get_pressed()
    if pressed[K_q]:
        break
    x,y = pygame.mouse.get_pos()
    screen.fill(white)       #画面を白で塗りつぶす
    pygame.draw.circle(screen, black, (x,y), 100, 1)
                             #ウィンドウの(200,200)に半径100、太さ1の黒い円を描く
    pygame.display.flip()    #裏画面に描かれたものを表示する。
    pygame.time.wait(10)    #100ミリ秒待つ
