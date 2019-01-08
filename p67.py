#-*- coding: utf-8 -*-

def readData():
	path = 'p067_triangle.txt'
	r = []
	with open(path) as f:
		lines = f.readlines()
		for line in lines:
			a = [int(x) for x in line.split(' ')]
			r.append(a)

	return r


if __name__ == '__main__':
	b = readData()
	print('----{}'.format(len(b)))
	end = 0
	for arr in b:
		print (arr)
	for i in range(1, len(b)):
		for j in range(i + 1):
			if j == 0:
				b[i][j] += b[i - 1][j]
			elif j == i:
				b[i][j] += b[i - 1][j - 1]
			else:	
				b[i][j] += b[i - 1][j - 1] if (b[i - 1][j - 1] > b[i - 1][j]) else b[i - 1][j]

	for arr in b:
		print (arr)

	print(max(b[99]))

