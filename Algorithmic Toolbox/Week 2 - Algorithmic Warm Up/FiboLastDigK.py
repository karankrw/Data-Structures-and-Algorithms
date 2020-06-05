#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:14:23 2020

@author: karanwaghela
"""


def fibo(n):
    if n<=1:
       return n
    
    a = 0
    b = 1
    
    for _ in range(n-1):
        c = a + b
        a = b
        b = (c % 10)
        
    return b

n = int(input())
print(fibo(n))