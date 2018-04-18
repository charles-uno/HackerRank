#!/usr/bin/env python3

"""
Charles McEachern
2018-04-17
https://projecteuler.net/problem=6
"""

# ######################################################################

def main():
    print( sqr_sum(*range(1, 101)) - sum_sqr(*range(1, 101)))

# ----------------------------------------------------------------------

def sum_sqr(*args):
    return sum( x**2 for x in args )

# ----------------------------------------------------------------------

def sqr_sum(*args):
    return sum(args)**2

# ######################################################################

if __name__ == '__main__':
    main()
