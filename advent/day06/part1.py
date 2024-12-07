DIRECTIONS = ['<', '^', '>', 'v']
MOVEMENT = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def next_direction(guard_position):
	next_direction = (guard_position[1] + 1) % len(DIRECTIONS)	
	return guard_position[0], next_direction

def next_position(guard_position):
	movement = MOVEMENT[guard_position[1]]
	position = guard_position[0]
	return (position[0] + movement[0], position[1] + movement[1]), guard_position[1]

def go(input):

	blocks = []
	guard_position = None

	height = 0
	width = 0
	for y, line in enumerate(input.readlines()):
		height += 1
		line = line.strip()
		width = len(line)

		for x, c in enumerate(line):
			if c == '#':
				blocks.append((x, y))
			elif c in DIRECTIONS:
				guard_position = ((x, y), DIRECTIONS.index(c))
	# print(height, width, blocks, guard_position)

	grid_size = (width, height)
	visited = set()

	while guard_position[0][0] >= 0 and guard_position[0][0] < grid_size[0] and \
	  guard_position[0][1] >= 0 and guard_position[0][1] < grid_size[1]:
		# print(guard_position)
		visited.add(guard_position[0])

		position = guard_position
		while next_position(position)[0] in blocks:
			# print('hit!')
			position = next_direction(position)
			# print('turned: %s' % str(position))
		guard_position = next_position(position)
	
	return len(visited)
