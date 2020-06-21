#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 01:28:30 2020

@author: karanwaghela
"""

import sys


def acyclic(adj):
    visited = [0 for _ in range(len(adj))]
    rec_stack = [0 for _ in range(len(adj))]
    
    for i in range(len(adj)):
        if not visited[i]:
            if dfs(adj, i, visited, rec_stack):
                return 1
    return 0


def dfs(adj, x, visited, rec_stack):
    visited[x] = 1
    rec_stack[x] = 1
    
    for i in range(len(adj[x])):
        if not visited[adj[x][i]] and dfs(adj, adj[x][i], visited, rec_stack):
            return 1
        elif rec_stack[adj[x][i]]:
            return 1
        
    rec_stack[x] = 0
    return 0
    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
