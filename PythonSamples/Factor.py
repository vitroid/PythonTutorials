#!/usr/bin/env python3

from bitarray import bitarray

primes = [2]


#list the primes upto y
def eratos(y):
    x = primes[-1]
    isPrime = bitarray(y-x)
    print("Allocate",y-x)
    isPrime.setall(1)
    print("Done.")
    #mark the known primes
    for p in primes:
        print("known primes:",p)
        xm = x % p
        x0 = x - xm + p
        for i in range(x0,y,p):
            isPrime[i-x] = 0
    tmax = int(y**0.5)
    for v in range(x+1,tmax+1):
        if isPrime[v-x]:
            primes.append(v)
            print("new prime:",v)
            for w in range(v+v,y,v):
                isPrime[w-x] = 0
    for v in range(tmax+1,y):
        if isPrime[v-x]:
            primes.append(v)


def _test_eratos():
    eratos(10)
    print(primes,len(primes))
    eratos(100)
    print(primes,len(primes))
    eratos(1000)
    print(primes,len(primes))
    eratos(10000)
    print(len(primes))

#_test_eratos()

def factor(x):
    maxprime = primes[-1]
    i = 0
    f = []
    while i < len(primes):
        p = primes[i]
        while x % p == 0:
            f.append(p)
            x //= p
        i += 1
    if maxprime**2 < x:
        eratos(x)
        return f + factor(x)
    if x != 1:
        f.append(x)
    return f

def product(L):
    x = 1
    for v in L:
        x *= v
    return x


for i in range(2,63):
    x = 2**i - 1
    f = factor(x)
    print(i,x,product(f),f)

#Note: factorint(x) in sympy is insanely fast.  Simply use it.
