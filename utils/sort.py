# -*- coding: utf-8 -*-

import random


def compare(a, b):
    if a > b: return 1
    if a == b: return 0
    if a < b: return -1


def partition(arr, low, high, compare):
    x = arr[low]
    i = low
    for j in range(low + 1, high + 1):
        if compare(arr[j], x) < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[i] = arr[i], arr[low]
    return i


def randomPartition(arr, low, high, compare):
    middle = int(low + random.random() * (high - low))
    arr[middle], arr[low] = arr[low], arr[middle]
    return partition(arr, low, high, compare)
    

def qsort(arr, low, high, compare=compare):
    if low < high:
        middle = randomPartition(arr, low, high, compare)
        qsort(arr, low, middle - 1, compare)
        qsort(arr, middle + 1, high, compare)


