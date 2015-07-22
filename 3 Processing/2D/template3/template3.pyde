"""
重なっている場合には遠ざかろうとするが、
遠い場合には近づこうとする円盤。
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

def pull_neighbors(particles,diam1,diam2):
    for p1,p2 in it.combinations(particles,2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        d2 = dx**2 + dy**2
        if diam1**2 < d2 < diam2**2:
            d1 = sqrt(d2) * 10
            dx /= d1
            dy /= d1
            p1[2] += dx
            p1[3] += dy
            p2[2] -= dx
            p2[3] -= dy

def displace(particles):
    for p in particles:
        p[0] += p[2] * 1.0
        p[1] += p[3] * 1.0

def rearrange(particles, diam):
    reset_force(particles)
    avoid_overlap(particles, diam)
    pull_neighbors(particles, diam*1.1, diam*1.3)
    displace(particles)

def find_particle(x,y,particles,diam):
    target = None
    for p in particles:
        dx = x - p[0]
        dy = y - p[1]
        if dx**2 + dy**2 < diam**2 / 4.0:
            target = p
    return target

def mousePressed():
    global particles,diam
    x = mouseX
    y = mouseY
    target = find_particle(x,y,particles,diam)
    if target is None:
        particles.append([x,y,0,0])
    else:
        particles.remove(target)

def setup():
    global particles,diam
    size(500,500)
    particles = []
    diam = 100

def draw():
    global paticles,diam
    background(100)
    rearrange(particles, diam)
    for p in particles:
        ellipse(p[0],p[1],diam,diam)
