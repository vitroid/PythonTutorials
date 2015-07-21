# template for self-arranging connected particles
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
    
def find_particle_id(x,y,particles,diam):
    id = -1
    for i in range(len(particles)):
        p = particles[i]
        dx = x - p[0]
        dy = y - p[1]
        if dx**2 + dy**2 < diam**2 / 4.0:
            id = i
    return id
    
def mousePressed():
    global particles,diam,target_id
    x = mouseX
    y = mouseY
    target_id = find_particle_id(x,y,particles,diam)
    if target_id < 0:
        target = [x,y,0,0]
        target_id = len(particles)
        particles.append(target)
        
def mouseReleased():
    global particles,diam,connections,target_id
    x = mouseX
    y = mouseY
    dest_id = find_particle_id(x,y,particles,diam)
    if target_id != dest_id:
        connections.add((target_id,dest_id))


def setup():
    global particles,diam,connections
    size(500,500)
    particles = []
    connections = set()
    diam = 100

def draw():
    global paticles,diam,connections,target_id
    background(100)
    rearrange(particles, diam)
    for p in particles:
        ellipse(p[0],p[1],diam,diam)
    for con in connections:
        i,j = con
        line(particles[i][0],particles[i][1],
             particles[j][0],particles[j][1])
    if mousePressed:
        line(particles[target_id][0],
             particles[target_id][1],
             mouseX,
             mouseY)

