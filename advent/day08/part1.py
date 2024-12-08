from collections import defaultdict
from itertools import combinations

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
			possibles = [(pair[1][0]+slope[0], pair[1][1]+slope[1]), (pair[0][0]-slope[0], pair[0][1]-slope[1])]
			# print(c, pair, slope, possibles)
			for possible in possibles:
				if possible[0] >= 0 and possible[0] < fieldsize[0] and \
				   possible[1] >= 0 and possible[1] < fieldsize[1]:
					antinodes.add(possible)
			
	return len(antinodes)
