#!/usr/bin/env python3

"""
Charles McEachern
2018-11-07
https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import helpers

# ######################################################################

def main():
    # Tried using the golden ratio to calculate large Fibonacci numbers
    # directly, do a bisection search, but it turns out Python will only
    # store floats to about 300 places. But computing a few thousand
    # Fibonacci values naively, it turns out, only takes a few seconds.
    for i, f in enumerate( helpers.fibonacci() ):
        if len( str(f) ) >= 1000:
            return print(i, f)

# ######################################################################

if __name__ == '__main__':
    main()
