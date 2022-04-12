#! /usr/bin/env python

import pygame
screen=pygame.display.set_mode((400,400),0,24)
white=[255,255,255]
black=[0,0,0]

while True:
    screen.fill(white)
    pygame.draw.circle(screen, black, (200,200), 100, 1)
    pygame.display.flip()
    pygame.time.wait(100)
