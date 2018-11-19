#!/usr/bin/env python3

"""
Charles McEachern
2018-11-14
https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""

# ######################################################################

def power_digit_sum(n, exp):
    tally = 0
    while n:
        n, d = n//10, n % 10
        tally += d**exp
    return tally

# ----------------------------------------------------------------------

def main():
    # We know that at most this will be a six-digit number, since 7*9**5
    # is a six-digit number. So no possible seven-digit number can
    # satisfy the condition.
    matches = []
    for n in range(2, 999999):
        if n == power_digit_sum(n, 5):
            matches.append(n)
    return print(sum(matches))

# ######################################################################

if __name__ == '__main__':
    main()
