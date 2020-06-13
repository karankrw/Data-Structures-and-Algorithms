#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:53:57 2020

@author: karanwaghela
"""

import sys


def optimal_weight(W, w):
    w = [0] + w
    items = len(w)
    capacity = W + 1
    
    #Creating Matrix for DP
    value = [[0] * (items + 1) for _ in range(capacity)]
    
    for j in range(1, items + 1):
        for i in range(1, capacity):
            value[i][j] = value[i][j-1]
            if w[j-1] <= i:
                val = value[i - w[j-1]][j-1] + w[j-1]
                if value[i][j] <= val:
                    value[i][j] = val
            
                
    return value[W][len(w)]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
    
