#!/usr/bin/env python3

"""
Charles McEachern
2018-04-23
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import helpers

# ######################################################################

def main():
    print( sum( x for x in amicable_pairs(10000) ) )

# ----------------------------------------------------------------------

def amicable_pairs(imax):
    for i in range(1, imax+1):
        if i != d(i) and i == d( d(i) ):
            yield i

# ----------------------------------------------------------------------

D = {}

def d(n):
    global D
    if n not in D:
        D[n] = sum( x for x in helpers.divisors(n) if x != n )
    return D[n]

# ######################################################################

if __name__ == '__main__':
    main()
