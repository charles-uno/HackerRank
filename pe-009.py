#!/usr/bin/env python3

"""
Charles McEachern
2018-04-18
https://projecteuler.net/problem=9


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find
the product abc.

"""

import helpers

# ######################################################################

def main():
    # Let's first check the easy ones. 1000 is divisible by several
    # perfect squares: 4, 25, 100. It'd be a lot faster if we could find
    # a Pythagorean triple for one of them.
    print( pythagorean_triple(1000) )

# ----------------------------------------------------------------------

def pythagorean_triple(n):
    """Accepts an integer n. Returns a Pythagorean triple (a, b, c) such
    that a**2 + b**2 == c**2 and a + b + c == n, assuming such a triple
    exists.
    """
    # Checking for large n is slow. Let's try factoring out divisors,
    # largest first.
    for div in list( helpers.divisors(n) )[::-1]:
        for abc in pythagorean_triples(n//div):
            return [ div*x for x in abc ]
    # If we can't find any, complain.
    raise ValueError('Found no Pythagorean triples summing to %d' % n)

# ----------------------------------------------------------------------

def pythagorean_triples(n):
    """Accepts an integer n. Returns all Pythagorean triples (a, b, c)
    such that a**2 + b**2 == c**2 and a + b + c == n. Triples are
    identified via brute force.
    """
    for a in range(1, n//3):
        for b in range(a+1, n//2-a//2):
            c = n - a - b
            if a**2 + b**2 == c**2:
                yield (a, b, c)

# ######################################################################

if __name__ == '__main__':
    main()
