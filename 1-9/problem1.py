multiples = filter(lambda x: (x % 3 == 0) or (x % 5 == 0), range(1, 1001))
required_sum = sum(multiples)
print(required_sum)
