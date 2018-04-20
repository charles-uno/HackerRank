
import collections
import math
import numpy as np

# ######################################################################

def scm(*args):
    # Let's figure out the maximum power of 2 we need, and the maximum
    # power of 3, and so on.
    power_by_factor = collections.defaultdict(int)
    for n in args:
        for f, p in get_power_by_factor(n).items():
            power_by_factor[f] = max(power_by_factor[f], p)
    # Now return the product of all those maximal powers.
    tmp = 1
    for f, p in power_by_factor.items():
        tmp *= f**p
    return tmp

# ----------------------------------------------------------------------

def get_power_by_factor(n):
    factors = list( factorize(n) )
    return { x:factors.count(x) for x in set(factors) }

# ----------------------------------------------------------------------

def factorize(n):
    primes = []
    i = 1
    while n > 1:
        i += 1
        if any( i % p == 0 for p in primes ):
            continue
        # Looks like we found a prime!
        primes.append(i)
        # Divide out divisors. Watch out for degeneracy.
        while n % i == 0:
            n //= i
            yield i

# ----------------------------------------------------------------------

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







# ----------------------------------------------------------------------

def divisors(n):
    for i in range(1, n//2):
        if n % i == 0:
            yield i
    yield n
