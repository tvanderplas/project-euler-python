

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

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

if __name__ == '__main__':
	print(get_prime_factors(600851475143)[-1])

