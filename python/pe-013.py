#!/usr/bin/env python3

"""
Charles McEachern
2018-11-23
https://projecteuler.net/problem=13
"""

# ######################################################################

def main():
    tally = 0
    with open('pe-013-numbers.txt', 'r') as handle:
        for line in handle:
            tally += int( line.strip() )
    return print(tally)

# ######################################################################

if __name__ == '__main__':
    main()
