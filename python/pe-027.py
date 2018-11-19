#!/usr/bin/env python3

"""
Charles McEachern
2018-11-07
https://projecteuler.net/problem=27

Euler discovered the remarkable quadratic formula:
    n**2+n+41
It turns out that the formula will produce 40 primes for the consecutive
integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is
divisible by 41, and certainly when n=41,412+41+41 is clearly divisible
by 41.

The incredible formula n**2−79n+1601 was discovered, which produces 80
primes for the consecutive values 0≤n≤79. The product of the
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n**2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
    e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n=0.
"""

import helpers

# ######################################################################

PRIMES = None

def main():
    global PRIMES
    # Pretty sure a can be any number. That means -1000 to 1000,
    # skipping zero.
    avals = set( range(-1000, 1001) ) - {0}
    # Clearly b needs to be prime, and thus positive, since otherwise
    # n=0 gives a nonprime.
    bvals = list( helpers.primes_upto(1000) )
    # Also we can get a sense for how large these primes are going to
    # get. Both a and b are capped at 1000, and we know n == b is not
    # prime, so the maximum we could possibly hit is just over two
    # million: 1000**2 + 1000*1000 + 1000.
    PRIMES = set( helpers.primes_upto(2001000) )
    # Keep track of the best run. For easy comparison, use a (run, a, b)
    # tuple.
    best_run = (0, 0, 0)
    for a in avals:
        for b in bvals:
            run = prime_run(a, b)
            if (run,) > best_run:
                best_run = (run, a, b)
    return print( best_run[1]*best_run[2] )

# ----------------------------------------------------------------------

def prime_run(a, b):
    """Accept a pair of integers, a and b. Return the number of
    consecutive primes (starting with n=0) given by
        n**2 + a*n + b
    """
    n = 0
    while n**2 + a*n + b in PRIMES:
        n += 1
    return n

# ######################################################################

if __name__ == '__main__':
    main()
