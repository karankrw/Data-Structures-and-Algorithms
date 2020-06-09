#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:44:42 2020

@author: karanwaghela
"""


def get_majority_element(a, left, right):
    if left == right:
        return -1
    
    dic = {}
    for i in set(a):
        dic[i] = 0
        
    for i in a:
        dic[i] += 1
        
    for i in list(dic.values()):
        if i > right/2:
            return 1
    return -1
    

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
