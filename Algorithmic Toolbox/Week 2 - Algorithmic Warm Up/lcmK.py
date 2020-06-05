#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:21:18 2020

@author: karanwaghela
"""


def gcd(a, b):
    dividend = a if (a >= b) else b
    divisor = a if (a <= b) else b

    while divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return dividend


def lcm(a, b):
    return (a * b) // gcd(a,b)


a, b = map(int, input().split())
print(lcm(a, b))