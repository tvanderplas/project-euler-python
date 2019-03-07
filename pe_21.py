

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

from math import sqrt

def divisors(x: int):
	if x > 1:
		answer = [1]
		for n in range(2, int(sqrt(x)) + 1):
			if x % n == 0:
				answer.extend([n, x // n])
		return [x for x in sorted(set(answer))]
	else:
		return [x for x in []]

if __name__ == '__main__':
	answer = []
	for n in range(2, 10000):
		sum_div_n = sum(divisors(n))
		if sum_div_n != n:
			if n == sum(divisors(sum_div_n)):
				answer.append(n)
	print(sum(answer))