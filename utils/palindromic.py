# -*- coding: utf-8 -*-

def isPalindromicList(l):
    ll = l[::-1]
    for i, j in zip(l, ll):
        if i != j:
            return False

    return True


def isPalindromicString(s):
    a = list(s)
    return isPalindromicList(a)


def isPalindromicNumber(n):
    return isPalindromicString(str(n))
