# -*- coding: utf-8 -*-


from utils import prime


def truncatableL2R(p):
    coefficient = 10
    m = 0
    while m < p:
        m = p % coefficient
        if not prime.isPrime(m):
            return False

        coefficient *= 10

    return True


def truncatableR2L(p):
    coefficient = 10
    q = p
    while q > 10:
        q = p / coefficient
        if not prime.isPrime(q):
            return False

        coefficient *= 10

    return True


if __name__ == '__main__':
    count = 0
    s = 0
    for p in prime.getPrime():
        if p >= 23 and truncatableL2R(p) and truncatableR2L(p):
            print(p)
            count += 1
            s += p
        if count == 11:
            break

    print(s)
