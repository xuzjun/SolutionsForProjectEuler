# -*- coding: utf-8 -*-


def fab(max):
	n, a, b = 0, 0, 1
	while a + b < max:
		yield a + b
		a, b = b, a + b
		n += 1


if __name__ == '__main__':
	sum = 0
	j = 0
	for i in fab(4000000):
		if i % 100000 == 0:
			j += 1
			print(j)
		if i % 2 == 0:
			sum += i

	print(sum)
