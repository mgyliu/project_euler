"""
PROBLEM 6

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.

https://projecteuler.net/problem=6
"""

n = 100
sum_sq = sum(i**2 for i in range(n+1))
sq_sum = sum(i for i in range(n+1))**2

print(sq_sum - sum_sq)