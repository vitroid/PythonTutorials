"""
アニメーションの例。

draw関数は一定周期で自動的に何度も呼ばれます。
background命令で画面を消去しなければ、どんどん
重ね描きされます。
"""

def setup():
    frameRate(30)
    size(500,500)

def draw():
    #background(100)
    dx = 30 + 20*cos(frameCount/10.0)
    dy = 30 - 20*cos(frameCount/10.0)
    x = 250 + 100*cos(frameCount/70.0)
    y = 250 + 100*sin(frameCount/70.0)
    ellipse(x,y,dx,dy)
