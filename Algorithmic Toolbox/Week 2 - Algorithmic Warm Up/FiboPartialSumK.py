#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:47:46 2020

@author: karanwaghela
"""
 
        
def get_fibo(n):
    
    
    if n<=1:
       return n
    
    a = 0
    b = 1
    
    for _ in range(n-1):
        a, b = b, (a+b)
        
    return b
        
        
        
def pisano_len(m):
    a = 0
    b = 1
    for i in range(m * m + 1):
        a, b = b, (a + b) % m
        
        if (a == 0 and b == 1):
            return i + 1
 
    
def fibo(n,m):
    remainder = n % pisano_len(m)
    return get_fibo(remainder) % m
       

def last_dig(n):
    if n<=1:
       return n
    
    a = 0
    b = 1
    
    for _ in range(n-1):
        a, b = b % 10, (a+b) % 10
        
    return b
        

def fibo_partial_sum(m, n):
    if m == n:
        return last_dig(m % 60)
    else:
        m %= 60
        n %= 60
        
        m_ld = fibo(m + 1, 10) - 1
        n_ld = fibo(n + 2, 10) - 1
        
    return (n_ld - m_ld) % 10


n, m = map(int, input().split())
print(fibo_partial_sum(n,m))