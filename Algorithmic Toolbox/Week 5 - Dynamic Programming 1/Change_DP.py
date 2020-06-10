#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:26:07 2020

@author: karanwaghela
"""

import sys


def dynamicCoinChange( T, L ):

      Opt = [0 for i in range(0, L+1)]
      sets = {i:[] for i in range(L+1)}
      n = len(T)
      for i in range(1, L+1):
            smallest = float("inf")
            for j in range(0, n):
                 if (T[j] <= i):
                       smallest = min(smallest, Opt[i - T[j]]) 
                       if smallest == Opt[i - T[j]]:
                             sets[i] = [T[j]] + sets[i-T[j]]
            Opt[i] = 1 + smallest 
      return Opt[L]
  

T = [1, 3, 4]
L = int(sys.stdin.read())
print(dynamicCoinChange( T, L ))