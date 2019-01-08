# -*- coding: utf-8 -*-


# Euler discovered the remarkable quadratic formula:
# 
# n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
# 
# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
# 
# Considering quadratics of the form:
# 
# n2+an+b, where |a|<1000 and |b|≤1000
# 
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
# 

import utils.sort


if __name__ == '__main__':
    a = set()
    for i in range(0, 80):
        a.add(i ** 2 - 79 * i + 1601)

    a = list(a)
    utils.sort.qsort(a, 0, len(a) - 1)
    print(a)
    print(len(a))
