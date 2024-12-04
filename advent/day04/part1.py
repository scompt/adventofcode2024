from operator import itemgetter

def go(input):
	field = {}

	lines = input.readlines()
	for y, line in enumerate(lines):
		for x, c in enumerate(line.strip()):
			field[(x, y)] = c
	maxx= max(field.keys(), key=itemgetter(0))[0] + 1
	maxy= max(field.keys(), key=itemgetter(1))[1] + 1

	def get(x, y):
		if x<0 or x>=maxx or y<0 or y>=maxy:
			return ''
		else:
			return field[(x, y)]
	
	count = 0
	asdf = list()
	for xstart in range(maxx):
		for ystart in range(maxy):
			for xdelta in (-1,0,1):
				for ydelta in (-1,0,1):
					if get(xstart+xdelta*0, ystart+ydelta*0) == 'X' and \
					   get(xstart+xdelta*1, ystart+ydelta*1) == 'M' and \
					   get(xstart+xdelta*2, ystart+ydelta*2) == 'A' and \
					   get(xstart+xdelta*3, ystart+ydelta*3) == 'S':
						asdf.append((xstart, ystart, xdelta, ydelta))

	return len(asdf)

