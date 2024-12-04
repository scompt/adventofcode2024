def go(input):
	instructions = input.read().strip()
	pointer = 0
	enabled = True

	sum = 0
	state = 0
	op1 = ''
	op2 = ''

	while pointer < len(instructions):
		c = instructions[pointer]

		if instructions[pointer:pointer+4] == 'mul(' and enabled:
			pointer += 4
			state = 1
			op1 = ''

		elif instructions[pointer:pointer+4] == 'do()':
			pointer += 4
			enabled = True
			
		elif instructions[pointer:pointer+7] == "don't()":
			pointer += 7
			enabled = False
			
		elif state == 1:
			pointer += 1
			if c == ',':
				state = 2
			else:
				try:
					_ = int(c)
					op1 += c
				except ValueError:
					state = 0
					op1 = ''
					op2 = ''
		elif state == 2:
			pointer += 1
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
			pointer += 1
			state = 0
		
	return sum
