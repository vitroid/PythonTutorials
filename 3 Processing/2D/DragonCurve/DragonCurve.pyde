"""
長い紙テープを準備します。これを半分に折り、さらに
半分に折り、また半分に折ってから、
折り目をすべて90度にひらくと、どんな形になるでしょ
うか。
"""

Right, Left = +85, -95

def dup(tape):
    newtape = []
    for fold in tape:
        newtape.append(fold)
    newtape.append(Right)
    for fold in reversed(tape):
        newtape.append(-fold)
    return newtape

tape = [Right]
tape = dup(tape)
tape = dup(tape)
tape = dup(tape)
tape = dup(tape)
tape = dup(tape)
tape = dup(tape)
#print(tape)

size(500,500)
pi = 3.14159
angle = 45
x,y = 250,250

#turtle graphics
def forward(x,y,angle,L):
    return x + L*cos(angle * pi / 180), y + L*sin(angle * pi / 180)

newx,newy = forward(x,y,angle,10)
line(x,y,newx,newy)
x,y = newx,newy

for fold in tape:
    angle += fold
    newx,newy = forward(x,y,angle,10)
    line(x,y,newx,newy)
    x,y = newx,newy
