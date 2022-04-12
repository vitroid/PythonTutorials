#! /usr/bin/env python

import pygame
from pygame.locals import *
screen=pygame.display.set_mode((400,400),0,24)
white=[255,255,255]
black=[0,0,0]

while True:
    pygame.event.get()
    x,y = pygame.mouse.get_pos()
    pressed = pygame.key.get_pressed()
    if pressed[K_q]:
        break
    screen.fill(white)
    pygame.draw.circle(screen, black, (x,y), 100, 1)
    pygame.display.flip()
    pygame.time.wait(10)
