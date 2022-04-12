#sudoku solver
#
# 高速化したいなら、書き換えによって影響を受けるgroupだけを処理するようにするのが良い。(Hull, Laser)
# 今はまだ実証試験中なので速さは求めない。
# この程度のありきたりな解法だけでは、最も難しい数独は解けないことがわかった。推論が必要。推論の深さで難度が測れるとすれば、僕がこれまで解いてきた数独はどれも推論がほぼ不要だったので、「容易」と言わざるをえない。
# http://mohsho.image.coocan.jp/WH-Sudoku02.html
#
from nodebox_wrapper import *
import itertools as it

speed(30)
size(1000,1000)

def prepare_groups():
    # グループとは、1〜9の数字を入れるべき格子点のセットのこと。
    groups = []
    groups_at_node = dict()
    # Square groups
    for gx in range(3):
        for gy in range(3):
            group = []
            for px in range(3):
                for py in range(3):
                    group.append((gx*3+px, gy*3+py))
            groups.append(frozenset(group))
    # row groups
    for row in range(9):
        group = []
        for x in range(9):
            group.append((x,row))
        groups.append(frozenset(group))
    # column groups
    for column in range(9):
        group = []
        for y in range(9):
            group.append((column,y))
        groups.append(frozenset(group))
    # groups_at_nodeは、ある格子点が属しているgroup(3つ)を格納
    for group in groups:
        for node in group:
            groups_at_node[node] = set()
    for group in groups:
        for node in group:
            groups_at_node[node].add(group)
    return groups, groups_at_node


def drawmap(map,zoom):
    #thin lines
    strokewidth(1)
    stroke(0)
    nofill()
    for i in range(10):
        line(0,i*zoom,zoom*9,i*zoom)
        line(i*zoom,0,i*zoom,zoom*9)
    #thick lines
    strokewidth(3)
    stroke(0)
    nofill()
    for i in range(4):
        line(0,i*zoom*3,zoom*9,i*zoom*3)
        line(i*zoom*3,0,i*zoom*3,zoom*9)
    #put candidates
    nostroke()
    fontsize(zoom/3)
    for x in range(9):
        for y in range(9):
            if len(map[x][y]) == 1:
                fontsize(zoom)
                fill(0,0,0)
                memb = list(map[x][y])
                text("%s" % memb[0],(x+0.2)*zoom,(y+0.8)*zoom)
            else:
                fontsize(zoom/3)
                fill(0,0,0,0.5)
                for sx in range(3):
                    for sy in range(3):
                        s = sx+sy*3 + 1
                        if s in map[x][y]:
                            text("%s" % s,(x+sx/3.+0.05)*zoom,(y+(sy+1)/3.-0.05)*zoom)
    

def unsetvalues(x,y,values,map,queue):
    last = map[x][y]
    map[x][y] -= values
    # もし変化したら
    if frozenset(last) != frozenset(map[x][y]):
        # それにより要素が1個になったら
        if len(map[x][y])==1:
            # chain reaction
            solevalue = list(map[x][y])[0]
            queue.append(("set",x,y,solevalue))
            print("Collateral2",x,y,solevalue)
        
                
def setvalue(x,y,value,map,queue):
    """
    指定された格子点の値を設定する
    その格子点と同じグループのほかの格子点から値を排除する。
    """
    print("Set",x,y,value)
    valueset = frozenset([value])
    for group in groups_at_node[(x,y)]:
        for nx,ny in group:
            if (nx,ny) != (x,y):
                if len(map[nx][ny]) > 1:
                    queue.append(("unset",nx,ny,valueset))
    map[x][y] = valueset
        

def solitary(group,map,queue):
    """
    グループの中で一箇所にしか出てこない数字をさがす。
    """
    count = [0] * 10
    # group内でそれぞれの数字が何回出てくるか。
    undecidedgrids = [(x,y) for x,y in group if len(map[x][y])>1]
    for x,y in undecidedgrids:
        for memb in map[x][y]:
            count[memb] += 1
    print("Counts",group,count)
    for num in range(1,10):
        if count[num] == 1:
            for x,y in undecidedgrids:
                if num in map[x][y]:
                    #setvalue(x,y,num,map,queue)
                    queue.append(("set", x,y,num))
                    print("Solo",x,y,num,group)
                    for x,y in group:
                        print(x,y,map[x][y])
                    print()
                    



def nums_in_group(group, map):
    nums = set()
    for x,y in group:
        nums |= map[x][y]
    return nums
    
