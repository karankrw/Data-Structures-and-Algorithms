#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:09:26 2020

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


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))