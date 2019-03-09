

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.


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

if __name__ == '__main__':
	print(sum([count_letters(x) for x in range(1, 1001)]))

