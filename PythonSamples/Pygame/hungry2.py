#! /usr/bin/env python
############################################################################
# Purpose : A very small,basic and my first game
# Usages : Learning purpose
# Start date : 12/04/2011
# End date : 14/04/2011
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# Version : 0.0.1
# Modification history : No modification yet
############################################################################

import pygame
from  pygame.locals import *
from sys import exit
from random import randint
from math import *

def putanapple(map,width,height):
    while True:
        apple = (randint(0,width-1),randint(0,height-1))
        if map[apple] == 0:
            return apple

def scores(score,high):
    scr=pygame.font.SysFont("comicsansms",20)
    text4=scr.render("Score   : %d"%score,True,(255,255,255))
    screen.blit(text4,(zoom*25,zoom))
    text4=scr.render("HiScore : %d"%high,True,(255,255,255))
    screen.blit(text4,(zoom*25,zoom*2))
def draw(snake,apples,zoom,hiscore,time):
    block=(zoom+3,zoom+3)
    screen.fill((0,0,0))
    for x,y in apples:
        pygame.draw.rect(screen,(255,0,0),Rect((x*zoom,y*zoom),block))
    #time -= len(snake)
    #time += 1
    for x,y in snake:
        c = 5.0*cos(time*0.7)
        s = 5.0*sin(time*0.7)
        pygame.draw.rect(screen,(0,255,0),Rect((x*zoom+c,y*zoom+s),block))
        time += 1
    scores(len(snake),hiscore)



def onegame(width,height,zoom,hiscore):
    map=dict()
    time = 0
    for x in range(width):
        for y in range(height):
            map[(x,y)] = 0
    snake=[(10,10),(11,10)]
    map[(10,10)] = 1
    map[(11,10)] = 1
    velo =(1,0)
    apples = dict()
    for i in range(350):
        apple = putanapple(map,width,height)
        apples[apple] = 1
        map[apple] = 2

    while True:
        time += 1
        x,y = pygame.mouse.get_pos()
        #print x,y
        now = pygame.time.get_ticks()
        for i in pygame.event.get():
            if i.type==QUIT:
                exit()
        pressed=pygame.key.get_pressed()
        newv = velo
        if pressed[K_LEFT]:
            newv=[-1,0]
        elif pressed[K_RIGHT]:
            newv=[1,0]
        elif pressed[K_UP]:
            newv=[0,-1]
        elif pressed[K_DOWN]:
            newv=[0,1]
        if not (newv[0] == -velo[0] and newv[1] == -velo[1]):
            velo = newv
        progress = (snake[-1][0]+velo[0], snake[-1][1]+velo[1])
        if not map.has_key(progress):
            return len(snake)
        if map[progress] == 1:
            return len(snake)
        if map[progress] == 2:
            del apples[progress]
            apple = putanapple(map,width,height)
            map[apple] = 2
            apples[apple] = 1
        else:
            tail = snake.pop(0)
            map[tail] = 0
        snake.append(progress)
        map[progress] = 1

        draw(snake,apples,zoom,hiscore,time)
        pygame.display.flip()
        while pygame.time.get_ticks() < now + 100:
            pygame.time.wait(1)
    
pygame.init()
zoom=24
width=32
height=24
screen=pygame.display.set_mode((zoom*width,zoom*height),0,24)
caption=pygame.display.set_caption("Hungry Snake")
hiscore = 2
while True:
    score = onegame(width,height,zoom,hiscore)
    if score > hiscore:
        hiscore = score
    scr=pygame.font.SysFont("comicsansms",zoom)
    for i in range(3):
        screen.fill((0,0,0))
        scores(score,hiscore)
        text4=scr.render("Start in %s seconds" % (3-i),True,(0,255,0))
        screen.blit(text4,(width/2*zoom,height/2*zoom))
        pygame.display.flip()
        pygame.time.wait(1000)
