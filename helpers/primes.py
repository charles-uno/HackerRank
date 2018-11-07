
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
    factors = list( factors(n) )
    return { x:factors.count(x) for x in set(factors) }

# ######################################################################

def nth_prime(n):
    """Accept an integer N. Return the Nth prime."""
    for i, p in enumerate( primes() ):
        if i == n-1:
            return p

# ----------------------------------------------------------------------

def primes_upto(n):
    """Accept an integer. Yield primes up to there using a sieve."""
    sieve = np.ones(n, dtype=bool)
    sieve[:2] = False
    for i in range(2, math.floor(n**0.5)):
        if sieve[i]:
            sieve[2*i::i] = False
    for i in range(n):
        if sieve[i]:
            yield i

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
