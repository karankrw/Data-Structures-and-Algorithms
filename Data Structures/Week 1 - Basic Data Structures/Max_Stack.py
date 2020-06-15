#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 00:07:24 2020

@author: karanwaghela
"""
import sys


class StackMax:
    
    def __init__(self):
        self.__stack = []
        self.__maxstack = []
        
    
    def push(self, a):
        self.__stack.append(a)
        if len(self.__maxstack) == 0:
            self.__maxstack.append(a)
        else:
            if self.__maxstack[-1] <= a:
                self.__maxstack.append(a)
                
                
    def pop(self):
        assert(len(self.__stack))
        a = self.__stack.pop()
        if a == self.__maxstack[-1]:
            self.__maxstack.pop()
            
            
    def max(self):
        assert(len(self.__stack))
        return self.__maxstack[-1]
    
    
    
if __name__ == '__main__':
    
    stack = StackMax()
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert(0)