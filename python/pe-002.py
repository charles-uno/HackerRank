#!/usr/bin/env python3

"""
Charles McEachern
2018-04-17
https://projecteuler.net/problem=2
"""

# ######################################################################

def main():
    print( sum( x for x in fib_up_to(4000000) if x % 2 == 0 ) )

# ----------------------------------------------------------------------

def fib_up_to(n):
    vals = [1, 2]
    while vals[0] < n:
        vals.append( sum(vals) )
        yield vals.pop(0)

# ######################################################################

if __name__ == '__main__':
    main()
