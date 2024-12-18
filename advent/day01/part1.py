def go(input):
	lefts = []
	rights = []
	
	for line in input.readlines():
		l, r = line.strip().split(None, 2)
		lefts.append(int(l))
		rights.append(int(r))
	
	lefts.sort()
	rights.sort()
	
	total_dist = 0
	for l, r in zip(lefts, rights):
		dist = abs(l-r)
		total_dist += dist
	
	return total_dist
