"""
PROBLEM 60

The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any 
order the result will always be prime. For example, 
taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest 
sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any 
two primes concatenate to produce another prime.

https://projecteuler.net/problem=60
"""

from functions import is_prime
from functions import prime_generator 
import itertools 
import pdb 
import time 
import math

def check_pair(p1, p2):
    p1_digs = int(math.log(p1, 10) + 1)
    p2_digs = int(math.log(p2, 10) + 1)
    return is_prime(p1 * 10**p2_digs + p2) and is_prime(p2 * 10**p1_digs + p1)
        
start = time.time()
plist = list(prime_generator(10000))

# I know this code is ugly! I plan on fixing it :)
good_pairs_sets = []
progress = 0
for p in itertools.combinations(plist, 2):
    if check_pair(p[0], p[1]):
        good_pairs_sets.append(set(p))

    progress += 1
    if progress % 10000 == 0:
        print(progress)

print("There are {} good pairs".format(len(good_pairs_sets)))

good_triples_sets = []
progress = 0
for pp in itertools.combinations(good_pairs_sets, 2):
    progress += 1
    if progress % 100000 == 0:
        print(progress)

    symdiff = pp[0].symmetric_difference(pp[1])
    if len(symdiff) != 2:
        continue
    if symdiff in good_pairs_sets:
        good_triples_sets.append(pp[0].union(pp[1]))

print("There are {} good triples".format(len(good_triples_sets)))

good_4tuples_sets = []
progress = 0
for t in itertools.combinations(good_triples_sets, 2):
    progress += 1
    if progress % 100000 == 0:
        print(progress)

    symdiff = t[0].symmetric_difference(t[1])
    if len(symdiff) != 2:
        continue
    if symdiff in good_pairs_sets:
        good_4tuples_sets.append(t[0].union(t[1]))

print("There are {} good 4-tuples".format(len(good_4tuples_sets)))

good_5tuples_sets = []
for t in itertools.combinations(good_4tuples_sets, 2):
    symdiff = t[0].symmetric_difference(t[1])
    if len(symdiff) != 2:
        continue 
    if symdiff in good_pairs_sets:
        good_5tuples_sets.append(t[0].union(t[1]))

fname = "/Users/maggieliu/project_euler/problem60.output"
with open(fname, 'w+') as f:
    for s in good_5tuples_sets:
        f.write("{}\n".format(s))

print("There are {} good 5-tuples".format(len(good_5tuples_sets)))
print(good_5tuples_sets[:10])
print("The min is {}".format(
    min([sum(s) for s in good_5tuples_sets])
))

end = time.time() 
print("It took {} seconds".format(end-start))