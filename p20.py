# -*- coding:utf-8 -*-

if __name__ == '__main__':
	p = 1
	for i in range(1, 101):
		p *= i

	s = str(p)
	a = [int(x) for x in s]
	print(sum(a))
		
