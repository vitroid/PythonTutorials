import math
# NMDS
import codecs


stations = []
file = codecs.open("stations.txt","r", "utf-8")
for line in file:
    stations.append(line)
file.close()

#http://www.kotsu.city.osaka.jp/ct/other000003800/ryoukinkusuhyo_sankakuhyou.pdf

table = dict()
file = open("blocks.txt")
rows = 1
for line in file:
    line = line.split()
    for i in range(len(line)):
        if int(line[i]):
            table[(rows,98-i)] = int(line[i])
    rows += 1
file.close()

#remove randomly
#for i in table.keys():
#    if random() < 0.03:
#        del table[i]
    


def show(pos,label):
    fontsize(18)
    fill(0)
    for i in range(len(pos)):
        oval(pos[i][0]*15+500-2,pos[i][1]*15+500-2,4,4)
    fill(0, 0, 0, 0.5)
    for i in range(len(pos)):
        text(label[i],pos[i][0]*15+500,pos[i][1]*15+500)


def order( distance ):
    o = 0
    d = dict()
    lastd = 9999
    lasto = 0
    for i in sorted(distance.keys(), cmp=lambda x,y: cmp(distance[x],distance[y])):
        if distance[i] != lastd:
            lasto = o
        d[i] = lasto
        #d[i] = o
        lastd = distance[i]
        o += 1
    return d

def normalize(pos):
    sx = 0.0
    sy = 0.0
    for x,y in pos:
        sx += x
        sy += y
    sx /= len(pos)
    sy /= len(pos)
    for i in range(len(pos)):
        pos[i] = ( pos[i][0]-sx, pos[i][1]-sy )
    s = 0.0
    for x,y in pos:
        s += x**2+y**2
    s =  len(pos) / math.sqrt(s)
    for i in range(len(pos)):
        pos[i] = ( pos[i][0]*s, pos[i][1]*s )


oorder = order(table)

pos = []
for i in range(rows):
    pos.append((random()*400-200,random()*400-200))
size(1000,1000)
speed(10)

def draw():
    print FRAME
    normalize(pos)
    show(pos,stations)

    #for i in sorted(table.keys(), cmp=lambda x,y: cmp(table[x],table[y])):
    #    print i,table[i],oorder[i]

    distance = dict()
    for i,j in table.keys():
        #print i,j
        dx = pos[i][0] - pos[j][0]
        dy = pos[i][1] - pos[j][1]
        distance[(i,j)] = dx**2 + dy**2
    corder = order(distance)
    #print corder
    for key in table:
        i,j = key
        if i == 29 or j == 29:
            if table[key] == 1:
                print key,corder[key]

    diff = 0.0
    for i,j in table.keys():
        d = corder[(i,j)] - oorder[(i,j)]
        diff += d**2
        # if d<0: i,j should get farther
        dx = pos[i][0] - pos[j][0]
        dy = pos[i][1] - pos[j][1]
        pos[i] = ( pos[i][0]-dx*d*0.000003, pos[i][1]-dy*d*0.000003)
        pos[j] = ( pos[j][0]+dx*d*0.000003, pos[j][1]+dy*d*0.000003)
    fill(0)
    nostroke()
    fontsize(18)
    text("E=%f" % diff, 50,50)
