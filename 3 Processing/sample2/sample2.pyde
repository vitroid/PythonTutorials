#setup()は最初に一回だけ実行されます。アニメーションの設定を行います。
def setup():
    size(500, 500, P3D)        #ウィンドウのサイズ。P3Dをつけると3次元モードに

#draw()で1コマを描きます。
def draw():
    background(255, 204, 0)    #背景を塗りつぶす色
    lights()                   #照明あり
    translate(308, 298, 0)     #座標をずらし、
    rotateY(frameCount/10.0)   #座標を回転させ、(frameCountはコマ番号)
    fill(200,250,200)
    stroke(126)
    box(40, 20, 50)            #そこに箱を描きます。
    line(0,0,0,100,100,100)
