#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:42:25 2020

@author: karanwaghela
"""


import sys

def lcs2(a, b):
    m = len(a)
    n = len(b)
    
    c = [[0] * (n + 1) for i in range(m + 1)]
    
        
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
                
    return c[m][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
