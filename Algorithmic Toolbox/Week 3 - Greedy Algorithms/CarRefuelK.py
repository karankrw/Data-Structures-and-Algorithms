#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 02:55:56 2020

@author: karanwaghela
"""



def compute_min_refills(distance, tank, stops, n):
    numRefills = 0
    currentPos = 0
    
    stops.insert(0, 0)
    stops.append(distance)
    
    while(currentPos <= n):
        lastPos = currentPos
        
        while(currentPos <= n and ((stops[currentPos + 1] - stops[lastPos]) <= m)):
            currentPos += 1
            
        if(currentPos == lastPos):
            return -1
        
        if(currentPos <= n):
            numRefills += 1
        
    return numRefills


if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    print(compute_min_refills(d, m, stops, n))
