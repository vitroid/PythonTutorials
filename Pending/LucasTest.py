# リュカ–レーマー・テスト
# p が奇素数のとき、メルセンヌ数 M_p = 2^p − 1 が素数となるための必要十分条件は、S_0 = 4, S_n = S_{n−1}^2 − 2 (n ≧ 1) と定義したときに S_{p−2} が M_p で割り切れることである。

from functools import lru_cache
import time
import sys
sys.setrecursionlimit(20000)

def primes():
    p = []
    x = 2
    while True:
        for y in p:
            if x % y == 0:
                break
        else:
            # print(p)
            p.append(x)
            yield(x)
        x += 1

@lru_cache
def S(n):
    if n == 0:
        return 4
    return S(n-1)**2 - 2

@lru_cache
def Sm(n, M):
    if n == 0:
        return 4
    return (Sm(n-1, M)**2 - 2) % M

@lru_cache
def Sm2(n, p):
    x = 4
    M = (1<<p) - 1
    for i in range(n):
        x = x**2 - 2
        x = (x >> p) + (x & M)
        x = (x >> p) + (x & M)
    if x == M:
        return 0
    return x


@lru_cache
def M(p):
    return 2**p - 1


def benchmark():
    Mp = []
    now = time.time()
    for p in primes():
        # if S(p-2) % M(p) == 0:      # 能天気な方法 30秒で6個
        # if Sm(p-2, M(p)) == 0:      # M_pの剰余系で計算する方法 同17個
        if Sm2(p-2, p) == 0:          # 2^p-1の剰余系で二進計算する方法 同19個
            Mp.append(p)
            print(time.time() - now, len(Mp), p)
    # 6.9141387939453125e-06 1 3
    # 3.719329833984375e-05 2 5
    # 4.506111145019531e-05 3 7
    # 6.103515625e-05 4 13
    # 7.295608520507812e-05 5 17
    # 8.511543273925781e-05 6 19
    # 0.00013113021850585938 7 31
    # 0.00031113624572753906 8 61
    # 0.0005559921264648438 9 89
    # 0.0007779598236083984 10 107
    # 0.0009710788726806641 11 127
    # 0.017242908477783203 12 521
    # 0.023930788040161133 13 607
    # 0.15041303634643555 14 1279
    # 0.8014321327209473 15 2203
    # 0.9136431217193604 16 2281
    # 3.0900449752807617 17 3217
    # 8.94567084312439 18 4253
    # 10.044462203979492 19 4423
    # 153.45290112495422 20 9689
    # 168.54608988761902 21 9941
    # 248.71342492103577 22 11213
    # 1871.0793900489807 23 19937
    # 2503.0759501457214 24 21701
    # 3182.565710067749 25 23209

def singleTest(p):
    now = time.time()
    print(Sm2(p-2, p) == 0)          # 2^p-1の剰余系で二進計算する方法 同19個
    print(time.time() - now)


if __name__ == "__main__":
    # benchmark()
    singleTest(23209) # 26; 4.865521192550659 sec Apple M1
    singleTest(44497) # 27; 25.91580867767334 sec
    singleTest(86243) # 28; 143.44582796096802 sec
