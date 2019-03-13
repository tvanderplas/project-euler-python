from math import sqrt

def fibonacci(n: int):
	getcontext().prec = 1000
	phi = Decimal((1 + sqrt(5)) / 2)
	f = (phi ** n - (-phi) ** -n) / (2 * phi - 1)
	return int(f)

def fibonacci_generator(x):
	"""generates list of fibonacci numbers under x"""
	numbers = [1, 1]
	while numbers[-1] + numbers[-2] < int(x):
		numbers.append(numbers[-1] + numbers[-2])
	return numbers

def get_primes(limit: int = 1000000):
	if limit < 2:
		return []
	_primes = [2]
	for number in range(max(_primes), limit + 1):
		for prime in _primes:
			if number % prime == 0:
				break
			elif number % prime != 0 and prime >= sqrt(number):
				_primes.append(number)
				break
	return _primes

def get_prime_factors(x: int, _answer: list = [], _primes: list = []):
	if len(_primes) == 0:
		_answer.clear()
		_primes = get_primes(int(sqrt(x) if x > 4 else x))
	for p in _primes:
		if x % p == 0 and x != p:
			_answer.append(p)
			return get_prime_factors(x // p, _answer, _primes)
		elif p == _primes[-1]:
			_answer.append(x)
			return _answer
	return _answer

def collatz(n: int):
	"""returns chain length of collatz sequence"""
	chains = dict()
	for x in range(1, n):
		chain = 1
		p = x
		while x > 1:
			if x % 2 == 0:
				x //= 2
				if x in chains:
					chain += chains[x] - 1
					x = 1
			else:
				x *= 3; x += 1
			chain += 1
		chains.update({p: chain})
	return chains

def catalan(x: int):
	pascal = [1, 1]
	for n in range(x * 2 - 1):
		pascal = [pascal[i] + pascal[i + 1] for i, v in enumerate(pascal) if i != len(pascal) - 1]
		pascal.append(1)
		pascal.insert(0, 1)
	return pascal[len(pascal) // 2]

def count_letters(x: int):
	"""returns number of letters for integers up to 1000"""
	map_ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
	map_tens = [0, 4, 6, 6, 5, 5, 5, 7, 6, 6]
	digits = [int(d) for d in str(x)[::-1]]

	if len(digits) > 3:
		digits[3] = map_ones[digits[3]] + 8

	if len(digits) > 2 and digits[2] != 0:
		if digits[:2] == [0, 0]:
			digits[2] = map_ones[digits[2]] + 7
		else:
			digits[2] = map_ones[digits[2]] + 10

	if len(digits) > 1:
		if digits[:2] in [[0, 1], [1, 1], [2, 1], [3, 1], [5, 1], [8, 1]]:
			digits[1] = 3
		else:
			digits[1] = map_tens[digits[1]]

	digits[0] = map_ones[digits[0]]

	return sum(digits)

def max_path(triangle: list):
	for i, row in enumerate(triangle[1:]):
		for ii in range(1, len(row) + 1):
			if 0 < ii < len(row) - 1:
				triangle[i + 1][ii] += max(triangle[i][ii - 1:ii + 1])
			elif ii == 0:
				triangle[i + 1][ii] += triangle[i][ii]
			elif ii == len(row) - 1:
				triangle[i + 1][ii] += triangle[i][ii - 1]
	return max(triangle[-1])

def is_leap_year(year: int):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		return True
	else:
		return False

def days_in_month(month: int = 4, year: int = 1900):
	num_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	num_days_ly = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	return num_days[month] if not is_leap_year(year) else num_days_ly[month]

def factorial(x: int):
	if x > 0:
		x *= factorial(x - 1)
		return x
	else:
		return 1

def divisors(x: int):
	if x > 1:
		answer = [1]
		for n in range(2, int(sqrt(x)) + 1):
			if x % n == 0:
				answer.extend([n, x // n])
		return [x for x in sorted(set(answer))]
	else:
		return [x for x in []]

def permutations(word: str):
	if len(word) < 2:
		return [word]
	base = word[:2]
	answer = []
	answer.extend([base, base[::-1]])
	next_answer = []
	for x in range(2, len(word)):
		for item in answer:
			for n in range(len(item) + 1):
				an_item = list(item)
				an_item.insert(n, word[x])
				next_answer.append(''.join([x for x in an_item]))
		answer.clear()
		answer.extend(next_answer)
		next_answer.clear()
		answer.sort()
	return answer
