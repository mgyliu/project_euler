fib_1 = 1
fib_2 = 2
fib_array = []

while fib_1 <= 4000000:
    fib_array.append(fib_1)
    fib_1, fib_2 = fib_2, fib_1 + fib_2

required_sum = sum(filter(lambda x: x % 2 == 0, fib_array))
print(required_sum)
