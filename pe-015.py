#!/usr/bin/env python3

"""
Charles McEachern
2018-04-23
https://projecteuler.net/problem=15
"""

import helpers

# ######################################################################

def main():
    # How many ways are there to traverse a 20x20 diagonal grid? We have
    # 20 "left" operations and 20 "up" operations. There are (40 choose
    # 20) ways to scramble them.
    print( choose(40, 20) )

# ----------------------------------------------------------------------

def choose(n, k):
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))

# ######################################################################

if __name__ == '__main__':
    main()
