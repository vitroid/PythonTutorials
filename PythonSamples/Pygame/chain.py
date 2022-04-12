#coding: utf-8
from pygame import *
from pygame.locals import *
screen=display.set_mode((400,400),0,24)
white=Color(255,255,255)
black=Color(0,0,0)

N = 5
k = 10.0
m = 1.0
r = [(0.0,0.0)]*(N+2)
v = [(0.0,0.0)]*(N+2)
dt = 0.02

x,y = mouse.get_pos()
for i in range(N+2):
    r[i] = (x*i/(N+1),y*i/(N+1))


while True:
    event.get()
    pressed = key.get_pressed()
    if pressed[K_q]:
        break
    x,y = mouse.get_pos()
    r[N+1] = (x,y)
    F = [(0.0,0.0)]*(N+2)
    for i in range(N+1):
        dr = (r[i+1][0] - r[i][0],  r[i+1][1] - r[i][1])
        fx = k * dr[0]
        fy = k * dr[1]
        F[i]   = (F[i][0] + fx, F[i][1] + fy)
        F[i+1] = (F[i+1][0] - fx, F[i+1][1] - fy)
    for i in range(1,N+1):
        a = (F[i][0] / m, F[i][1] / m)
        v[i] = (v[i][0]+dt*a[0], v[i][1]+dt*a[1])
        r[i] = (r[i][0]+dt*v[i][0], r[i][1]+dt*v[i][1])
    screen.fill(white)
    for i in range(0,N+1):
        draw.line(screen, black, (r[i][0],r[i][1]), (r[i+1][0],r[i+1][1]), 1)
    for i in range(1,N+1):
        draw.circle(screen, black, (r[i][0],r[i][1]), 40, 3)
    display.flip()
    time.wait(20)
