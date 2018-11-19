#!/usr/bin/env python3

"""
Charles McEachern
2018-04-19
https://projecteuler.net/problem=10
"""

import helpers

# ######################################################################

def main():
    print( sum( helpers.primes_upto(2000000) ) )

# ######################################################################

if __name__ == '__main__':
    main()
