#!/usr/bin/env python3

"""
Charles McEachern
2018-04-20
https://projecteuler.net/problem=12
"""

import helpers

# ######################################################################

def main():
    n = 0
    while True:
        n += 1
        tri = n*(n+1)//2
        ndivisors = helpers.ndivisors(tri)
        if ndivisors > 500:
            print(n, ':', tri, ':', ndivisors)
            break
    return

# ######################################################################

if __name__ == '__main__':
    main()
