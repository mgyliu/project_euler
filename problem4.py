"""
PROBLEM 4

A palindromic number reads the same both ways. The largest 
palindrome made from the product of two 2-digit numbers is 
9009 = 91 x 99.

Find the largest palindrome made from the product of two 
3-digit numbers.

https://projecteuler.net/problem=4
"""

from functions import is_palindrome

pal_products = set()
for i in range(999, 100-1, -1):
    for j in range(999, 100-1, -1):
        if is_palindrome(i*j):
            pal_products.add(i*j)

print(max(pal_products))

