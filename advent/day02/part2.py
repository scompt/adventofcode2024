from itertools import combinations

def test_report(possible_report):
	for report in [possible_report] + list(combinations(possible_report, len(possible_report)-1)):
		if all(this != that for this, that in zip(report, report[1:])) \
		  and all(abs(this-that) <= 3 for this, that in zip(report, report[1:])) \
		  and (all(this < that for this, that in zip(report, report[1:])) or \
		  all(this > that for this, that in zip(report, report[1:]))):
			return True
	return False

def go(input):
	reports = []
	for line in input.readlines():
		levels = [int(l) for l in line.strip().split()]
		reports.append(levels)

	safe_count = 0
	for possible_report in reports:
		if test_report(possible_report):
			safe_count += 1
		
	return safe_count
