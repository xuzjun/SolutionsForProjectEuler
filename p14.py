# -*- coding: utf-8 -*-

if __name__ == '__main__':
	m = 0
	for i in range(2, 1000000):
		j = i
		c = 0
		while True:
			c += 1
			if j == 1:
				break

			if j % 2 == 0:
				j = j / 2
			else:
				j = j * 3 + 1

		if m < c:
			m = c
			print('{} {}'.format(i, m))

	print(m)
