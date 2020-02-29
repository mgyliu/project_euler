"""
PROBLEM 9

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

https://projecteuler.net/problem=9
"""

import pdb 

def check_pythagorean_triple(a, b, c):
    a, b, c = sorted([a, b, c])
    if a**2 + b**2 == c**2:
        return True 
    else:
        return False

def problem9(max):
    for i in range(1, int(max/2)+1):
        for j in range(1, max-i):
            k = max - j - i
            if check_pythagorean_triple(i, j, k):
                return((i,j,k))

i,j,k = problem9(1000)
print("The triple is ({}, {}, {})".format(i, j, k))
print("The product is: {}".format(i*j*k))
                