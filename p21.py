# -*- coding: utf-8 -*-

if __name__ == '__main__':
	d = [0 for i in range(10000)]
	for i in range(1, 10000):
		a = []
		for j in range(1, i / 2 + 1):
			if i % j == 0:
				a.append(j)

		d[i] = sum(a)

	print('220[{}] 284[{}]'.format(d[220], d[284]))
	r = 0
	for i in range(1, 10000):
		if d[i] < 10000 and i == d[d[i]] and i != d[i]:
			print(i)
			r += i

	print(r)
