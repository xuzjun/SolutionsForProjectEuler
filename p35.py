# -*- coding: utf-8 -*-


from utils import prime


def isCircularPrimes(n):
    if n < 20:
        return True

    q = n
    p = 10
    w = 1
    while True:
        if q / p != 0:
            w += 1
        else:
            break
        p *= 10

    p = 10 ** (w - 1)
    while w > 1:
        w -= 1
        n = (n % p) * 10 + n / p
        if not prime.isPrime(n):
            return False
    
    return True


if __name__ == '__main__':
    r = 0
    for i in prime.getPrime():
        if i >= 1000000:
            break

        if isCircularPrimes(i):
            r += 1

    print(r)
