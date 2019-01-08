# -*- coding: utf-8 -*-

import math

def isPrime(n):
	if n % 2 == 0:
		return False

	a = int(math.sqrt(n)) + 1
	for i in range(3, a, 2):
		if n % i == 0:
			return False

	return True


if __name__ == '__main__':
	#a = 13195
	a = 600851475143
	b = int(math.sqrt(a)) + 1

	sum = 0
	for i in range(2, b):
		if a % i == 0 and isPrime(i):
			print(i)
			sum += i

	print(sum)

