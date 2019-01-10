# -*- coding: utf-8 -*-

def getTriangleNumber(n):
    return n * (n + 1) / 2


def getPentagonalNumber(n):
    return n * (3 * n - 1) / 2


def getHexagonalNumber(n):
    return n * (2 * n - 1)


if __name__ == '__main__':
    count = 286
    found = False
    idxForTriangle = 286
    idxForPentagonal = 166
    idxForHexagonal = 144
    while True:
        t = getTriangleNumber(count)
        for i in range(idxForPentagonal, count):
            p = getPentagonalNumber(i)
            if p > t:
                idxForPentagonal = i
                break

            if p == t:
                for j in range(idxForHexagonal, i):
                    h = getHexagonalNumber(j)
                    if h > p:
                        idxForHexagonal = j
                        break

                    if h == p:
                        found = True
                        print('{} {} {} {}'.format(t, count, i, j))
                        break
            
        if found:
            break
        count += 1

