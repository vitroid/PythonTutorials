#! /usr/bin/env python

import pygame
from pygame.locals import *
screen=pygame.display.set_mode((400,400),0,24)
white = Color(0)
white.hsva = (0,0,100,100)
black = Color(0)
col   = Color(0)

ay = 400
circles = []
hue = 1
while True:
    screen.fill(white)
    pygame.event.get()
    pressed = pygame.key.get_pressed()
    if pressed[K_q]:
        break
    button1,button2,button3 = pygame.mouse.get_pressed()
    if button1:
        x,y = pygame.mouse.get_pos()
        r = 30.0
        circles.append([x,y,r,hue])
        hue += 3
        if hue >= 360:
            hue -= 360
    updated = []
    for x,y,r,h in circles:
        col.hsva = (h,100,100,10)
        pygame.draw.circle(screen, col, (x,y), r, 0)
        dx = x - 200
        dy = y - 200
        dx *= 1.02
        dy *= 1.02
        r  *= 1.02
        x = 200 + dx
        y = 200 + dy
        if dx**2 + dy**2 < 500**2:
            updated.append([x,y,r,h])
    circles = updated
    pygame.display.flip()
    pygame.time.wait(10)
