#! /usr/bin/env python

import pygame
from pygame.locals import *
screen=pygame.display.set_mode((400,400),0,24)
white = Color(0)
white.hsva = (0,0,100,100)
black = Color(0)

ay = 400
vy = 0
x = y = 0
while True:
    screen.fill(white)
    pygame.event.get()
    pressed = pygame.key.get_pressed()
    if pressed[K_q]:
        break
    button1,button2,button3 = pygame.mouse.get_pressed()
    if button1:
        x,y = pygame.mouse.get_pos()
        vy = 0.0
    pygame.draw.circle(screen, black, (x,y), 100, 3)
    vy = vy + ay * 0.01
    y  = y  + vy * 0.01
    pygame.display.flip()
    pygame.time.wait(10)
