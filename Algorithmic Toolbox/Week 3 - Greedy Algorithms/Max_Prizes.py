#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:27:06 2020

@author: karanwaghela
"""


import sys


def optimal_summands(n):
    
    summands = []
    
    for i in range(1, n+1):
        n -= i
        
        if n <= i:
            summands.append(n + i)
            break
        
        elif n == 0:
            summands.append(i)
            
        else:
            summands.append(i)
    
    return summands



if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')