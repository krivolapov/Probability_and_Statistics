# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 14:46:00 2020

@author: Max
"""

test_1 = [0.1, 0.2, 0.1, 0.3, 0.1, 0.2]
test_2 = [0.99, 0.01]

def median_cal(data):
    x = 0
    temp = []
    while x < len(data):
        if (sum(data[:(x+1)]) >= 0.5 and sum(data[x:]) >= 0.5):
               temp.append(x+1)
        x += 1
    return (sum(temp))/(len(temp))