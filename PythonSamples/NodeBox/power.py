# まず、可能な分割のしかたをリストする。
# x^9を(x^4)*(x^3)*(x^2)に分割できることを、diviでは[4,3,2]と表記する。
# x^9を(x^3)*(x^3)*(x^3)に分割できることを、diviでは[3,3,3]と表記する。
def divi(n,max=0):
    if n==0:
        return []
    if n==1:
        return [[1]]
    if max == 0:
        max = n-1
    elif n < max:
        max = n-1
    combi = []
    for i in range(1,max+1):
        left = i
        right = divi(n-i,max=i)
        for r in right:
            combi.append( [left] + r )
    return combi
# x^9を(x^4)*(x^3)*(x^2)に分割できることを、div2では[0,0,1,1,1]と表記する。
# x^9を(x^3)*(x^3)*(x^3)に分割できることを、div2では[0,0,0,3]と表記する。
def div2(n,max=0):
    if n==0:
        return [[]]
    if n==1:
        return [[0,1]]
    if max == 0:
        max = n-1
    elif n < max:
        max = n-1
    combi = []
    for i in range(1,max+1):
        left = i
        right = div2(n-i,max=i)
        for r in right:
            dup = list(r)
            m = len(dup)
            if m <= left:
                for i in range(m,left+1):
                    dup.append(0)
            dup[left] += 1
            combi.append( dup )
    return combi

print divi(9)
print
print div2(9)
print

#小さいnから順に、x^nに必要なかけ算回数を数え、count[]に入れていく。
#大きいnを数える際に、小さいnのcount[]が必要になるから。
count = [0] * 100
count[1] = 0
#2から順に40まで
for i in range(2,40):
    #まず、すべての分割方法をdiv2形式で得る(これに時間がかかる)
    combi = div2(i)
    #かけ算回数の最小値候補
    min = 1000
    #最小値での、分割内容(div2形式)
    minc = []
    for c in combi:
        sum = -1
        for j in range(1,len(c)):
            if c[j] > 0:
                #count[j]はx^jを計算するために必要なかけ算の回数の最小値。
                #それをc[j]乗するにはさらにc[j]-1回の乗算が必要。
                #cのほかの要素との掛けあわせにさらに1回必要。
                sum += (c[j]-1) + count[j] + 1
        #sum最小の組合せを探し、記憶する。
        if sum < min:
            min = sum
            minc = c
            #print i,min,c
    #最小値をcount[i]に覚えておく。
    count[i] = min
    print i,min,minc