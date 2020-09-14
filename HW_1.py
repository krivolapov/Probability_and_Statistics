# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:02:57 2020

@author: Max
"""
import numpy as np

def seq_sum(n):
    """ input: n, generate a sequence of n random coin flips
        output: return the number of heads 
        Hint: For simplicity, use 1,0 to represent head,tails
    """
    #
    # YOUR CODE HERE
    #
    rand_num = np.random.rand(n)
    rand_num = rand_num + 0.5
    rand_num = list(map(int, rand_num))
    return sum(rand_num)

def estimate_prob(n = 0,k1 = 0,k2 = 0,m = 0):
    x = 0
    counter_prob = 0
    while x < m:
        out = seq_sum(n)
        if out < k2 and out >= k1: counter_prob = counter_prob +1
        x = x+1
    print(counter_prob)
    return float(counter_prob)/m
