#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:43:17 2020

@author: karanwaghela
"""
import queue
            
    
def distance(adj, cost, s, t):
    dist = [float('inf')] * len(adj)
    dist[s] = 0
    pq = queue.PriorityQueue()
    pq.put(s)
    
    while not pq.empty():
        u_index = pq.get()
        
        for v in adj[u_index]:
            v_index = adj[u_index].index(v)
            
            if dist[v] > dist[u_index] + cost[u_index][v_index]:
                dist[v] = dist[u_index] + cost[u_index][v_index]
                pq.put(v)
                
    if dist[t] == float('inf'):
        return -1
    return dist[t]
    


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = map(int, input().split())
    s, t = s-1, t-1
    print(distance(adj, cost, s, t))