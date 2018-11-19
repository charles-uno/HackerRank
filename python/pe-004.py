#!/usr/bin/env python3

"""
Charles McEachern
2018-04-17
https://projecteuler.net/problem=4
"""

# ######################################################################

def main():
    # Three digits isn't very dig. Let's brute force this one. 
    print( max( find_palindrome_numbers(3) ) )

# ----------------------------------------------------------------------

def find_palindrome_numbers(ndigs=3):
    imin = 10**(ndigs-1)
    imax = 10**ndigs
    for i in range(imin, imax):
        for j in range(imin, imax):
            if is_palindrome_number(i*j):
                yield i*j

# ----------------------------------------------------------------------

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

# ######################################################################

if __name__ == '__main__':
    main()
