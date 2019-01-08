# -*- coding: utf-8 -*-

if __name__ == '__main__':
    l = [[0 for i in range(21)] for i in range(21)]

    for col in range(21):
        l[0][col] = 1

    for row in range(21):
        l[row][0] = 1

    for row in range(1, 21):
        for col in range(1, 21):
            l[row][col] = l[row - 1][col] + l[row][col - 1]


    print(l[20][20])
