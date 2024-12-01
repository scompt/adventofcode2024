from collections import defaultdict

def go(input):
	lefts = []
	rights = []
	
	for line in input.readlines():
		l, r = line.strip().split(None, 2)
		lefts.append(int(l))
		rights.append(int(r))
	
	left_counts = defaultdict(lambda: 0)
	right_counts = defaultdict(lambda: 0)
	
	for alist, counts in [(lefts, left_counts), (rights, right_counts)]:
		for num in alist:
			counts[num] += 1
	
	similarity = 0
	for num, count in left_counts.items():
		similarity += num * count * right_counts[num]

	return similarity

