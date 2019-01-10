# -*- coding: utf-8 -*-


def lenOfNumber(n):
	p = 10
	c = 0
	while n > 0:
		n /= p
		c += 1

	return c


def numberIndexOf(n, i):
	l = lenOfNumber(n)
	d = l - i
	p = 1
	while d > 0:
		p *= 10
		d -= 1
	return (n / p) % 10


if __name__ == '__main__':
	l = 11
	a = [1,1]
	idx = 100
	for i in range(11, 1000001):
		l1 = lenOfNumber(i)
		if l1 + l >= idx:
			d = idx - l
			n = numberIndexOf(i, d)
			print(i)
			a.append(n)
			idx *= 10
			if idx > 1000000:
				break
		l += l1

	print(a)
	p = 1
	for i in a:
		p *= i

	print(p)

