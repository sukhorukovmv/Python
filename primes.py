#!/usr/bin/python3

import itertools

def primes():
    def isPrime(n):
        def findDivisor(n, testDivisor):
            if testDivisor ** 2 > n:
                return True
            if n % testDivisor == 0:
                return False
            else:
                testDivisor += 1
                return findDivisor(n, testDivisor)
        return findDivisor(n, 2)

    n = 1
    while True:
        n += 1
        if isPrime(n) == True:
            #print(n)
            yield n

#primes()
print(list(itertools.takewhile(lambda x : x <= 31, primes())))
