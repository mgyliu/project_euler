"""
PROBLEM 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 
13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

https://projecteuler.net/problem=7
"""

from functions import prime_generator

pgen = prime_generator(10**10)

answer = 0
for i in range(10001):
    answer = next(pgen)

print(answer)