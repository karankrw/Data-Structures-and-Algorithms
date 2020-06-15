#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:38:01 2020

@author: karanwaghela
"""


import sys
import threading

sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)


class TreeHeight:
        
    
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.nodes = {}
        
        for i in range(self.n):
            self.nodes[i] = []
            
        for i in range(self.n):
            if self.parent[i] == -1:
                pass
            else:
                self.nodes[self.parent[i]] += [i]
        
    
    def tree_height(self):
        root = None
        try:
            root = self.parent.index(-1)
        except ValueError:
            return 0
        
        queue = []
        queue.append(root)
        height = 0
        while True:
            node_count = len(queue)
            if node_count == 0:
                return height
            height += 1
            while node_count > 0:
                node = queue[0]
                queue.pop(0)
                if self.nodes[node]:
                    for v in self.nodes[node]:
                        queue.append(v)
                        
                node_count -= 1
    


tree = TreeHeight()
tree.read()
print(tree.tree_height())
    
    
