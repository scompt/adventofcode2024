from collections import defaultdict
from itertools import combinations

def reduce_slope(slope):
	for i in range(2, min(slope[0], slope[1])):
		if slope[0] % i == 0 and slope[1] % i == 0:
			return reduce_slope((slope[0] // i, slope[1] // i))
	return slope

def go(input):
	field = {}
	antennae = defaultdict(lambda: set())

	for y, line in enumerate(input.readlines()):
		for x, c in enumerate(line.strip()):
			if c.isalpha() or c.isdigit():
				field[(x,y)] = c
				antennae[c].add((x,y))
	fieldsize = (x+1, y+1)

	antinodes = set()
	for c, locs in antennae.items():
		for pair in combinations(locs, 2):
			slope = (pair[1][0]-pair[0][0], pair[1][1]-pair[0][1])
			slope = reduce_slope(slope)
			
			loc = pair[1]
			while loc[0] >= 0 and loc[0] < fieldsize[0] and \
			   loc[1] >= 0 and loc[1] < fieldsize[1]:
				antinodes.add(loc)
				loc = (loc[0]+slope[0], loc[1]+slope[1])
			loc = pair[1]
			while loc[0] >= 0 and loc[0] < fieldsize[0] and \
			   loc[1] >= 0 and loc[1] < fieldsize[1]:
				antinodes.add(loc)
				loc = (loc[0]-slope[0], loc[1]-slope[1])
			
	return len(antinodes)