def laser(g1, g2, map, queue):
    """
    1. グループA,Bで共有している格子点(複数)に、ある数字が候補として含まれる
    2. その数字はグループAの残りの格子点では候補ではない。
    3. その場合、グループBの残りの格子点でも候補ではない。
    """
    commongrid = g1 & g2
    onlyg1grid = g1 - commongrid
    onlyg2grid = g2 - commongrid

    commonnums = nums_in_group(commongrid, map)
    onlyg1nums = nums_in_group(onlyg1grid, map)
    onlyg2nums = nums_in_group(onlyg2grid, map)
    for num in commonnums:
        if num not in onlyg1nums and num in onlyg2nums:
            print("Laser", commongrid, commonnums, num, onlyg2grid)
            # should not be in g2
            for x,y in onlyg2grid:
                unsetvalues(x,y,set([num]),map,queue)
        elif num not in onlyg2nums and num in onlyg1nums:
            print("Laser", commongrid, commonnums, num, onlyg1grid)
            for x,y in onlyg1grid:
                unsetvalues(x,y,set([num]),map,queue)


                
def hull(group, map, queue):
    """
    あるグループの中で、n個の格子点がn個の数字を候補とする場合。
    同じグループのほかの格子点はそれらの数字を候補とできない。
    """
    undecidedgrids = [(x,y) for x,y in group if len(map[x][y])>1]
    N = len(undecidedgrids)
    for i in range(2,N):
        for g1 in it.combinations(undecidedgrids, i):
            nums = nums_in_group(g1, map)
            if len(nums) == i:
                # i grids share i nums
                # remove them from other grids
                print("Hull", g1, nums, N)
                g2 = set(undecidedgrids) - set(g1)
                for x,y in g2:
                    unsetvalues(x,y,set(nums),map,queue)
                
def clean(group, map,queue):
    """
    unsetの結果soloになった格子があれば、他の格子からその数字を消す。
    """
    for x,y in group:
        if len(map[x][y])==1:
            print("Clean",x,y,map[x][y])
            for nx,ny in group:
                if (x,y) != (nx,ny):
                    unsetvalues(nx,ny,map[x][y],map,queue)
    

def digest_queue(queue,map,mode):
    global groups
    while len(queue) > 0:
        command, x,y, value = queue.pop()
        print("Digest",command, x,y,value)
        if command == "set":
            setvalue(x,y,value,map,queue)
            break
        elif command == "unset":
            unsetvalues(x,y,value,map,queue)
            

map26 = [".8.4.6...",
         ".....876.",
         ".459.....",
         ".....3..9",
         "1.......3",
         "5..6.....",
         ".....912.",
         ".697.....",
         "...3.4.7.",]

map9x9g1_1 = ["7..2.....",
              "......5.3",
              "..4.3....",
              "2.69...3.",
              ".7...58..",
              "...6....4",
              ".3.......",
              "....4..7.",
              "..9...62."]
                  
hardest=["8........",
         "..36.....",
         ".7..9.2..",
         ".5...7...",
         "....457..",
         "...1...3.",
         "..1....68",
         "..85...1.",
         ".9....4.."]

def easy_setup(mapx):
    queue = list()
    for row in range(9):
        for col in range(9):
            if mapx[col][row] in "123456789":
                queue.append(("set", row,col,int(mapx[col][row])))
    return queue


def setup():
    global cursor,map,zoom,queue,mode, groups, groups_at_node
    groups, groups_at_node = prepare_groups()
    cursor = None
    map = [[set([1,2,3,4,5,6,7,8,9]) for i in range(9)] for j in range(9)]
    zoom = 60 #size of one square
    queue = set()
    colormode(HSB)
    mode = 0
    #queue = easy_setup(map9x9g1_1)
    #queue = easy_setup(map26)
    queue = easy_setup(hardest)
        
    
def draw():
    global cursor,map,zoom,queue,mode,groups
    digest_queue(queue,map,mode)
    #for group in groups:
    #    solitary(group,map,queue)
    if len(queue) == 0:
        for g1,g2 in it.combinations(groups,2):
            if len(g1 & g2) > 1:
                laser(g1,g2,map,queue)
        for group in groups:
            clean(group,map,queue)
            hull(group,map,queue)
    drawmap(map,zoom)
    print(FRAME,mode,queue,len(queue))
    x=input()
    

animate(setup,draw)
