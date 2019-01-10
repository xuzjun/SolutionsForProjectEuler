# -*- coding: utf-8 -*-

# The series, 1 ** 1 + 2 ** 2 + 3 ** 3 + ... + 10 ** 10 = 10405071317.
# 
# Find the last ten digits of the series, 1 ** 1 + 2 ** 2 + 3 ** 3 + ... + 1000 ** 1000.


# (X * Y) mod P = ((X mod P) * (Y mod P)) mod P
# (X + Y) mod P = ((X mod P) + (Y mod P)) mod P


P = 10000000000


def getModOfSquare(n):
    m = n
    for i in range(n - 1):
        m = ((m % P) * (n % P)) % P

    return m


if __name__ == '__main__':
    last = 1
    for i in range(2, 1001):
        m1 = getModOfSquare(i)
        last = (last + m1) % P

    print(last)
