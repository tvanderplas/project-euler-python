
import unittest
from pe_03 import get_primes, get_prime_factors

class get_primes_tests(unittest.TestCase):

	def test_primes_under_20(self):
		self.assertEqual(get_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])

	def test_no_primes_under_1(self):
		self.assertEqual(get_primes(1), [])

	def test_no_primes_if_zero_input(self):
		self.assertEqual(get_primes(0), [])

	def test_no_primes_if_negative_input(self):
		self.assertEqual(get_primes(-10), [])

class get_prime_factors_tests(unittest.TestCase):

	def test_prime_factors_of_2(self):
		self.assertEqual(get_prime_factors(2), [2])

	def test_prime_factors_of_3(self):
		self.assertEqual(get_prime_factors(3), [3])

	def test_prime_factors_of_4(self):
		self.assertEqual(get_prime_factors(4), [2, 2])

	def test_prime_factors_of_5(self):
		self.assertEqual(get_prime_factors(5), [5])

	def test_prime_factors_of_6(self):
		self.assertEqual(get_prime_factors(6), [2, 3])

	def test_prime_factors_of_7(self):
		self.assertEqual(get_prime_factors(7), [7])

	def test_prime_factors_of_8(self):
		self.assertEqual(get_prime_factors(8), [2, 2, 2])

	def test_prime_factors_of_9(self):
		self.assertEqual(get_prime_factors(9), [3, 3])

	def test_prime_factors_of_10(self):
		self.assertEqual(get_prime_factors(10), [2, 5])

	def test_prime_factors_of_11(self):
		self.assertEqual(get_prime_factors(11), [11])

	def test_prime_factors_of_12(self):
		self.assertEqual(get_prime_factors(12), [2, 2, 3])

	def test_prime_factors_of_13(self):
		self.assertEqual(get_prime_factors(13), [13])

	def test_prime_factors_of_14(self):
		self.assertEqual(get_prime_factors(14), [2, 7])

	def test_prime_factors_of_15(self):
		self.assertEqual(get_prime_factors(15), [3, 5])

	def test_prime_factors_of_16(self):
		self.assertEqual(get_prime_factors(16), [2, 2, 2, 2])

	def test_prime_factors_of_17(self):
		self.assertEqual(get_prime_factors(17), [17])

	def test_prime_factors_of_18(self):
		self.assertEqual(get_prime_factors(18), [2, 3, 3])

	def test_prime_factors_of_19(self):
		self.assertEqual(get_prime_factors(19), [19])

	def test_prime_factors_of_20(self):
		self.assertEqual(get_prime_factors(20), [2, 2, 5])

	def test_prime_factors_of_34(self):
		self.assertEqual(get_prime_factors(34), [2, 17])

	def test_prime_factors_of_100(self):
		self.assertEqual(get_prime_factors(100), [2, 2, 5, 5])

	def test_prime_factors_of_104677(self):
		self.assertEqual(get_prime_factors(104677), [104677])

	def test_prime_factors_of_bignasty(self):
		self.assertEqual(get_prime_factors(600851475143), [71, 839, 1471, 6857])

	def test_prime_factors_of_1(self):
		self.assertEqual(get_prime_factors(1), [])

	def test_prime_factors_of_0(self):
		self.assertEqual(get_prime_factors(0), [])

	def test_prime_factors_of_negative_input(self):
		self.assertEqual(get_prime_factors(-10), [])

if __name__ == '__main__':
	unittest.main()

