# -*- coding: utf-8 -*-

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 
# 43 44 45 46 47 48 49
# 42 21 22 23 24 25 26
# 41 20  7  8  9 10 27 
# 40 19  6  1  2 11 28
# 39 18  5  4  3 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?



if __name__ == '__main__':
    sv = [[0 for i in range(4)] for i in range(501)]
    sv[0][3] = 1
    for i in range(1, 501):
        sv[i][3] = sv[i - 1][3] + i * 8
        sv[i][2] = sv[i][3] - 2 * i
        sv[i][1] = sv[i][2] - 2 * i
        sv[i][0] = sv[i][1] - 2 * i

    s = 0
    for arr in sv:
        for i in arr:
            s += i

    print(s)

