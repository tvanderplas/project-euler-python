

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from pe_03 import get_prime_factors
all_factors = []
for n in range(2, 21):
	for i in get_prime_factors(n):
		while all_factors.count(i) < get_prime_factors(n).count(i):
			all_factors.append(i)
all_factors.sort()
answer = 1
for i in all_factors:
	answer *= i
print(answer)