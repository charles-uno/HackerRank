#!/usr/bin/env python3

"""
Charles McEachern
2018-04-20
https://projecteuler.net/problem=12
"""

import numpy as np

import helpers

# ######################################################################

def main():
    n = 0
    while True:
        n += 1
        tri = n*(n+1)//2
        # Right off the bat, we can break a triangular number into two
        # smaller factors. This should make it quicker to factorize.
        if n % 2 == 0:
            factors = factorize(n//2) + factorize(n+1)
        else:
            factors = factorize(n) + factorize(n//2+1)
        # If n contains 2 powers of 17, that's 3 options: 17^0, 17^1,
        # 17^2. And all prime factors are independent, of course.
        ndivisors = np.prod( [ x+1 for x in value_counts(factors).values() ] )
        if ndivisors > 500:
            print(n, ':', tri, ':', ndivisors)
            break
    return

# ----------------------------------------------------------------------

FACTORS = {}

def factorize(n):
    """We can save a bit of time by remembering factors."""
    global FACTORS
    if n not in FACTORS:
        FACTORS[n] = list( factorize_many(n) )
    return FACTORS[n]

# ----------------------------------------------------------------------

# Don't want to bother checking for empty lists.
PRIMES = [2]

def factorize_many(n):
    """If we're factoring a ton of numbers -- or, really, anything in
    ascending order -- it's faster to remember primes as we find them.
    """
    global PRIMES
    # First, check primes that we have encountered in the past.
    for p in PRIMES:
        while n % p == 0:
            n //= p
            yield p
    # Now check for additional primes. Note that we stores primes in
    # ascending order, so the last one is the largest.
    i = PRIMES[-1]
    while n > 1:
        i += 1
        if any( i % p == 0 for p in PRIMES ):
            continue
        # Looks like we found another prime!
        PRIMES.append(i)
        # Now check if it's a divisor.
        while n % i == 0:
            n //= i
            yield i

# ----------------------------------------------------------------------

def value_counts(seq):
    return { x:seq.count(x) for x in set(seq) }

# ######################################################################

if __name__ == '__main__':
    main()
