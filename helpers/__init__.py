
import collections
import math
import numpy as np

# ######################################################################

def fibonacci():
    """Iterator that returns Fibonacci numbers forever."""
    i, j = 0, 1
    while True:
        yield i
        i, j = j, i+j

# ######################################################################

def scm(*args):
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

# ######################################################################

PRIMES = [2]

def factorize(n):
    # In most situations, it's faster to remember primes as we find
    # them. Potential downside is, if we accumulate a ton of primes, it
    # now takes longer to factor small numbers. But problems trpically
    # have us worry about stuff in ascending order anyway.
    global PRIMES
    # Start by checking for prime factors we have encountered already.
    for p in PRIMES:
        while n % p == 0:
            n //= p
            yield p
    # Now check for additional primes. Note that we stores primes in
    # ascending order, so the last one is the largest.
    i = PRIMES[-1]
    while n > 1:
        i += 1
        if any( i % p == 0 for p in PRIMES ):
            continue
        # Looks like we found another prime!
        PRIMES.append(i)
        # Now check if it's a divisor.
        while n % i == 0:
            n //= i
            yield i

# ----------------------------------------------------------------------

def factor_counts(n):
    """Factorize a number, then return a dictionary. Index is prime
    factors, value is the power of that factor.
    """
    factors = list( factorize(n) )
    return { x:factors.count(x) for x in set(factors) }

# ######################################################################

def nth_prime(n):
    primes = []
    i = 1
    while len(primes) < n:
        i += 1
        if any( i % p == 0 for p in primes ):
            continue
        # Looks like we found a prime!
        primes.append(i)
    return primes[-1]

# ----------------------------------------------------------------------

def primes_upto(n):
    sieve = np.ones(n, dtype=bool)
    sieve[:2] = False
    for i in range(2, math.floor(n**0.5)):
        if sieve[i]:
            sieve[2*i::i] = False
    for i in range(n):
        if sieve[i]:
            yield i

# ######################################################################

def divisors(n):
    if n < 1:
        raise ValueError('Can\'t factor nonpositive numbers')
    fc = factor_counts(n)
    divs = [1]
    for factor, count in fc.items():
        divs = { d*factor**i for d in divs for i in range(count+1) }
    return divs

# ----------------------------------------------------------------------

def proper_divisors(n):
    return divisors - {n}

# ----------------------------------------------------------------------

def ndivisors(n):
    """Factorize a number to figure out how many divisors it has,
    without actually generating those divisors.
    """
    return np.prod( [ x+1 for x in factor_counts(n).values() ] )
