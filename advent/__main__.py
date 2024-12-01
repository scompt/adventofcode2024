import glob
import importlib

def matches(actual, expected):
	if type(actual) is int:
		expected = int(expected)
	return actual == expected

for day in range(1, 26):
	day_printed = False
	for part in (1, 2):
		mod_name = "advent.day%02d.part%d" % (day, part)
		test_glob = 'advent/day%02d/test%d.*.in' % (day, part)
	
		try:
			mod = importlib.import_module(mod_name)
			if not day_printed:
				print('Day %02d' % day)
				day_printed = True
			print('\tPart %d' % part)
			inputs = glob.glob(test_glob)
			for input_filename in inputs:
				with open(input_filename) as input_file:
					actual_output = mod.go(input_file)
				output_filename = input_filename.removesuffix('in') + 'out'
				try:
					output_file = open(output_filename, 'r')
					expected_output = output_file.read().strip()
					
					if matches(actual_output, expected_output):
						print('\t\t✓')
					else:
						print (f'\t\t✘ {actual_output}')
					
				except FileNotFoundError as e:
					print(f'\t\t? {actual_output}')
		except ModuleNotFoundError as e:
			pass
