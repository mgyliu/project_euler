"""
PROBLEM 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

https://projecteuler.net/problem=3
"""

from functions import find_prime_factors
given = 600851475143

print(max(find_prime_factors(given))) 
