#!/usr/bin/env python3

"""
Charles McEachern
2018-11-13
https://projecteuler.net/problem=31

In England the currency is made up of pound, £, and pence, p, and there
are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

import math

# ######################################################################

COINS = [1, 2, 5, 10, 20, 50, 100, 200]

def main():
    target = 200
    combos = [ [] ]
    # The 1p and 2p coins are the expensive ones to compute, so leave
    # them off for now. Figure out all the different ways we can arrange
    # 5p and up to get no more than 200p.
    for coin in sorted(COINS, reverse=True):
        if coin < 3:
            break
        new_combos = []
        for combo in combos:
            leftover = target - sum(combo)
            for i in range(leftover//coin + 1):
                new_combos.append( combo + i*[coin] )
        combos = new_combos
    # If the coins sum to 200 exactly, that's one combination. If they
    # sum to 195, that's 3 combinations, since there can be zero, one,
    # or two 2p coins (and the rest 1p). If we are Np shy, that
    # represents 1 + N//2 options.
    ncombos = 0
    for combo in combos:
        ncombos += 1 + (target-sum(combo))//2
    return print(ncombos)

# ######################################################################

if __name__ == '__main__':
    main()
