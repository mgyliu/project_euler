# Functions that are likely to be useful for more than
# one problem :)

# Prime factorization of n
# Returns a list
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
				factors.append(int(n))
				break
	return factors	

# Checks if n is prime
def is_prime(n):
    if n < 2:
        return False 
        
    if n == 2 or n == 3:
        return True 

    if (n%6 == 5 or n%6 == 1) and len(find_factors(n)) == 1:
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
		