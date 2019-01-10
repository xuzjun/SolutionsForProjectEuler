# -*- coding: utf-8 -*-


def readData():
    r = []
    with open('p042_words.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace(' ', '')
            line = line.replace('"', '')
            words = line.split(',')
            for w in words:
                r.append(w)
            
    return r


def getTriangleNumber():
    n = 1
    while True:
        yield n * (n + 1) / 2
        n += 1
        

S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if __name__ == '__main__':
    words = readData()
    wordValue = []
    for w in words:
        v = 0
        for c in w:
            v += S.index(c) + 1
        wordValue.append(v)

    triangleNumbers = []
    maxValue = max(wordValue) 
    for n in getTriangleNumber():
        if n > maxValue:
            break

        triangleNumbers.append(n)

    s = 0
    for v in wordValue:
        if v in triangleNumbers:
            s += 1

    print(s)
