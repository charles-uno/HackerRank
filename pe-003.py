#!/usr/bin/env python3

"""
Charles McEachern
2018-04-17
https://projecteuler.net/problem=3
"""

import math

# ######################################################################

def main():
    print( max( factorize(600851475143) ) )

# ----------------------------------------------------------------------

def factorize(n):
    # Don't even bother checking evens.
    primes = []
    i = 1
    while n > 1:
        i += 2
        if any( i % p == 0 for p in primes ):
            continue
        # Looks like we found a prime!
        primes.append(i)
        # Divide out divisors. Watch out for degeneracy.
        while n % i == 0:
            n //= i
            yield i

# ######################################################################

if __name__ == '__main__':
    main()
