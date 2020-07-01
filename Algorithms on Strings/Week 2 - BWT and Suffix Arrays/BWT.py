#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:35:40 2020

@author: karanwaghela
"""

import sys

def BWT(text):
    l = len(text)
    circular = []
    
    for i in range(l):
        circular.append(text[i:] + text[:i])
        
    circular.sort()
    result = ""
    
    for row in circular:
        result += row[-1]
        
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))