# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:34:37 2020

@author: Max
"""
import itertools
from itertools import product


def complement_of_union(A, B, U):
    AB = A.union(B)
    U_minus_AB = U.difference(AB)
    return (AB, U_minus_AB)

A = {1, 2, 3}
B = {3, -6, 2, 0}
U = {-10, -9, -8, -7, -6, 0, 1, 2, 3, 4}
print(complement_of_union(A, B, U))

def intersection_of_complements(A, B, U):
    return (U-A, (U-A).intersection(U-B))

A = {1, 2, 3, 4, 5}
B = {0, 2, -6, 5, 8, 9}
U = A|B|{-3, 7, 10, -4}
print(intersection_of_complements(A, B, U))

def product_of_unions(A, B, S, T):
    product_out = set()
    AB = A.union(B)
    ST = S.union(T)
    for i in product(AB, ST):
        product_out.add((i))
    return(AB, product_out)

A = {1, 2}
B = {1, 3}
S = {-1, 0}
T = {0, 10}
print(product_of_unions(A, B, S, T))

def union_of_products(A, B, S, T):
    AxS = set()
    AxT = set()
    BxS = set()
    BxT = set()
    for i in product(A, S):
        AxS.add((i))
    for i in product(A, T):
        AxT.add((i))
    for i in product(B, S):
        BxS.add((i))
    for i in product(B, T):
        BxT.add((i))
    return (AxS, AxS|AxT|BxS|BxT)

A = {1, 2}
B = {1, 3}
S = {-1, 0}
T = {0, 10}
print(union_of_products(A, B, S, T))
