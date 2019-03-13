
import context
import unittest
from Challenges.functions import days_in_month

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

