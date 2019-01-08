# -*- coding: utf-8 -*-

import math

def isPrime(n):
	if n < 2: return False
	if n == 2: return True

	if n % 2 == 0: return False

	sqrt = int(math.ceil(math.sqrt(n)))
	for i in range(3, sqrt + 1, 2):
		if n % i == 0:
			return False

	return True
	

def divisorNumber(n):
	sqrt = int(math.ceil(math.sqrt(n)))
	a = n
	r = []
	for i in range(2, sqrt + 1): 
		if isPrime(i): 
			c = 0
			while a % i == 0:
					c += 1
					a = a / i
			if c > 0:
				r.append(c)

	p = 1
	for i in r:
		p *= i + 1

	return p


if __name__ == '__main__':
	count = 0
	tn = 0
	while True:
		count += 1
		tn += count
		r = divisorNumber(tn)

		print('{} {}'.format(tn, r))
		if r >= 500:
			break

	print(tn)
