#ライブラリを使う場合はここに並べます。
from math import sin, cos
#キャンバスの大きさ=movieファイルの大きさ。
size(600,600)
#毎秒最大何フレーム表示するか。これを指定するとアニメーションとみなされる。
speed(30)
#⌘.(ピリオド)を押して止めるまで更新しつづける。

#setupは最初に一度だけ実行される関数。
#ここでは、全フレームで共通に使う(global)変数cntに初期値0を入れている。
def setup():
    global cnt,x,y,vx,vy, dt,mass
    cnt = 0.0
    x = 0.0
    y = 0.0
    vx = 0.0
    vy = 0.0
    dt = 0.1
    mass = 0.3
#1フレームを描く関数。
def draw():
    #色モードを指定。
    colormode(HSB)
    global cnt,x,y,vx,vy,dt
    #マウス位置と円の位置の差
    deltax = MOUSEX - x
    deltay = MOUSEY - y
    #マウスの方向に加わる力
    forcex = deltax * 0.1
    forcey = deltay * 0.1
    #速度は加速度の積分。
    vx = vx + forcex / mass * dt
    vy = vy + forcey / mass * dt
    #座標は速度の積分
    x = x + vx * dt
    y = y + vy * dt
    #cntを増やす。
    cnt += 0.01
    if cnt > 1:
        cnt = cnt - 1.0
    #cntの値で色を変える。
    fill(cnt, 1.0, 0.8)
    oval(x,y,20,20)
    stroke(0,0,0)
    line(x+10,y+10,MOUSEX,MOUSEY)
