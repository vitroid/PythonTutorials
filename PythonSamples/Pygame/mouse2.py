#! /usr/bin/env python

import pygame
from pygame.locals import *
screen=pygame.display.set_mode((400,400),0,24)
white = Color(0)
white.hsva = (0,0,100,100)
col = Color(0)

screen.fill(white)
hue = 0
while True:
    pygame.event.get()
    x,y = pygame.mouse.get_pos()
    pressed = pygame.key.get_pressed()
    if pressed[K_q]:
        break
    col.hsva = (hue,100,100,10)
    pygame.draw.circle(screen, col, (x,y), 100, 3)
    hue += 1
    if hue >= 360:
        hue -= 360
    pygame.display.flip()
    pygame.time.wait(10)
