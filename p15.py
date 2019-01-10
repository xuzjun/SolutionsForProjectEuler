# -*- coding: utf-8 -*-


def countRoutes(m, n):  # grid[ m x n ]
    l = [[0 for i in range(m + 1)] for i in range(n + 1)]

    for col in range(m + 1):
        l[0][col] = 1

    for row in range(n + 1):
        l[row][0] = 1

    for row in range(1, m + 1):
        for col in range(1, n + 1):
            l[row][col] = l[row - 1][col] + l[row][col - 1]

    return l[m][n]


if __name__ == '__main__':

    r = countRoutes(20, 20)

    print(r)
