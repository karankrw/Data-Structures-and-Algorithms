#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 02:03:31 2020

@author: karanwaghela
"""

import sys

def dfs(adj, visited, order, x):
    #write your code here
    visited[x] = 1
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:
            dfs(adj, visited, order, adj[x][i])
    order.append(x)


def toposort(adj):
    visited = [0] * len(adj)
    order = []
    #write your code here
    for i in range(len(adj)):
        if not visited[i]:
            dfs(adj, visited, order, i)
    order.reverse()
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
