

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

biggest = 0
for x in range(100, 1000):
	for y in range(100, 1000):
		p = str(x * y)
		if p == p[::-1] and int(p) > biggest:
			biggest = int(p)
			print(x, y, p)