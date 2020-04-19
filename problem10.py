"""
PROBLEM 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

https://projecteuler.net/problem=10
"""

from functions import prime_generator

sum = 0
for p in prime_generator(2000000+1):
    sum += p
print(sum)
