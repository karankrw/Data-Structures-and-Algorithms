#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 02:50:36 2020

@author: karanwaghela
"""


def fibo_sum_last_d(n):
    if n<=1:
       return n
    
    
    a = 0
    b = 1
    
    for _ in range(n - 1):
        a, b = b, (a+b) % 10
        
    #if (b == 0):
      #  return 9
    
    return (b % 10)


def fibo_sum_squares(n):
    v = fibo_sum_last_d(n % 60) 
    h = fibo_sum_last_d((n + 1) % 60)
    
    sumSquares = h * v
    return sumSquares % 10


n = int(input())
print(fibo_sum_squares(n))