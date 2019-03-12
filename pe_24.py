

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from pe_functions import factorial

def permutations(word: str):
	if len(word) < 2:
		return [word]
	base = word[:2]
	answer = []
	answer.extend([base, base[::-1]])
	next_answer = []
	for x in range(2, len(word)):
		for item in answer:
			for n in range(len(item) + 1):
				an_item = list(item)
				an_item.insert(n, word[x])
				next_answer.append(''.join([x for x in an_item]))
		answer.clear()
		answer.extend(next_answer)
		next_answer.clear()
		answer.sort()
	return answer

if __name__ == '__main__':
	answer = permutations('0123456789')
	print(answer[999999])
