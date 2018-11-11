#!/usr/bin/env python3

"""
Charles McEachern
2018-11-10
https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
"""

# ######################################################################

def main():
    # The one at the center is a special case. Add that on.
    # If there are N layers to the square already, the four corners of
    # the next layer are: (N**2+N+1), (N**2+2N+2), (N**2+3N+3), and
    # (N**2+4N+4). So (4N**2+10N+10). Note also that we just added two
    # layers, so we can say N=(2n-1), each layer adds (16n**2+4n+4).
    # To get the sum from a 5x5 grid, we need to do the middle (special
    # case at n=0) plus 2 more. To get a 1001x1001 spiral, we're looking
    # at n=0 plus another 500.
    print( sum( layer_sum(n) for n in range(501) ) )

# ----------------------------------------------------------------------

def layer_sum(n):
    if n == 0:
        return 1
    else:
        return 16*n**2 + 4*n + 4

# ######################################################################

if __name__ == '__main__':
    main()
