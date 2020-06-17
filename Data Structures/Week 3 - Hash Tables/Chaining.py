#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 23:28:29 2020

@author: karanwaghela
"""

class Chaining:
    
    _multiplier = 263
    _prime = 1000000007
    
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]
        
        
    def hash_function(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count
    
    
    def add(self, string):
        hashed = self.hash_function(string)
        bucket = self.buckets[hashed]
        if string not in bucket:
            self.buckets[hashed] = [string] + bucket
            
            
    def delete(self, string):
        hashed = self.hash_function(string)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i] == string:
                bucket.pop(i)
                break
            
            
    def find(self, string):
        hashed = self.hash_function(string)
        if string in self.buckets[hashed]:
            return "yes"
        return "no"
    
    
    def check(self, i):
        return self.buckets[i]
    
    
def process_queries(queries):
    for query in queries:
        cmd, arg = query.split()
        if cmd == "add":
            qp.add(arg)
            
        elif cmd == "del":
            qp.delete(arg)
            
        elif cmd == "find":
            print(qp.find(arg))
            
        elif cmd == "check":
            arg = int(arg)
            print(" ".join(qp.check(arg)))
            
            

if __name__ == "__main__":
    bucket_count = int(input())
    n = int(input())
    
    qp = Chaining(bucket_count)
    queries = [input() for i in range(n)]
    process_queries(queries)
    
    
    
    