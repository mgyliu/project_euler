# Functions that are likely to be useful for more than
# one problem :)

from collections import Counter 

# Prime factorization of n
# Returns a list
def find_prime_factors(n):
	# returns all prime factors of n
	factors = []
	# start with the smallest possible prime factor
	d = 2
	while n > 1:
		# if d is a divisor, add it to the factors
		while n % d == 0:
			factors.append(d)
			n = n / d
		# since we keep dividing n by d, we know that whenever we append d, it will be a prime
		# (even though factors array will not be unique)	
		d = d + 1
		# if d is greater than sqrt(n) we stop on a condition
		if d*d > n:
			if n > 1: 
				factors.append(int(n))
				break
	return factors	

def prime_factorization(n):
	prime_factors = find_prime_factors(n)
	d = {p: 1 for p in prime_factors}
	for f in prime_factors:
		# how many times does f divide n?
		times = 0
		temp_n = n
		while temp_n % f == 0:
			times += 1
			temp_n = temp_n / f
		d[f] = times
	return d

# Checks if n is prime
def is_prime(n):
    if n < 2:
        return False 
        
    if n == 2 or n == 3:
        return True 

    if (n%6 == 5 or n%6 == 1) and len(find_prime_factors(n)) == 1:
        return True 
    else:
        return False

# Generates primes <= max
def prime_generator(max):
	i = 1
	while i < max: 
		i += 1
		if is_prime(i):
			yield i
		else:
			continue

# n is an int or string
def is_palindrome(n):
	s = str(n)
	while(len(s) > 1):
		if s[0] != s[-1]:
			return False 
		s = s[1:-1]
	return True 