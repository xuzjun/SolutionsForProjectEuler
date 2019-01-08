# -*- coding: utf-8 -*-

# Largest palindrome product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#

def isPalindrome(n):
    a1 = list(str(n))[:]
    a2 = list(str(n))[::-1]

    for a, b in zip(a1, a2):
        if a != b:
            return False

    return True


if __name__ == '__main__':
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            p = i * j
            if isPalindrome(p) and p > max:
                max = p

    print(max)
