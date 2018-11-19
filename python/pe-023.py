#!/usr/bin/env python3

"""
Charles McEachern
2018-04-23
https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import helpers

# ######################################################################

def main():
    imax = 28123
    # First, find all the abundant numbers.
    abundant_numbers = set()
    for i in range(1, imax):
        if is_abundant(i):
#            print('Found abundant number:', i)
            abundant_numbers.add(i)
#    print('Found', len(abundant_numbers), 'abundant numbers')
    # Now check what we can get with sums of two abundant numbers.
    not_double_abundant = set()
    for i in range(imax):
        for a0 in abundant_numbers:
            if i - a0 in abundant_numbers:
                break
        else:
#            print('Not double abundant:', i)
            not_double_abundant.add(i)
    print('Sum of non-double-abundant numbers:', sum(not_double_abundant))

# ----------------------------------------------------------------------

def is_abundant(n):
    # Double n because this returns all divisors, not just proper divisors.
    return 2*n < sum( helpers.divisors(n) )

# ######################################################################

if __name__ == '__main__':
    main()
