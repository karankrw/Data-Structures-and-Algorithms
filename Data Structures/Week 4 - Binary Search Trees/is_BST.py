#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:11:41 2020

@author: karanwaghela
"""

import sys
import threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def isBinarySearchTree(j, mn, mx):
    if not j in tree:
        return True
    if tree[j][0] < mn or tree[j][0] > mx:
        return False
    return isBinarySearchTree(tree[j][1], mn, tree[j][0]-1) and \
    isBinarySearchTree(tree[j][2], tree[j][0]+1, mx)


def main():
    nodes = int(sys.stdin.readline().strip())
    global tree
    tree, int_max, int_min = {}, 2147483647, -2147483647
    for i in range(nodes):
        tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
    
    if isBinarySearchTree(0, int_min, int_max):
        print("CORRECT")
    else:
        print("INCORRECT")
        
threading.Thread(target = main).start()