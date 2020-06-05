#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:25:09 2020

@author: karanwaghela
"""

def pisano_len(m):
    a = 0
    b = 1
    for i in range(m * m + 1):
        a, b = b, (a + b) % m
        
        if (a == 0 and b == 1):
            return i + 1
        


def get_fibo(n):
    
    
    if n<=1:
       return n
    
    a = 0
    b = 1
    
    for _ in range(n-1):
        a, b = b, (a+b)
        
    return b


def fibo(n,m):
    remainder = n % pisano_len(m)
    return get_fibo(remainder) % m


n, m = map(int, input().split())
print(fibo(n,m))