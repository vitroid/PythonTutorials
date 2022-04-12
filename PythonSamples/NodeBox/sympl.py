from math import *   #sqrt()関数のために必要。
speed(30)
size(400,400)
def circle(x,y,r):
    oval(x-r,y-r,r*2,r*2)
def setup():
    #力学変数はみんなsetup()で初期化し、
    #draw()関数と共通に使えるようにする。
    global x,y,vx,vy,Dt,k,m,fx,fy
    x = 0.0
    y = 0.0
    vx = 0.0
    vy = 0.0
    Dt = 0.1
    k = 1.0
    m = 1.0
    fx = 0.0
    fy = 0.0
def draw():
    global x,y,vx,vy,Dt,k,m,fx,fy
    #速度を成分ごとに積分する
    vx = vx + fx / m * Dt * 0.5
    vy = vy + fy / m * Dt * 0.5

    #位置を成分ごとに積分する
    x = x + vx * Dt
    y = y + vy * Dt

    #相対位置の計算
    dx = x - MOUSEX
    dy = y - MOUSEY
    #距離の計算
    r = sqrt(dx**2+dy**2)
    #バネの力は距離に比例
    f = -k * r
    #力ベクトルを求める。
    fx = f * dx / r
    fy = f * dy / r
    #速度を成分ごとに積分する
    vx = vx + fx / m * Dt * 0.5
    vy = vy + fy / m * Dt * 0.5
    #ポテンシャルエネルギー
    Epot=k*r**2 / 2.0
    #運動エネルギー
    Ekin=m*(vx**2+vy**2) / 2.0

    #円を描く
    circle(x,y,10)
    #ポテンシャルと運動エネルギーの和を表示する。
    fontsize(14)
    text("%s" % (Epot+Ekin),0,10)