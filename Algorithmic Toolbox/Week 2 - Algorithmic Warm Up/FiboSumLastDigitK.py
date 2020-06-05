#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 02:25:06 2020

@author: karanwaghela
"""


def fibo_sum_last_d(n):
    n = (n+2) % 60
    
    a = 0
    b = 1
    
    for _ in range(n - 1):
        a, b = b % 10, (a+b) % 10
        
    if (b == 0):
        return 9
    
    return (b % 10 - 1)


n = int(input())
print(fibo_sum_last_d(n))