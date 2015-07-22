"""
自己回避円盤: マウスを押した場所に円盤が描かれます。
円盤は、互いが重ならないように、にじり動きます。
"""
import itertools as it

def reset_force(particles):
    for p in particles:
        p[2] = 0
        p[3] = 0

def avoid_overlap(particles,diam):
    for p1,p2 in it.combinations(particles,2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        d2 = dx**2 + dy**2
        if d2 < diam**2:
            d1 = sqrt(d2)
            dx /= d1
            dy /= d1
            p1[2] -= dx
            p1[3] -= dy
            p2[2] += dx 
            p2[3] += dy

def displace(particles):
    for p in particles:
        p[0] += p[2] * 1.0
        p[1] += p[3] * 1.0

def rearrange(particles, diam):
    reset_force(particles)
    avoid_overlap(particles, diam)
    displace(particles)

def find_particle(x,y,particles,diam):
    target = None
    for p in particles:
        dx = x - p[0]
        dy = y - p[1]
        if dx**2 + dy**2 < diam**2 / 4.0:
            target = p
    return target

#マウスが押されると呼ばれる特別な関数。
def mousePressed():
    global particles,diam,target
    x = mouseX
    y = mouseY
    target = find_particle(x,y,particles,diam)
    if target is None:
        target = [x,y,0,0]
        particles.append(target)
    else:
        particles.remove(target)

#最初に1度だけ呼ばれる関数
def setup():
    global particles,diam
    size(500,500)
    particles = []
    diam = 100

#フレームごとに呼ばれる関数
def draw():
    global paticles,diam
    background(100)
    rearrange(particles, diam)
    for p in particles:
        ellipse(p[0],p[1],diam,diam)
