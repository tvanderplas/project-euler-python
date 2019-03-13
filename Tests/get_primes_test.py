
import context
import unittest
from Challenges.functions import get_primes

class get_primes_tests(unittest.TestCase):

	def test_primes_under_20(self):
		self.assertEqual(get_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])

	def test_no_primes_under_1(self):
		self.assertEqual(get_primes(1), [])

	def test_no_primes_if_zero_input(self):
		self.assertEqual(get_primes(0), [])

	def test_no_primes_if_negative_input(self):
		self.assertEqual(get_primes(-10), [])

if __name__ == '__main__':
	unittest.main()

