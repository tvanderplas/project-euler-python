

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

def catalan(x: int):
	pascal = [1, 1]
	for n in range(x * 2 - 1):
		pascal = [pascal[i] + pascal[i + 1] for i, v in enumerate(pascal) if i != len(pascal) - 1]
		pascal.append(1)
		pascal.insert(0, 1)
	return pascal[len(pascal) // 2]

if __name__ == '__main__':
	print(catalan(20))
