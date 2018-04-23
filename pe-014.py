#!/usr/bin/env python3

"""
Charles McEachern
2018-04-23
https://projecteuler.net/problem=14
"""

# ######################################################################

def main():
    print( max( (steplen(x), x) for x in range(1000000) ) )

# ----------------------------------------------------------------------

STEPLENS = {0:0, 1:1}

def steplen(n):
    global STEPLENS
    if n not in STEPLENS:
        STEPLENS[n] = 1 + steplen( step(n) )
    return STEPLENS[n]

# ----------------------------------------------------------------------

def step(n):
    return 3*n + 1 if n % 2 else n//2

# ######################################################################

if __name__ == '__main__':
    main()
