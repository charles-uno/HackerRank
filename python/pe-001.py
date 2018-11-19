#!/usr/bin/env python3

"""
Charles McEachern
2018-04-17
https://projecteuler.net/problem=1
"""

# ######################################################################

def main():
    print( sum( i for i in range(1000) if i % 3 == 0 or i % 5 == 0 ) )

# ######################################################################

if __name__ == '__main__':
    main()
