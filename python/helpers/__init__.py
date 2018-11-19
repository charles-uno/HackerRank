
from .primes import *

# ######################################################################

def fibonacci():
    """Iterator that returns Fibonacci numbers forever."""
    i, j = 0, 1
    while True:
        yield i
        i, j = j, i+j
