# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 14:46:00 2020

@author: Max
"""
import random
from statistics import median


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


def sample_median(n,P):
    rms = random.choices(range(1, len(P) + 1), weights = P, k = n)
    return median(rms)

def expected_cal(P):
    out = 0
    for i in range(len(P)):
        out += P[i] * (i+1)
    return out

def average_sample_median(n,P):
    M = 1000
    sum_median = 0
    for i in range(M):
        sum_median += sample_median(n, P)
    return sum_median / M
