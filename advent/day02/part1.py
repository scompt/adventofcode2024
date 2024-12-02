def go(input):
	reports = []
	for line in input.readlines():
		levels = [int(l) for l in line.strip().split()]
		reports.append(levels)

	safe_count = 0
	for report in reports:
		if all(this != that for this, that in zip(report, report[1:])) \
		  and all(abs(this-that) <= 3 for this, that in zip(report, report[1:])) \
		  and (all(this < that for this, that in zip(report, report[1:])) or \
		  all(this > that for this, that in zip(report, report[1:]))):
			safe_count += 1
		
	return safe_count
