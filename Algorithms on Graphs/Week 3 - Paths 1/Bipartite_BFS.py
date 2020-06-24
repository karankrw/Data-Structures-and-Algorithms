#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:00:08 2020

@author: karanwaghela
"""

def bipartite(adj):
    color_arr = [-1] * len(adj)
    color_arr[0] = 1
    queue = []
    queue.append(0)
    
    while queue:
        u = queue.pop(0)
        
        for v in adj[u]:
            if color_arr[v] == -1:
                color_arr[v] = 1 - color_arr[u]
                queue.append(v)
            elif color_arr[u] == color_arr[v]:
                return 0
    return 1
                


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        # adjacency list		
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))