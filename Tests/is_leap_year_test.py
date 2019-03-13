
import context
import unittest
from Challenges.functions import is_leap_year

class is_leap_year_test(unittest.TestCase):

	def test_years_not_divisible_by_4_are_not_leap_years(self):
		self.assertFalse(is_leap_year(1))
		self.assertFalse(is_leap_year(2006))
		self.assertFalse(is_leap_year(1999))

	def test_years_divisible_by_4_are_leap_years(self):
		self.assertTrue(is_leap_year(0))
		self.assertTrue(is_leap_year(4))
		self.assertTrue(is_leap_year(1992))
		self.assertTrue(is_leap_year(2016))

	def test_years_divisible_by_400_are_leap_years(self):
		self.assertTrue(is_leap_year(400))
		self.assertTrue(is_leap_year(2000))
		self.assertTrue(is_leap_year(2400))

	def test_years_divisible_by_100_but_not_400_are_not_leap_years(self):
		self.assertFalse(is_leap_year(100))
		self.assertFalse(is_leap_year(1900))
		self.assertFalse(is_leap_year(1800))

if __name__ == '__main__':
	unittest.main()

