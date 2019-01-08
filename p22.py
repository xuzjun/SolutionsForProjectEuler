# -*- coding: utf-8 -*-


# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?


import private_qsort

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def readData():
    names = []
    with open('p022_names.txt') as f:
        lines = f.readlines()
        for line in lines:
            nl = line.replace('"', '')
            nl = nl.replace(' ', '')
            for n in nl.split(','):
                names.append(n)

    return names


def compare(a, b):
    if a > b: return 1
    if a == b: return 0
    if a < b: return -1


if __name__ == '__main__':
    names = readData()
    private_qsort.qsort(names, 0, len(names) - 1, compare)
    nameIndex = 1
    scores = 0
    for name in names:
        t = 0
        for c in name:
            t += alphabet.index(c) + 1

        scores += nameIndex * t
        nameIndex += 1

    print(scores)
