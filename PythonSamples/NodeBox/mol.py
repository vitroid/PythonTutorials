import math
#animation
speed(30)
size(10,10)

# d is a 2-element list
def force(d):
    dx = d[0]
    dy = d[1]
    r  = math.sqrt(dx**2 + dy**2)
    f  = -12.0 * r**-13 + 6.0 * r**-7
    fx = f * dx / r
    fy = f * dy / r
    return [fx,fy]


# d is a 2-element list
def potential(d):
    dx = d[0]
    dy = d[1]
    r  = math.sqrt(dx**2 + dy**2)
    ep = r**-12 - r**-6
    return ep


def totalkinetic(atoms):
    eksum = 0.0
    #accumulate velocity
    for i in range(len(atoms)):
        eksum = eksum + (atoms[i][1][0]**2 + atoms[i][1][1]**2) * atoms[i][3]
    return eksum / 2.0    


def totalpotential(atoms):
    epsum = 0.0
    for i in range(len(atoms)):
        mass  = atoms[i][3]
        #position of atom i
        xi = atoms[i][0][0]
        yi = atoms[i][0][1]
        for j in range(len(atoms)):
            #position of atom j
            xj = atoms[j][0][0]
            yj = atoms[j][0][1]
            if i != j:
                dx = xj - xi
                dy = yj - yi
                ep = potential( [dx,dy] )
                epsum = epsum + ep
        epsum = epsum + k * (xi**2+yi**2)
    return epsum / 2.0


def circle(x,y,r):
    oval(x-r,y-r,2*r,2*r)


# list of list of position, velocity, force, and mass.
# velocity of atom 3 is denoted by atoms[3][1]
# y component of the position of atom 2 is atomss[2][0][1]

atoms = [[[1.0,1.0],[2.0,1.0],[0.0,0.0],1.0],
         [[2.0,1.0],[-3.0,1.0],[0.0,0.0],1.0],
         [[3.0,1.0],[5.0,2.0],[0.0,0.0],1.0],
         [[4.0,1.0],[-7.0,3.0],[0.0,0.0],1.0],
         [[5.0,1.0],[11.0,5.0],[0.0,0.0],1.0]]    
dt = 0.01
k = 1.0
def draw():
    translate(WIDTH/2, HEIGHT/2)
    #accumulate position
    for i in range(len(atoms)):
        atoms[i][0][0] = atoms[i][0][0] + atoms[i][1][0] * dt * 0.5
        atoms[i][0][1] = atoms[i][0][1] + atoms[i][1][1] * dt * 0.5
    #calculate interaction
    for i in range(len(atoms)):
        #reset force
        fxsum = 0.0
        fysum = 0.0
        mass  = atoms[i][3]
        #position of atom i
        xi = atoms[i][0][0]
        yi = atoms[i][0][1]
        for j in range(len(atoms)):
            #position of atom j
            xj = atoms[j][0][0]
            yj = atoms[j][0][1]
            if i != j:
                dx = xj - xi
                dy = yj - yi
                fx,fy = force( [dx,dy] )
                fxsum = fxsum + fx
                fysum = fysum + fy
        atoms[i][2][0] = fxsum/mass - k * xi 
        atoms[i][2][1] = fysum/mass - k * yi
    #accumulate velocity
    for i in range(len(atoms)):
        atoms[i][1][0] = atoms[i][1][0] + atoms[i][2][0] * dt
        atoms[i][1][1] = atoms[i][1][1] + atoms[i][2][1] * dt
    #accumulate position
    for i in range(len(atoms)):
        atoms[i][0][0] = atoms[i][0][0] + atoms[i][1][0] * dt * 0.5
        atoms[i][0][1] = atoms[i][0][1] + atoms[i][1][1] * dt * 0.5
        circle(atoms[i][0][0], atoms[i][0][1], 0.2)
    epsum = totalpotential(atoms)
    eksum = totalkinetic(atoms)
    print epsum, eksum, epsum+eksum