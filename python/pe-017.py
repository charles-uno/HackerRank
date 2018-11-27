#!/usr/bin/env python3

"""
Charles McEachern
2018-11-26
https://projecteuler.net/problem=17
"""

# ######################################################################

UNITS = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

TENS = {
    0: '',
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

TEENS = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

# ----------------------------------------------------------------------

def _spell_number(n):
    if n > 1999 or n < 0 or not isinstance(n, int):
        raise ValueError('Need positive integer less than 2000')
    if n >= 1000:
        return 'one thousand ' + spell_number(n - 1000)
    elif n >= 100:
        return UNITS[n//100] + ' hundred and ' + spell_number(n % 100)
    elif 10 < n < 20:
        return TEENS[n]
    else:
        return TENS[n//10] + '-' + UNITS[n%10]

# ----------------------------------------------------------------------

def spell_number(n):
    # Clean up dangling punctuation.
    sn = _spell_number(n).replace('-zero', '').strip(' -')
    if sn.endswith(' and'):
        sn = sn.replace(' and', '')
    return sn

# ----------------------------------------------------------------------

def main():
    tally = 0
    for i in range(1, 1001):
        print(i, ':', spell_number(i))
        tally += len(spell_number(i).replace(' ', '').replace('-', ''))
    return print(tally)

# ######################################################################

if __name__ == '__main__':
    main()
