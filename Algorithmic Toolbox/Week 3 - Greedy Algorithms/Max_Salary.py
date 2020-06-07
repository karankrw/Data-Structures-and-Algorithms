#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:58:20 2020

@author: karanwaghela
"""

import sys
from itertools import permutations

def largest_number(a):
    
    res = int(max((''.join(i) for i in permutations(str(i)  
                     for i in a)), key = int)) 
    
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(str(largest_number(a)))
