#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:32:12 2020

@author: karanwaghela
"""

import sys
import random


def partition3(a, l, r):
    pivot = a[l]
    i = l
    lt = l
    gt = r
    
    while i <= gt:
        if a[i] < pivot:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
            
    return lt, gt


def partition2(a, l, r):
    pivot = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= pivot:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    mid1, mid2 = partition3(a, l, r)
    randomized_quick_sort(a, l, mid1 - 1);
    randomized_quick_sort(a, mid2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for pivot in a:
        print(pivot, end=' ')
