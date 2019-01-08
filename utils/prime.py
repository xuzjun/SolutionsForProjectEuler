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

