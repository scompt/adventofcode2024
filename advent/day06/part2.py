DIRECTIONS = ['<', '^', '>', 'v']
MOVEMENT = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def next_direction(guard_position):
	next_direction = (guard_position[1] + 1) % len(DIRECTIONS)	
	return guard_position[0], next_direction

def next_position(guard_position):
	movement = MOVEMENT[guard_position[1]]
	position = guard_position[0]
	return (position[0] + movement[0], position[1] + movement[1]), guard_position[1]



def trytrytry(guard_position, grid_size, blocks):
	visited = set()
	visited_with_direction = set()
	
	while guard_position[0][0] >= 0 and guard_position[0][0] < grid_size[0] and \
	  guard_position[0][1] >= 0 and guard_position[0][1] < grid_size[1] and \
	  guard_position not in visited_with_direction:
	
		visited.add(guard_position[0])
		visited_with_direction.add(guard_position)

		position = guard_position
		prev_position = guard_position
		while next_position(position)[0] in blocks:
			position = next_direction(position)
		guard_position = next_position(position)
	
	return guard_position in visited_with_direction


def go(input):

	blocks = set()
	guard_position = None

	height = 0
	width = 0
	for y, line in enumerate(input.readlines()):
		height += 1
		line = line.strip()
		width = len(line)

		for x, c in enumerate(line):
			if c == '#':
				blocks.add((x, y))
			elif c in DIRECTIONS:
				guard_position = ((x, y), DIRECTIONS.index(c))
	grid_size = (width, height)
	possible_blocks = set()

	for y in range(height):
		for x in range(width):
			possible_block = (x,y)
			if possible_block in blocks or guard_position[0] == possible_block:
				pass
			poss = set()
			poss.add((x, y))
			blocks_with_possible = blocks.union(poss) 
			trapped = trytrytry(guard_position, grid_size, blocks_with_possible)
			if trapped:
				possible_blocks.add(possible_block)
	return len(possible_blocks)
