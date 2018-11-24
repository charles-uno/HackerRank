#!/usr/bin/env python3

"""
Charles McEachern
2018-11-20
https://projecteuler.net/problem=47

The first two consecutive numbers to have two distinct prime factors
are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2**2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime
factors each. What is the first of these numbers?
"""

import itertools

import helpers

# ######################################################################

NDF_TARGET = 4

def n_distinct_factors(n):
    return len( set( helpers.factors(n) ) )

# ----------------------------------------------------------------------

def first_ndf_match(n):
    # Figure out the number of distinct factors for the numbers around
    # n. Note that we just need that many in a row -- n can be anywhere
    # in the sequence.
    ndfs = []
    for i in range(n - NDF_TARGET + 1, n + NDF_TARGET):
        ndfs.append( n_distinct_factors(i) )
    # Check if we have enough matches in a row. Then, if we match
    # [23, 24, 25], return 23.
    for i in range(NDF_TARGET):
        if ndfs[i:i + NDF_TARGET] == [NDF_TARGET]*NDF_TARGET:
            return n - NDF_TARGET + 1 + i
    return False

# ----------------------------------------------------------------------

def product(seq):
    tally = 1
    for s in seq:
        tally *= s
    return tally

# ----------------------------------------------------------------------

def main():
    # I'll bet at least one of the elements of the series will have no
    # higher powers. Let's see if that's true!
    primes = list( helpers.primes_upto(100) )
    # Come up with all combinations of 4 primes. Sort them by product.
    combos = sorted(itertools.combinations(primes, NDF_TARGET), key=product)
    for combo in combos:
        match = first_ndf_match( product(combo) )
        if match:
            print(match)
            break
    print('NO MATCH')
    return

# ######################################################################

if __name__ == '__main__':
    main()
