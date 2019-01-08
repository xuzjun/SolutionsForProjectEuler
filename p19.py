#-*- coding: utf-8 -*-

daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapYearDays = 366
yearDays = 365
daysBeforeYear = []


def isLeapYear(n):
	return (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)


def fillDaysBeforeYear():
	daysBeforeYear.append(0)
	daysOfYear = [0 for x in range(101)]
	for y in range(1900, 2001):
		daysOfYear[y - 1900] = (sum(daysOfMonth) + 1) if isLeapYear(y) else sum(daysOfMonth)
		if y > 1900:
			daysBeforeYear.append(daysBeforeYear[y - 1900 - 1] + daysOfYear[y - 1900 - 1])


def daysOfYear(y, m, d):
	days = 0
	if m == 0:
		return d + 1
	else:
		for i in range(m):
			days += daysOfMonth[i] + d + 1

		if isLeapYear(y):
			days += 1

	return days


def daysFrom1900(yyyy, mm, dd):
	r = 0
	r += daysBeforeYear[yyyy - 1900]
	r += daysOfYear(yyyy, mm, dd)
	return r


if __name__ == '__main__':
	fillDaysBeforeYear()
	print('--{}--'.format(daysFrom1900(1900,0,0)))
	print('--{}--'.format(daysFrom1900(1900,1,1)))
	print('--{}--'.format(daysFrom1900(1901,0,1)))

	r = 0
	for y in range(1900, 2001):
		for m in range(12):
			if daysFrom1900(y, m, 0) % 7 == 0:
				r += 1

	print(r)
