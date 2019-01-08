# -*- coding: utf-8 -*-


from utils import palindromic


def getBinaryListOf(n):
    a = []
    while n > 1: 
        a.append(n % 2)
        n = n / 2 
    
    a.append(n)
    a = a[::-1]
    return a


if __name__ == '__main__':
    s = 0
    for n in range(1000000):
        l = getBinaryListOf(n)
        if palindromic.isPalindromicList(l) and palindromic.isPalindromicNumber(n):
            s += n

    print(s)
