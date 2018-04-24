#!/usr/bin/env python3

"""
Charles McEachern
2018-04-23
https://projecteuler.net/problem=22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import helpers

# ######################################################################

def main():
    names = readfile('pe-022-names.txt').replace('"', '').split(',')
    # We want to index from one, not zero.
    names = [''] + sorted(names)
    print( sum( i*namescore(x) for i, x in enumerate(names) ) )

# ----------------------------------------------------------------------

def namescore(name):
    return sum( score(x) for x in name.upper() )

# ----------------------------------------------------------------------

def score(letter):
    return ord(letter) - ord('A') + 1

# ----------------------------------------------------------------------

def readfile(path):
    with open(path, 'r') as handle:
        return ''.join(handle)

# ######################################################################

if __name__ == '__main__':
    main()
