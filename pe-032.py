#!/usr/bin/env python3

"""
Charles McEachern
2018-11-14
https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9
pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""

import itertools

# ######################################################################

def num(digs):
    tally = 0
    for d in digs:
        tally *= 10
        tally += d
    return tally

# ----------------------------------------------------------------------

def pandigital_products(digs):
    # The product will always be exactly 4 or 5 digits. And without loss
    # of generality we can say the multiplicand is 1 or 2 digits.
    for i in range(1, 3):
        for j in range(5, 7):
            m, n, p = num(digs[:i]), num(digs[i:j]), num(digs[j:])
            if m*n == p:
                yield p

# ----------------------------------------------------------------------

def main():
    products = set()
    for digs in itertools.permutations(list(range(1, 10)), 9):
        for p in pandigital_products(digs):
            products.add(p)
    return print( sum(products) )

# ######################################################################

if __name__ == '__main__':
    main()
