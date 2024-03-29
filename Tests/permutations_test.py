import context
import unittest
from Challenges.functions import permutations, factorial

class permutations_test(unittest.TestCase):

	def test_permutations_of_0(self):
		self.assertEqual(permutations('0'), ['0'])
	def test_permutations_length_1(self):
		self.assertEqual(len(permutations('0')), factorial(1))
	
	def test_permutations_of_01(self):
		self.assertEqual(permutations('01'), ['01','10'])
	def test_permutations_length_2(self):
		self.assertEqual(len(permutations('01')), factorial(2))
		
	def test_permutations_of_012(self):
		self.assertEqual(permutations('012'), ['012', '021', '102', '120', '201', '210'])
	def test_permutations_length_3(self):
		self.assertEqual(len([int(x) for x in permutations('012')]), factorial(3))

	def test_permutations_of_ABCD(self):
		self.assertEqual(permutations('ABCD'), 
			['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADBC', 'ADCB',
			'BACD', 'BADC', 'BCAD', 'BCDA', 'BDAC', 'BDCA',
			'CABD', 'CADB', 'CBAD', 'CBDA', 'CDAB', 'CDBA',
			'DABC', 'DACB', 'DBAC', 'DBCA', 'DCAB', 'DCBA'])
	def test_permutations_length_4(self):
		self.assertEqual(len([int(x) for x in permutations('0123')]), factorial(4))

if __name__ == '__main__':
	unittest.main()


