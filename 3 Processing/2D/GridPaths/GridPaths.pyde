"""
京都や札幌のような碁盤目の街路で、北西の端から南東の
端まで移動する最短経路は何通りあるかを可視化します。

重複順列の機能はitertoolsに含まれていないので、イン
ターネットでさがしてきました。
"""

#Taken from http://stackoverflow.com/questions/6284396/permutations-with-unique-values
def unique_permutations(elements):
    if len(elements) == 1:
        yield (elements[0],)
    else:
        unique_elements = set(elements)
        for first_element in unique_elements:
            remaining_elements = list(elements)
            remaining_elements.remove(first_element)
            for sub_permutation in unique_permutations(remaining_elements):
                yield (first_element,) + sub_permutation

def fac(x):
    if x <= 1:
        return 1
    return x*fac(x-1)

cityx = 8
cityy = 5
print fac(13)/fac(5)/fac(8)
pix   = 100
pixh  = pix / 2
right = 0
down  = 1
aroute = [right]*cityx + [down]*cityy

routes = []
for r in unique_permutations(aroute):
    routes.append(r)

def setup():
    size((cityx+1)*pix,(cityy+1)*pix)
    #frameRate(3)

def draw():
    if frameCount < len(routes):
        background(0) #black
        fill(255)
        noStroke()
        textSize(24)
        text("{0}".format(frameCount+1),10,20)
        noFill()
        stroke(200)   #gray
        strokeWeight(1)  #thin
        #draw grid lines
        for i in range(cityx+1):
            line(i*pix+pixh, pixh, i*pix+pixh, cityy*pix+pixh)
        for i in range(cityy+1):
            line(pixh, i*pix+pixh, cityx*pix+pixh, i*pix+pixh)
        #draw a route
        stroke(255,0,0)   #red
        strokeWeight(5)   #thick
        route = routes[frameCount]
        x = pixh
        y = pixh
        for i in route:
            if i == right:
                newx = x + pix
                newy = y
            else:
                newx = x
                newy = y + pix
            line(x,y,newx,newy)
            x,y = newx,newy
    else:
        noLoop()
