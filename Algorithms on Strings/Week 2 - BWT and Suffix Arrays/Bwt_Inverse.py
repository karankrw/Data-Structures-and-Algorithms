#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:35:28 2020

@author: karanwaghela
"""
import sys

def InverseBWT(bwt):
	A, C, G , T = 1, 1, 1, 1
	lastColunm = []
	for c in bwt:
		if c == '$':
			lastColunm.append(('$', 0))
		elif c == 'A':
			lastColunm.append(('A', A))
			A += 1
		elif c == 'C':
			lastColunm.append(('C', C))
			C += 1
		elif c == 'G':
			lastColunm.append(('G', G))
			G += 1
		else:
			lastColunm.append(('T', T))
			T += 1
	firstColunm = sorted(lastColunm)
	firstToLast = {}
	for i in range(len(firstColunm)):
		firstToLast[firstColunm[i]] = lastColunm[i]
	result = ""
	nextChar = ('$', 0)
	while len(result) < len(firstColunm):
		result += nextChar[0]
		nextChar = firstToLast[nextChar]
	result = result[::-1]
	return result


if __name__ == '__main__':
	bwt = sys.stdin.readline().strip()
	print(InverseBWT(bwt))
"""
import sys

def InverseBWT(bwt):
    A_count, C_count, G_count, T_count = 1, 1, 1, 1
    last_column = ['A'] * len(bwt)
    
    for idx, char in enumerate(bwt):
        if char == '$':
            last_column[idx] = '$'
        elif char == 'A':
            last_column[idx] = 'A' + str(A_count)
            A_count += 1
        elif char == 'C':
            last_column[idx] = 'C' + str(C_count)
            C_count += 1
        elif char == 'G':
            last_column[idx] = 'G' + str(G_count)
            G_count += 1
        else:
            last_column[idx] = 'T' + str(T_count)
            T_count += 1
            
    first_column = sorted(last_column)
    first_to_last_map = dict(zip(first_column, last_column))
    
    result = ['A'] * len(bwt)
    next_char = ('$')
    
    i = 0
    while i < len(first_column):
        result[i] = next_char[0]
        next_char = first_to_last_map[next_char]
        i += 1
        
    return ''.join(result[::-1])


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt)) 
    
"""