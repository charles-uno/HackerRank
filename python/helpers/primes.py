
import collections
import math
import numpy as np

# ######################################################################

# Sometimes it's easier to remember primes as we go. Use a list, as
# order may matter.
PRIMES = [2]

def primes():
    """Generator that spits out primes forever."""
    global PRIMES
    for p in PRIMES:
        yield p
    i = max(PRIMES)
    while True:
        i += 1
        if any( i % p == 0 for p in PRIMES ):
            continue
        PRIMES.append(i)
        yield i

# ######################################################################

def factors(n):
    """Yield the factors of a given number, including duplicates."""
    p = 2
    while n > 1:
        # We're working up, so n % p == 0 implies p is prime.
        while n % p == 0:
            n /= p
            yield p
        p += 1

# ----------------------------------------------------------------------

def factor_counts(n):
    """Factorize a number, then return a dictionary. Index is prime
    factors, value is the power of that factor.
    """
    facs = list( factors(n) )
    return { x:facs.count(x) for x in set(facs) }

# ######################################################################

def nth_prime(n):
    """Accept an integer N. Return the Nth prime."""
    for i, p in enumerate( primes() ):
        if i == n-1:
            return p

# ----------------------------------------------------------------------

def primes_upto(n):
    """Accept an integer. Yield primes up to there using a sieve."""
    # No need to track evens.
    if n >= 2:
        yield 2
    sieve = np.ones(n//2, dtype=bool)
    sieve[0] = False
    # If i is true, 2i+1 is prime. So we can strike (2i+1)**2 and
    # further multiples.
    for i in range(1, int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*i+2*i::2*i+1] = False
    for i, isprime in enumerate(sieve):
        if isprime:
            yield 2*i+1

# ######################################################################

def scm(*args):
    """Accept any number of positive integers. Return their smallest
    common multiple.
    """
    # Let's figure out the maximum power of 2 we need, and the maximum
    # power of 3, and so on.
    power_by_factor = collections.defaultdict(int)
    for n in args:
        for f, p in factor_counts(n).items():
            power_by_factor[f] = max(power_by_factor[f], p)
    # Now return the product of all those maximal powers.
    tmp = 1
    for f, p in power_by_factor.items():
        tmp *= f**p
    return tmp

# ----------------------------------------------------------------------

def gcd(*args):
    """Accept two any number of positive integers. Return the greatest
    common divisor.
    """
    divs = [ divisors(n) for n in args ]
    return max( set.intersection(*divs) )

# ----------------------------------------------------------------------

def divisors(n):
    """Accept an integer. Return a set of its divisors, including
    itself.
    """
    if n < 1:
        raise ValueError('Can\'t factor nonpositive numbers')
    fc = factor_counts(n)
    divs = [1]
    for factor, count in fc.items():
        divs = { d*factor**i for d in divs for i in range(count+1) }
    return divs

# ----------------------------------------------------------------------

def reduce_fraction(p, q):
    """Accept two integers. Return them, scaled down by their greatest
    common divisor.
    """
    common_factor = gcd(abs(p), abs(q))
    return p//common_factor, q//common_factor

# ----------------------------------------------------------------------

def proper_divisors(n):
    """Accept an integer. Return a set of its divisors, not including
    itself.
    """
    return divisors - {n}

# ----------------------------------------------------------------------

def ndivisors(n):
    """Accept an integer. Return the number of divisors it has
    (including itself) without actually calculating those divisors.
    """
    return np.prod( [ x+1 for x in factor_counts(n).values() ] )
