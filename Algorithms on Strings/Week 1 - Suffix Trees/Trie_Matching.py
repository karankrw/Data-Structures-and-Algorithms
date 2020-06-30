#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 01:12:30 2020

@author: karanwaghela
"""

import sys

def build_trie(patterns):
    trie = {}
    trie[0] = {}
    index = 1
    
    for pattern in patterns:
        curr = trie[0]
        for letter in pattern:
            if letter in curr.keys():
                curr = trie[curr[letter]]
            else:
                curr[letter] = index
                trie[index] = {}
                curr = trie[index]
                index = index + 1
    return trie


def prefix_trie_matching(text, trie):
    index = 0
    letter = text[index]
    curr = trie[0]
    
    while True:
        if not curr:
            return True
        elif letter in curr.keys():
            curr = trie[curr[letter]]
            index = index + 1
            if index < len(text):
                letter = text[index]
            else:
                letter = '$'
        else:
            return False
        

def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)
    
    n = len(text)
    for i in range(n):
        if prefix_trie_matching(text[i:], trie):
            result.append(i)
            
    return result
    


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
#     text = input().strip()
    n = int(sys.stdin.readline().strip())
#     n = int(input().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]
#         patterns+= [ input().strip()]

    ans = solve(text, n, patterns)
#     print(' '.join(map(str,ans))+'\n')
    sys.stdout.write(' '.join(map(str, ans)) + '\n')