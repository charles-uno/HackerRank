#!/usr/bin/env python3

"""
Charles McEachern
2018-11-14
https://projecteuler.net/problem=641

Consider a row of n dice all showing 1.

First turn every second die,(2,4,6,…), so that the number showing is
increased by 1. Then turn every third die. The sixth die will now show a
3. Then turn every fourth die and so on until every nth die (only the
last die) is turned. If the die to be turned is showing a 6 then it is
changed to show a 1.

Let f(n) be the number of dice that are showing a 1 when the process
finishes. You are given f(100)=2 and f(10**8)=69.

Find f(10**36).
"""

import helpers

# ######################################################################

def main():
    # We're looking for numbers for which ndivisors % 6 == 1. So in
    # terms of powers of factors, we're looking at (p**6) and
    # (p**4 * q**4). We can string these together however we like.

    # Easy part: for how many N does N**6 <= 10**36? Note this captures
    # all combinations of primes with everything in powers of 6.

    # Hard part: for how many N0, N1, ... Nk does
    # N0**4 N1**4 ... Nk**4 <= 10**36? Note we need an even number of
    # distinct N. Then, for each, we can also tack on powers of six.



    fmos = set()

    for i in range(20000):
        fmos.add( tuple( (p-1)%6 for p in helpers.factors(6*i + 1) ) )

    [ print(f) for f in fmos ]

    return

    for n in range(1, 10001):
        if helpers.ndivisors(n) % 6 == 1:
            print(n, helpers.ndivisors(n), helpers.factor_counts(n))

    return

# ######################################################################

if __name__ == '__main__':
    main()
