#!/usr/bin/env python
# coding: utf-8
import pygame
from pygame.locals import *
import random as ra


#settings
RGB = "rgb"
HSB = "hsb"
COLORMODE = RGB
STROKECOLOR = Color(0,0,0,255)
FILLCOLOR   = Color(100,100,100,255)
BACKGROUND = Color(255,255,255,255)
FILL = True
STROKE = False
STROKEWIDTH = 1
FPS = 0
SCREEN=pygame.display.set_mode((1000,1000),0,24)
FRAME = 0
MOUSEX = 1
MOUSEY = 2
mousedown = False
keydown = False
_sysfont = None
pygame.font.init()
_sysfont = pygame.font.SysFont(u"helvetica", 10)

#define the campus size
def size(w,h):
    global SCREEN
    SCREEN=pygame.display.set_mode((int(w),int(h)),0,24)
    SCREEN.fill(BACKGROUND)
    pygame.display.flip()    #裏画面に描かれたものを表示する。

def colormode(mode):
    global COLORMODE
    COLORMODE = mode

#set the line color
#value range: 255,255,255 for pygame RGB
#360,100,100,100 for pygame hsva
def stroke(A,B=999,C=999,D=0.5):
    global STROKECOLOR,STROKE
    STROKE = True
    if B == 999:
        B = A
        C = A
    if A > 1:
        A = 1
    if B > 1:
        B = 1
    if C > 1:
        C = 1
    if COLORMODE == RGB:
        STROKECOLOR = (A*255,B*255,C*255)
    elif COLORMODE == HSB:
        STROKECOLOR.hsva = (A*360,B*100,C*100,D*100)

def nostroke():
    global STROKE
    STROKE = False



def nofill():
    global FILL
    FILL = False

#set the fill color
def fill(A,B=999,C=999,D=1):
    global FILLCOLOR, FILL
    FILL = True
    if B == 999:
        B = A
        C = A
    if A > 1:
        A = 1
    if B > 1:
        B = 1
    if C > 1:
        C = 1
    if A < 0:
        A = 0
    if COLORMODE == RGB:
        FILLCOLOR = Color(A*255,B*255,C*255,D*255)
    elif COLORMODE == HSB:
        FILLCOLOR.hsva = (A*360,B*100,C*100,D*100)

def oval(x,y,w,h):
    if FILL:
        pygame.draw.ellipse(SCREEN, FILLCOLOR, (x,y,w,h))
    if STROKE:
        pygame.draw.ellipse(SCREEN, STROKECOLOR, (x,y,w,h), STROKEWIDTH)

def rect(x,y,w,h):
    if FILL:
        pygame.draw.rect(SCREEN, FILLCOLOR, (x,y,w,h))
    if STROKE:
        pygame.draw.rect(SCREEN, STROKECOLOR, (x,y,w,h), STROKEWIDTH)

def line(x1,y1,x2,y2):
    if STROKE:
        pygame.draw.line(SCREEN,STROKECOLOR,[x1,y1],[x2,y2],STROKEWIDTH)

def random():
    return ra.random()
        
def strokewidth(w):
    global STROKEWIDTH
    STROKEWIDTH = int(w+0.5)

def speed(fps):
    global FPS
    FPS = fps

def animate(setup,draw):
    global FPS,FRAME,MOUSEX,MOUSEY,mousedown
    setup()
    if FPS == 0:
        draw()
        return
    while True:
        pygame.event.get()
        pressed = pygame.key.get_pressed()
        keypressed = 1 in pressed
        if pressed[K_q]:
            break
        MOUSEX,MOUSEY = pygame.mouse.get_pos()
        mousedown,md2,md3 = pygame.mouse.get_pressed()
        SCREEN.fill(BACKGROUND)
        draw()
        pygame.display.flip()    #裏画面に描かれたものを表示する。
        pygame.time.wait(1000//FPS)
        FRAME += 1


def wait_q():
    pygame.display.flip()    #裏画面に描かれたものを表示する。
    while True:
        pygame.event.get()
        pressed = pygame.key.get_pressed()
        if pressed[K_q]:
            break
        pygame.time.wait(100)

def fontsize(x):
    global _sysfont
    _sysfont = pygame.font.SysFont(u"helvetica", x)

def text(text,x,y):
    image = _sysfont.render(text, True, (0,0,0))
    w,h = image.get_size()
    SCREEN.blit(image, (x,y-h*0.8))
