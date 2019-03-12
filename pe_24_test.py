from pe_24 import permutations
import unittest

class permutations_test(unittest.TestCase):

	def test_permutations_length_1(self):
		self.assertEqual(permutations('0'), ['0'])
	def test_permutations_length_2(self):
		self.assertEqual(permutations('01'), ['01','10'])
	def test_permutations_length_3(self):
		self.assertEqual(permutations('012'), ['012', '021', '102', '120', '201', '210'])




if __name__ == '__main__':
	unittest.main()


