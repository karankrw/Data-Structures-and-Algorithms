#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:51:35 2020

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
        curr['$'] = {}
    return trie


def prefix_trie_matching(text, trie, external_index):
    index = 0
    letter = text[index]
    curr = trie[0]
    result = -1
    
    while True:
        if (not curr) or ('$' in curr):
            return result
        if letter in curr:
            curr = trie[curr[letter]]
            result = external_index
            index += 1
            
            if index < len(text):
                letter = text[index]
            elif '$' in curr:
                return result
            else:
                letter = '@'
                result = -1
        else:
            if '$' in curr:
                return result
            else:
                return -1
            
    
def solve(text, n, patterns):
    result = set()
    n = len(text)
    trie = build_trie(patterns)
    
    for i in range(n):
        if (prefix_trie_matching(text[i:], trie, i) != -1):
            result.add(prefix_trie_matching(text[i:], trie, i))
            
    return sorted(list(result))


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
#         text = input().strip()
    n = int(sys.stdin.readline().strip())
#     n = int(input().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]
#         patterns+= [ input().strip()]

    ans = solve(text, n, patterns)
#     print(' '.join(map(str,ans))+'\n')
    sys.stdout.write(' '.join(map(str, ans)) + '\n')