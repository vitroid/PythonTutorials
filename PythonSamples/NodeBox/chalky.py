from math import *   #sqrt()関数のために必要。
speed(30)
size(400,400)
def circle(x,y,r):
    oval(x-r,y-r,r*2,r*2)
def setup():
    #力学変数はみんなsetup()で初期化し、
    #draw()関数と共通に使えるようにする。
    global x,y,vx,vy,Dt,m,inter,k,r0
    x = [1,2,3,4,5,6,7,8]
    y = [1,2,3,4,5,6,7,8]
    vx = [0.0] * 8
    vy = [0.0] * 8
    Dt = 0.1
    m = [1.0] * 8
    k = 1.0
    r0 = 30.0
    inter = [[0,1],[0,2],[1,2],[1,3],[1,4],[2,4],[2,5]
             ,[3,4],[4,5],[3,6],[4,6],[4,7],[5,7],
             [6,7] ]
def draw():
    global x,y,vx,vy,Dt,k,m,inter,r0
    x[0] = MOUSEX
    y[0] = MOUSEY
    fx = [0.0] * 8
    fy = [0.0] * 8
    for i,j in inter:
        #相対位置の計算
        dx = x[i] - x[j]
        dy = y[i] - y[j]
        #距離の計算
        r = sqrt(dx**2+dy**2)
        #バネの力は距離に比例
        f = -k * (r - r0)
        #力ベクトルを求める。
        xf = f * dx / r
        yf = f * dy / r
        fx[i] += xf
        fy[i] += yf
        fx[j] -= xf
        fy[j] -= yf
    for i in range(0,8):
        #速度を成分ごとに積分する
        vx[i] = vx[i] + fx[i] / m[i] * Dt
        vy[i] = vy[i] + fy[i] / m[i] * Dt
        #位置を成分ごとに積分する
        x[i] = x[i] + vx[i] * Dt
        y[i] = y[i] + vy[i] * Dt
        #円を描く
        circle(x,y,10)