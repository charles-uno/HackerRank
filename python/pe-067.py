#!/usr/bin/env python3

"""
Charles McEachern
2018-11-20
https://projecteuler.net/problem=67

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click
and 'Save Link/Target As...'), a 15K text file containing a triangle
with one-hundred rows.
"""

# ######################################################################

def load_triangle():
    with open('pe-067-triangle.txt', 'r') as handle:
        return [ [ int(x) for x in line.split() ] for line in handle ]

# ----------------------------------------------------------------------

def mini_triangle():
    """Example triangle, for validation."""
    return [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3],
    ]

# ----------------------------------------------------------------------

def main():
    triangle = load_triangle()
    # Eat the triangle from the bottom up. For each i, keep track of the
    # best sum we can get passing through that spot.
    old_sum = triangle.pop(-1)
    while triangle:
        new_sum = []
        for i, val in enumerate( triangle.pop(-1) ):
            new_sum.append( val + max(old_sum[i:i+2]) )
        old_sum = new_sum
    return print( max(old_sum) )

# ######################################################################

if __name__ == '__main__':
    main()
