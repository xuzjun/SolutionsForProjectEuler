# -*- coding: utf-8 -*-

if __name__ == '__main__':
	arr = []
	for p in range(3, 1001):
		count = 0
		for a in range(1, p / 2):
			for b in range(1, p / 2):
				c = p - a - b
				if c > 0 and a + b > c and a + c > b and b + c > a \
                   and a ** 2 + b ** 2 == c ** 2:
					print('{} {} {} {}'.format(p, a, b, c))
					count += 1
		arr.append((p, count / 2))

	print('*' * 23)
	max = 0
	for i, j in arr:
		if j > max:
			max = j
			print('{} {}'.format(i, j))
		
