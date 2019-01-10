# -*- coding: utf-8 -*-

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 
# 9 = 7 + 2 * (1 ** 2)
# 15 = 7 + 2 * (2 ** 2)
# 21 = 3 + 2 * (3 ** 2)
# 25 = 7 + 2 * (3 ** 2)
# 27 = 19 + 2 * (2 ** 2)
# 33 = 31 + 2 * (1 ** 2)
# 
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


from utils import prime


def isASquare(n):
    for i in range(1, n / 2):
        if n == i ** 2:
            return True
        if i ** 2 > n:
            break

    return False


def isTwiceASquare(n):
    if n == 0: return True
    if n == 1 : return False
    if n % 2 != 0: return False

    q = n / 2
    return isASquare(q)


if __name__ == '__main__':
    n = 35
    while True:
        for i in range(n, 0, -1):
            if prime.isPrime(i) and isTwiceASquare(n - i):
                break
        if i == 1:
            print('{} {} {}'.format(n, i, n - i))
            exit()

        n += 2
