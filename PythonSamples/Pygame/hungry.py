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


while True:
 up=1
 down=2
 right=3
 left=4
 step=20
 block=[20,20]
 x=randint(1,20)
 y=randint(2,22)
 applexy=[]
 snakexy=[int(x*20),int(y*20)]
 snakelist=[[x*20,y*20],[(x-20)*20,(y*20)]]
 apple=0
 dead=0
 grow=0
 direction=right
 score=0
 start=0


 pygame.init()
 screen=pygame.display.set_mode((640,480),0,24)
 caption=pygame.display.set_caption("Hungry Snake")
 f=pygame.font.SysFont("comicsansms",50)
 text1=f.render("Hungry Snake",True,(0,255,0))
 clock=pygame.time.Clock()
 start=pygame.font.SysFont("comicsansms",30)
 text2=start.render("Press s to start",True,(0,255,0))
 q=pygame.font.SysFont("comicsansms",30)
 text3=q.render("Press q to quit",True,(0,255,0))
 s=[[300,200],[280,200],[260,200],[240,200],[220,200],[200,200],[180,200],[180,220],[160,220],[140,220],[120,220],[120,240],[100,240]]
 a=[100,240]
 pygame.draw.rect(screen,(255,0,0),Rect(a,block),0)
 screen.blit(text1,(60,60))
 screen.blit(text2,(300,300))
 screen.blit(text3,(300,350))
 for i in s:
  pygame.draw.rect(screen,(0,255,0),Rect(i,block),0)
  pygame.display.flip()
  clock.tick(10)
 pygame.display.flip()


 while True:
  for i in pygame.event.get():
   if i.type==QUIT:
    exit()
  pressed=pygame.key.get_pressed()
  if pressed[K_q]:
   exit()
  if pressed[K_s]:
   break


 while not dead:
  for i in pygame.event.get():
   if i.type==QUIT:
    exit()
  pressed=pygame.key.get_pressed()
  if pressed[K_LEFT] and direction!=right:
    direction=left
  elif pressed[K_RIGHT] and direction!=left:
     direction=right
  elif pressed[K_UP] and direction!=down:
     direction=up
  elif pressed[K_DOWN] and direction!=up:
     direction=down
  if direction==right:
   snakexy[0]=snakexy[0]+step
   if snakexy[0]>620:
    dead=1

  elif direction==left:
   snakexy[0]=snakexy[0]-step
   if snakexy[0]<20:
    dead=1

  elif direction==up:
   snakexy[1]=snakexy[1]-step
   if snakexy[1]<20:
    dead=1
  elif direction==down:
   snakexy[1]=snakexy[1]+step
   if snakexy[1]>460:
    dead=1
  if snakelist.count(snakexy)>0:
   dead=1
  if apple==0:
   x1=randint(1,31)
   y1=randint(2,22)
   applexy=[int(x1*step),int(y1*step)]
   apple=1

  snakelist.insert(0,list(snakexy))
  if snakexy[0]==applexy[0] and snakexy[1]==applexy[1]:
   apple=0
   score=score+1
  else:
   snakelist.pop()

  screen.fill((0,0,0))
  scr=pygame.font.SysFont("comicsansms",20)
  text4=scr.render("Score : %d"%score,True,(0,255,0))
  screen.blit(text4,(500,10))
  pygame.draw.rect(screen,(255,0,0),Rect(applexy,block),0)
  for i in snakelist:
   pygame.draw.rect(screen,(0,255,0),Rect(i,block))
  pygame.display.flip()
  clock.tick(10)

 if dead==1:
  screen.fill((0,0,0))
  over=pygame.font.SysFont("comicsansms",40)
  text5=over.render("GAME OVER",True,(0,255,0))
  screen.blit(text5,(50,50))
  screen.blit(text4,(200,200))
  pygame.display.flip()
  while True:
   for i in pygame.event.get():
    if i.type==QUIT:
     exit()
   pressed=pygame.key.get_pressed()
   if pressed[K_q]:
    exit()
   if pressed[K_s]:
    break






















