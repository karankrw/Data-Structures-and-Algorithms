#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:20:07 2020

@author: karanwaghela
"""
import sys
import numpy

def lcs3(a, b, c):
    m = len(a)
    n = len(b)
    p = len(c)
    
    l = numpy.zeros((m+1, n+1, p+1))
    
    for i in range(m+1):
        for j in range(n+1):
            for k in range(p+1):
                
                if i == 0 or j == 0 or k == 0:
                    l[i][j][k] = 0
                
                elif a[i - 1] == b[j - 1] and a[i - 1] == c[k - 1]:
                    l[i][j][k] = (l[i - 1][j - 1][k - 1]) + 1
                    
                else:
                    l[i][j][k]= max(l[i-1][j][k], l[i][j-1][k], l[i][j][k-1]) 
                                    #,l[i-1][j-1][k], l[i-1][j][k-1], l[i][j-1][k-1])
                
    return int(l[m][n][p])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
