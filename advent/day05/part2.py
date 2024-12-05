from collections import defaultdict

def test_report(report, rules, reverse_rules):
	for i in range(len(report)-1, -1, -1):
		for j in range(i, -1, -1):
			if report[j] in rules[report[i]]:
				return False
	return True
	
def fix_report(report, rules):
	swapped = report
	while True:
		swapped, report = None, swapped
		for i in range(len(report)-1, -1, -1):
			for j in range(i-1, -1, -1):
				if not swapped and report[j] in rules[report[i]]:
					swapped = report[:]
					swapped[i], swapped[j] = swapped[j], swapped[i]	
		if not swapped:
			break

	return report

def go(input):
	lines = input.readlines()

	rules = defaultdict(lambda: [])
	reverse_rules = defaultdict(lambda: [])
	while True:
		line = lines.pop(0).strip()
		if not line:
			break

		left, right = line.split('|', 2)
		rules[int(left)].append(int(right))
		reverse_rules[int(right)].append(int(left))

	reports = []
	while True:
		try:
			line = lines.pop(0).strip()
		except IndexError:
			break

		if not line:
			break

		reports.append([int(val) for val in line.split(',')])

	correct = 0
	for report in reports:
		if not test_report(report, rules, reverse_rules):
			fixed = fix_report(report, rules)
			correct += fixed[len(fixed)//2]

	return correct
