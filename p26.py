# -*- coding: utf-8 -*-

def getRecurringCycleLen(n):
	numerator = 1
	a = []
	idx = 0
	while numerator > 0:
		while numerator < n:
			numerator *= 10
			idx += 1

		for i in range(len(a)):
			if a[i][0] == numerator:
				return idx - a[i][1]

		a.append((numerator, idx))
		numerator %= n
		quotient = numerator / n

	return 0

if __name__ == '__main__':
	max = 0 
	for i in range(2, 1000):
		l = getRecurringCycleLen(i)
		if l > max:
			max = l
			print('{} {}'.format(i, l))
	
	print(max)
