

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for c in range(2, 999):
	for b in range(2, 999):
		if c + b < 1000:
			a = 1000 - (c + b)
			if a**2 + b**2 == c**2 and a < b < c:
				print(a * b * c)