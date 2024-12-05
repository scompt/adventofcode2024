from collections import defaultdict

def test_report(report, rules, reverse_rules):
	for i in range(len(report)-1, -1, -1):
		for j in range(i, -1, -1):
			if report[j] in rules[report[i]]:
				return False
	return True
	
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
		if test_report(report, rules, reverse_rules):
			correct += report[len(report)//2]
		# print(report, test_report(report, rules, reverse_rules))

	return correct
