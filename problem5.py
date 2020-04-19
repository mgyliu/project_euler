"""
PROBLEM 5

2520 is the smallest number that can be divided by each of 
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?

https://projecteuler.net/problem=5
"""

from functions import find_prime_factors
from collections import Counter 

factors = {}
for i in range(1, 20+1):
    for f, c in Counter(find_prime_factors(i)).items():
        if f not in factors.keys():
            factors[f] = c
        else:
            factors[f] = max(factors[f], c)
        
prod = 1
for f,c in factors.items():
    prod *= f ** c

print(prod)