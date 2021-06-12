from pprint import pprint
from datetime import datetime
from icecream import ic as IC, install
from math import isqrt


def unixTimestamp():
    return f'{datetime.now().strftime("%d %B, %Y %H:%M:%S")}|>'


IC.configureOutput(prefix=unixTimestamp)
install()


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, isqrt(n), 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*len(sieve[i*i::2*i])
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


rateofLimit = int(input("Enter the Range for generting prime numbers:"))
totalNumberOfPrimes = primes(rateofLimit)
print(f'Total No of Primes :{len(totalNumberOfPrimes)}')
print(f'Size of Primes Array :{totalNumberOfPrimes.__sizeof__()}')
