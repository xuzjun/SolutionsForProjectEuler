# -*- coding: utf-8 -*-

import math

def isPrime(n):
    if n < 2: return False 
    if n == 2: return True
    if n % 2 == 0: return False

    sq = int(math.sqrt(n)) + 1
    for i in range(3, sq, 2):
        if n % i == 0:
            return False

    return True


def getPrime():
    n = 2
    while True:
        if isPrime(n):
            yield n
        n += 1


if __name__ == '__main__':
    sum = 0
    for i in getPrime():
        if i < 2000000:
            sum += i
        else:
            break

    print(sum)
