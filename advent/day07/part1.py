from functools import reduce
from operator import add

def trytry(total, numbers):
	# print()
	for i in range(2**(len(numbers)-1)):
		# print('i: %d' % i)
		running_total = numbers[0]
		# print('%s%d' % ('('*(len(numbers)-1), running_total), end='')

		x = i
		for number in numbers[1:]:
			# print(' x: %d' % x)
			if x % 2 == 0:
				# print('+%d)' % number, end='')
				running_total += number
			else:
				# print('*%d)' % number, end='')
				running_total *= number
			x //= 2
		# print('=%d %d %s' % (running_total, total, running_total == total))
		if running_total == total:
			return True
	return False

def go(input):
	stuff = []
	for line in input.readlines():
		total, numbers = line.strip().split(':', 1)
		numbers = [int(n) for n in numbers.strip().split(' ')]
		total = int(total)
		stuff.append((total, numbers))

	sum = 0
	for total, numbers in stuff:
		if trytry(total, numbers):
			sum += total
	
	return sum
