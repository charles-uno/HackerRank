#!/usr/bin/env python3

"""
Charles McEachern
2018-11-26
https://projecteuler.net/problem=91

The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates
and are joined to the origin, O(0,0), to form triangle OPQ.

There are exactly fourteen triangles containing a right angle that can
be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.

Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be
formed?
"""

import helpers

# ######################################################################

def dot_product(v0, v1):
    return sum( x0*x1 for x0, x1 in zip(v0, v1) )

# ----------------------------------------------------------------------

XMAX = 50

def main():
    triangles = set()
    points = [ (x, y) for x in range(XMAX+1) for y in range(XMAX+1) ]
    for px, py in points:
        for qx, qy in points:
            # Watch out for overlapping points.
            if len( { (px, py), (qx, qy), (0, 0) } ) < 3:
                continue
            # Watch out for double counting.
            if (px, py) < (qx, qy):
                continue
            # Check for perpendicular slopes.
            slopes = [
                (px, py),
                (qx, qy),
                (px-qx, py-qy),
            ]
            # For legibility. 
            slope_pairs = [
                (slopes[0], slopes[1]),
                (slopes[1], slopes[2]),
                (slopes[2], slopes[0]),
            ]
            if any( dot_product(*x) == 0 for x in slope_pairs ):
                triangles.add( ( (px, py), (qx, qy) ) )
    [ print(x) for x in sorted(triangles) ]
    return print( len(triangles) )

# ######################################################################

if __name__ == '__main__':
    main()
