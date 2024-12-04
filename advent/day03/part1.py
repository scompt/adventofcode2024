def go(input):
	sum = 0
	state = 0
	op1 = ''
	op2 = ''

	for c in input.read().strip():
		if state == 0 and c == 'm':
			state = 1
		elif state == 1 and c == 'u':
			state = 2
		elif state == 2 and c == 'l':
			state = 3
		elif state == 3 and c == '(':
			state = 4
			op1 = ''
		elif state == 4:
			if c == ',':
				state = 5
			else:
				try:
					_ = int(c)
					op1 += c
				except ValueError:
					state = 0
					op1 = ''
					op2 = ''
		elif state == 5:
			if c == ')':
				try:
					sum += int(op1) * int(op2)
					state = 0
					op1 = ''
					op2 = ''
				except ValueError:
					state = 0
					op1 = ''
					op2 = ''
			else:
				try:
					_ = int(c)
					op2 += c
				except ValueError:
					state = 0
					op1 = ''
					op2 = ''
		else:
			state = 0
		
	return sum
