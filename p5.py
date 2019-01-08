#-*- coding: utf-8 -*-
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)


def lcm(x, y):
    return x * y / gcd(x, y)


if __name__ == '__main__':
    lcmOfFirstTen = 2520
    tmpLCM = 2520
    for i in range(11, 21):
        tmpLCM = lcm(tmpLCM, i)
   
    print(tmpLCM)
