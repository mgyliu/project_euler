# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


given = 600851475143

def find_factors(n):
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
				factors.append(n)
				break
	print factors	

find_factors(given) 