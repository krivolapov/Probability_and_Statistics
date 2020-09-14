# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:14:09 2020

@author: Max
"""

def union(A, B):
    return (A|B, len(A|B))

A = {1, 2, 3}
B = {3, -6, 2, 0}
print (union(A, B))

def inclusion_exclusion(A, B):
    size_A = len(A)
    size_B = len(B)
    size_A_and_B = len(A&B)
    size_A_uni_B = size_A + size_B - size_A_and_B
    return (size_A, size_B, size_A_and_B, size_A_uni_B)


def union3(A, B, C):
    size_A = len(A)
    size_B = len(B)
    size_C = len(C)
    size_AB = len(A&B)
    size_AC = len(A&C)
    size_CB = len(C&B)
    size_ABC = len(A&B&C)
    return (A|B|C, (size_A + size_B + size_C -size_AB - size_AC - size_CB + size_ABC))