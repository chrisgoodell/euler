
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13. What is the 10001st prime number?
'''

def sieveofE():
    '''Yields the sequence of prime numbers via the sieve of Eratosthenes algorithm'''
    D = {}  # map composite integers to primes
    q = 2   # initial integer to test for prime
    while 1:
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1

def nth_prime(n):
    for i, prime in enumerate(sieveofE()):
        if i == n - 1:
            return prime

print(nth_prime(10001))
