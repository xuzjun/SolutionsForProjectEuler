# -*- coding: utf-8 -*-


'''
	[one, two, three, four, five, six, seven, eight, nine],
    [ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen],
    ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	[hundred]
'''

one2Nine = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
eleven2Nineteen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tys = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def getStringGEOneThousand(n):
	d = n / 1000
	return one2Nine[d - 1] + ' thousand'

def getStringGEOneHundred(n):
	d = n / 100
	return one2Nine[d - 1] + ' hundred'

def getStringOfGETen(n):
	if n >= 10 and n < 20:
		return eleven2Nineteen[n - 10]
	else:
		if n % 10 > 0:
			return tys[n / 10 - 2] + '-' + one2Nine[n % 10 - 1]
		else:
			return tys[n / 10 - 2]

def digitStringLen(s):
	c = 0
	for i in range(len(s)):
		if s[i] != ' ' and s[i] != '-':
			c += 1

	return c 

if __name__ == '__main__':
	sumLen = 0
	for i in range(1, 1001):
		n = i
		s = ''

		if n >= 1000:
			s += getStringGEOneThousand(n)
			if n % 1000 > 0:
				s += ' and '
			n %= 1000
		if n >= 100:
			s += getStringGEOneHundred(n)
			if n % 100 > 0:
				s += ' and '
			n %= 100
		if n >= 10 and n < 100:
			s += getStringOfGETen(n)
		elif n < 10 and n >= 1:
			s += one2Nine[n - 1]

		sumLen += digitStringLen(s)

	print(sumLen)
