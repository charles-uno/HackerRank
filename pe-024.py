#!/usr/bin/env python3

"""
Charles McEachern
2018-04-23
https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import math

# ######################################################################

def main():
    digs = list( range(10) )
    seq = []
    # There are 10! permutations total. 3628800
    # There are 9! permutations starting with 0. 362880. Another 9!
    # starting with 1, with 2, etc. So we can figure out the first
    # digit.
    n = 1000000 - 1
    for i in list(range(10))[::-1]:
        seq.append( digs.pop( n//math.factorial(i) ) )
        n %= math.factorial(i)
    print( ''.join( str(x) for x in seq ) )

# ######################################################################

if __name__ == '__main__':
    main()
