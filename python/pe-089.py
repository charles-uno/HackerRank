#!/usr/bin/env python3

"""
Charles McEachern
2018-11-23
https://projecteuler.net/problem=89

For a number written in Roman numerals to be considered valid there are
basic rules which must be followed. Even though the rules allow some
numbers to be expressed in more than one way there is always a "best"
way of writing a particular number.

For example, it would appear that there are at least six ways of writing
the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the
last example is considered to be the most efficient, as it uses the
least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
contains one thousand numbers written in valid, but not necessarily
minimal, Roman numerals; see About... Roman Numerals for the definitive
rules for this problem.

Find the number of characters saved by writing each of these in their
minimal form.
"""

# ######################################################################

def read_numerals():
    with open('pe-089-roman.txt', 'r') as handle:
        return [ x.strip() for x in handle ]

# ----------------------------------------------------------------------

ROMAN_VALUES = {
    1000:'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}

# Numerals must be arranged in descending order of size.
# M, C, and X cannot be equalled or exceeded by smaller denominations.
# D, L, and V can each only appear once.

# Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
# I can only be placed before V and X.
# X can only be placed before L and C.
# C can only be placed before D and M.

def roman(n):
    for val, rom in sorted(ROMAN_VALUES.items(), reverse=True):
        if n >= val:
            return rom + roman(n - val)
    return ''

# ----------------------------------------------------------------------

def arabic(r):
    for val, rom in sorted(ROMAN_VALUES.items(), reverse=True):
        if r.startswith(rom):
            return val + arabic( r[len(rom):] )
    return 0

# ----------------------------------------------------------------------

def main():
    # Start with roman numerals from the file, then convert them to
    # latin numerals and back again to get the most terse form for each.
    rn_old, rn_new = read_numerals(), []
    for rn in rn_old:
        ln = arabic(rn)
        rn_new.append( roman(ln) )
    digs_old = sum( len(x) for x in rn_old )
    digs_new = sum( len(x) for x in rn_new )
    print('OLD:', digs_old)
    print('NEW:', digs_new)
    print('SAVED:', digs_old - digs_new)
    return

# ######################################################################

if __name__ == '__main__':
    main()
