#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:59:33 2020

@author: karanwaghela
"""
def MaxPairProduct(n,a,c):
    for i in range(0,n):
        for j in range(1,n):
            if a[i] != a[j]:
                m= a[i]*a[j]
                c.append(m)
                
            else:
                continue
            
    Product1 = max(c)
    return Product1

def MaxPairwiseProductFast(n,a):
    max_index1 = -1
    for i in range(0,n):
        if a[i] > a[max_index1] or max_index1 == -1:
            max_index1 = i


    max_index2 = -1
    for j in range(0,n):
        if (max_index2 == -1 or a[j] > a[max_index2]) and j != max_index1:
            max_index2 = j   

    Product2 = a[max_index1] * a[max_index2]
    return Product2


n = int(input())
a = [int(x) for x in input().split()]
assert (len(a)==n)
c = list()

#print(MaxPairProduct(n,a,c))
print(MaxPairwiseProductFast(n,a))  