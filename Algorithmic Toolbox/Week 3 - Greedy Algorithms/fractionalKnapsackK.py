#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:06:19 2020

@author: karanwaghela
"""
import sys

def get_maximal_value(capacity, values, weights):
 
    max_value = 0
    fractions = [0]*len(values)
   
    for i in range(len(values)):
        fractions[i] = [values[i], weights[i], values[i] / weights[i]]
    
    fractions.sort(reverse = True, key = lambda x: x[:][2])
    
    for i in range(len(fractions)):
        add_capacity = min(fractions[i][1], capacity)
        max_value += fractions[i][2] * add_capacity
        capacity -= add_capacity
        
        if capacity == 0:
            return max_value
 
    return max_value


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    max_value = get_maximal_value(capacity, values, weights)
    print("{:.10f}".format(max_value))