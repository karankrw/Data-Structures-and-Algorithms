#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:00:21 2020

@author: karanwaghela
"""

def fibo(n):
    if n<=1:
       return n
    
    a = 0
    b = 1
    
    for _ in range(n-1):
        a, b = b, a + b
       # a = b
        #b = a + b
    return b

n = int(input())
print(fibo(n))