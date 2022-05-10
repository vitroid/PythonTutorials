# リュカ–レーマー・テスト
# p が奇素数のとき、メルセンヌ数 M_p = 2^p − 1 が素数となるための必要十分条件は、S_0 = 4, S_n = S_{n−1}^2 − 2 (n ≧ 1) と定義したときに S_{p−2} が M_p で割り切れることである。

import gmpy2
from functools import lru_cache
from LucasTest import primes
import time
import sys

@lru_cache
def LucasTest(n, p):
    x = gmpy2.mpz(4)
    M = (1<<p) - 1
    for i in range(n):
        x = x**2 - 2
        x = (x >> p) + (x & M)
        x = (x >> p) + (x & M)
    return x == M


def isMersennePrime(p):
    return LucasTest(p-2, p)


def benchmark(p=0):
    if p > 0:
        now = time.time()
        print(isMersennePrime(p))      # 2^p-1の剰余系で二進計算する方法 同19個
        print(p, time.time() - now)
        return
    Mp = []
    for p in primes():
        now = time.time()
        if isMersennePrime(p):          # 2^p-1の剰余系で二進計算する方法 同19個
            Mp.append(p)
            print(p, time.time() - now)


if __name__ == "__main__":
    # benchmark()
    # benchmark(23209) # 26; 0.5093061923980713 sec Apple M1
    # benchmark(44497) # 27; 1.9888668060302734 sec
    # benchmark(86243) # 28; 9.635300874710083 sec めちゃ速だけどこれでも並列処理ではないようだ。
    # benchmark(216091) # 31; 73.81052112579346 sec
    benchmark(756839) # 32; 
    # benchmark(1257787) # 34; infinite.
