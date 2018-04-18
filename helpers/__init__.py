

import collections

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
