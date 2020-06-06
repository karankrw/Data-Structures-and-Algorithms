#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 02:21:23 2020

@author: karanwaghela
"""

import sys
from collections import namedtuple


Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    
    points = []
    sort_segments = sorted(segments, key = lambda x: x.end)
    
    while sort_segments:
        segment = sort_segments.pop(0)
        point = segment.end
        points.append(point)
        
        for s in sort_segments[:]:
            if s.start <= point <= s.end:
                sort_segments.remove(s)
                
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end = " ")