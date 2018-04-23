#!/usr/bin/env python3

"""
Charles McEachern
2018-04-23
https://projecteuler.net/problem=16
"""

# ######################################################################

def main():
    # I'll bet there's a trick to this, but it's trivial to solve it
    # with brute force.
    print( sum( int(x) for x in str(2**1000) ) )

# ######################################################################

if __name__ == '__main__':
    main()
