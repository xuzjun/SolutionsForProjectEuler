# -*- coding: utf-8 -*-

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


a = [12]
def isAbundantNumber(n):
    if n in a: return True
    if n < a[-1]: return False
    s = 0
    for i in range(1, n / 2 + 1):
        if n % i == 0:
            s += i

    if s > n:
        a.append(n)
        return True

    return False


if __name__ == '__main__':
    s = 0
    for i in range(1, 28124):
        can = 0
        for j in range(12, i / 2 + 1):
            if isAbundantNumber(j) and isAbundantNumber(i - j):
                can = 1
                break
        if can == 0:
            s += i

    print(s)
