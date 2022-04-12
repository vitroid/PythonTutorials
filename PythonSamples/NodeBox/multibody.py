from math import *   #sqrt()関数のために必要。
speed(30)
size(400,400)
def circle(x,y,r):
    oval(x-r,y-r,r*2,r*2)


#2つの位置を引数とし、斥力(逆6乗)を計算する。
def Repulsion( pos1,pos2 ):
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    r = sqrt(dx**2+dy**2)
    f = 6.0 / r**8
    fx = f * dx
    fy = f * dy
    return [fx,fy]
    
#2つの位置を引数とし、ばね力を計算する。
def Spring( pos1,pos2 ):
    k = 5.0
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    r = sqrt(dx**2+dy**2)
    fx = -k * dx
    fy = -k * dy
    return [fx,fy]

#すべての物体の相互作用を計算し、加速度を求める。
def Force(objs):
    #物体の数
    n = len(objs)
    #それぞれの物体について
    for i in range(0,n):
        #i番目の物体に加わる力をfに積算する。
        f = [0.0,0.0]
        #外場から物体iに与えられる力は、ここで計算しておく。
        # x,y = objs[i][0]で座標をx,yに入れ、それを使って外場の力を求める。
        x,y = objs[i][0]
        dx = x - 20
        dy = y - 20
        r = sqrt(dx**2+dy**2)
        k = 0.4
        fx = -k * dx
        fy = -k * dy
        f = [fx,fy]
        #相手の物体それぞれについて
        for j in range(0,n):
            #自分自身とは相互作用しない
            if i != j:
                #i番目とj番目の物体の位置を渡し、
                #斥力を計算する。
                rep = Repulsion( objs[i][0], objs[j][0] )
                #repは力の成分
                f[0] += rep[0]
                f[1] += rep[1]
                #ばねの力は特定の組合せのみ。
                if ((i==0 and j==1) or
                    (i==1 and j==0) or
                    (i==1 and j==2) or
                    (i==2 and j==1)):
                    spr = Spring( objs[i][0], objs[j][0] )
                    f[0] += spr[0]
                    f[1] += spr[1]
        mass = objs[i][3]
        #加速度を計算する。
        ax = f[0] / mass
        ay = f[1] / mass
        #i番目の物体の2番目の属性=加速度
        objs[i][2] = [ax,ay]

#加速度を速度に加算する。
def Accel(objs,Dt):
    #物体の数
    n = len(objs)
    #それぞれの物体について
    for i in range(0,n):
        #リストのままで計算するとわかりにくいので、
        #一旦変数に出し、計算して、戻す。
        vx,vy = objs[i][1]
        ax,ay = objs[i][2]
        vx += ax * Dt
        vy += ay * Dt
        objs[i][1] = [vx,vy]

#速度を位置に加算する。
def Progress(objs,Dt):
    #物体の数
    n = len(objs)
    #それぞれの物体について
    for i in range(0,n):
        #リストのままで計算するとわかりにくいので、
        #一旦変数に出し、計算して、戻す。
        x,y = objs[i][0]
        vx,vy = objs[i][1]
        x += vx * Dt
        y += vy * Dt
        objs[i][0] = [x,y]

#物体を表示する。
def Show(objs,zoom):
    n = len(objs)
    #物体は円。
    for i in range(0,n):
        x,y = objs[i][0]
        circle(x*zoom,y*zoom,zoom/2)
    #ばねは線であらわす。
    #0-1, 1-2の間を線でつなぐ。
    stroke(0)
    line(objs[0][0][0]*zoom,objs[0][0][1]*zoom,
         objs[1][0][0]*zoom,objs[1][0][1]*zoom)
    line(objs[1][0][0]*zoom,objs[1][0][1]*zoom,
         objs[2][0][0]*zoom,objs[2][0][1]*zoom)
    
        
#アニメーションの初期化。    
def setup():
    #力学変数はみんなsetup()で初期化し、
    #draw()関数と共通に使えるようにする。
    global objs,Dt
    #前から順に、位置、速度、加速度、質量。
    objs = [[[10.0, 10.0], [0.0,0.0], [0.0,0.0], 1.0],
            [[13.0, 10.0], [0.0,0.0], [0.0,0.0], 1.0],
            [[11.0, 15.0], [0.0,0.0], [0.0,0.0], 1.0],
            [[11.0, 20.0], [0.0,0.0], [0.0,0.0], 1.0],
            [[11.0, 25.0], [0.0,0.0], [0.0,0.0], 1.0],
            [[11.0, 30.0], [0.0,0.0], [0.0,0.0], 1.0],
            [[11.0, 35.0], [0.0,0.0], [0.0,0.0], 1.0],
            [[11.0, 40.0], [0.0,0.0], [0.0,0.0], 1.0],]
    Dt = 0.01
#アニメーションの描画
def draw():
    global objs,Dt
    objs[0][0] = [MOUSEX/10.0, MOUSEY/10.0]
    #すべての物体に働く力を求め、加速度を計算する
    Force(objs)
    #すべての物体の速度を、Dtだけ進める。
    Accel(objs,Dt)
    #すべての物体の位置を、Dtだけ進める。
    Progress(objs,Dt)
    #すべての物体を表示する。
    Show(objs,zoom=10.0)