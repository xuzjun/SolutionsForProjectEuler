# -*- coding: utf-8 -*-

def addTwoArrayAsInteger(a, b, c):
	flag = 0
	for i in range(1000):
		c[i] = (a[i] + b[i] + flag) % 10
		flag = (a[i] + b[i] + flag) / 10


if __name__ == '__main__':
	a = [0 for i in range(1001)]
	b = [0 for i in range(1001)]
	c = [0 for i in range(1001)]

	a[0] = 1
	b[0] = 1
	i = 3
	while True:
		addTwoArrayAsInteger(a, b, c)
		if c[999] != 0:
			print(c)
			print(i)
			break
		tmp = a
		a = b
		b = c
		c = tmp
		i += 1

