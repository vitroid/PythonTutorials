#ライブラリを使う場合はここに並べます。
from math import sin, cos
#キャンバスの大きさ=movieファイルの大きさ。
size(400,400)
#毎秒最大何フレーム表示するか。これを指定するとアニメーションとみなされる。
speed(30)
#⌘.(ピリオド)を押して止めるまで更新しつづける。

#setupは最初に一度だけ実行される関数。
#ここでは、全フレームで共通に使う(global)変数cntに初期値0を入れている。
def setup():
    global cnt,positions,cx,cy,vx,vy, dt,mass
    cnt = 0.0
    vx = 0.0
    vy = 0.0
    cx = 1.0
    cy = 1.0
    positions=[[cx,cy,10.0]]
    dt = 0.1
    mass = 0.3
#1フレームを描く関数。
def draw():
    #色モードを指定。
    colormode(HSB)
    global cnt,positions,cx,cy,vx,vy,dt,mass
    translate(200,200)
    #マウス位置と円の位置の差
    mx = MOUSEX - 200
    my = MOUSEY - 200
    deltax = mx - cx
    deltay = my - cy
    #マウスの方向に加わる力
    forcex = deltax * 0.1
    forcey = deltay * 0.1
    #速度は加速度の積分。
    vx = vx + forcex / mass * dt
    vy = vy + forcey / mass * dt
    #座標は速度の積分
    cx = cx + vx * dt
    cy = cy + vy * dt
    stroke(0,0,0)
    nofill()
    line(cx,cy,mx,my)
    #cntを増やす。
    if FRAME % 5 == 0:
        positions.insert(0,[cx,cy,10.0])
    cnt += 0.01
    if cnt > 1:
        cnt = cnt - 1.0
    #cntの値で色を変える。
    for i in positions:
        #fill(cnt, 1.0-0.1*i, 1)
        x = i[0]
        y = i[1]
        r = i[2]
        #rint x,y,r,i
        oval(x-r,y-r,r*2,r*2)
        i[0] *= 1.03
        i[1] *= 1.03
        i[2] *= 1.03
        if i[0]**2 + i[1]**2 > 300*300:
            positions.remove( i )
            
