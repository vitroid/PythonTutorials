#!/usr/bin/env python3

from sympy import sieve
from sympy.ntheory import factorint

for i in sieve.primerange(1, 1000):
    print(i)
    print(factorint(2**i-1))

