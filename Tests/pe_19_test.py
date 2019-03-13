import context
from Challenges.functions import is_leap_year, days_in_month
import unittest

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

class days_in_month_test(unittest.TestCase):

	def test_months_if_not_leap_year(self):
		self.assertEqual(days_in_month(1, 1999), 31)
		self.assertEqual(days_in_month(2, 1999), 28)
		self.assertEqual(days_in_month(3, 1999), 31)
		self.assertEqual(days_in_month(4, 1999), 30)
		self.assertEqual(days_in_month(5, 1999), 31)
		self.assertEqual(days_in_month(6, 1999), 30)
		self.assertEqual(days_in_month(7, 1999), 31)
		self.assertEqual(days_in_month(8, 1999), 31)
		self.assertEqual(days_in_month(9, 1999), 30)
		self.assertEqual(days_in_month(10, 1999), 31)
		self.assertEqual(days_in_month(11, 1999), 30)
		self.assertEqual(days_in_month(12, 1999), 31)

	def test_months_if_leap_year(self):
		self.assertEqual(days_in_month(1, 2016), 31)
		self.assertEqual(days_in_month(2, 2016), 29)
		self.assertEqual(days_in_month(3, 2016), 31)
		self.assertEqual(days_in_month(4, 2016), 30)
		self.assertEqual(days_in_month(5, 2016), 31)
		self.assertEqual(days_in_month(6, 2016), 30)
		self.assertEqual(days_in_month(7, 2016), 31)
		self.assertEqual(days_in_month(8, 2016), 31)
		self.assertEqual(days_in_month(9, 2016), 30)
		self.assertEqual(days_in_month(10, 2016), 31)
		self.assertEqual(days_in_month(11, 2016), 30)
		self.assertEqual(days_in_month(12, 2016), 31)

if __name__ == '__main__':
	unittest.main()

