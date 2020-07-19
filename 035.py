# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:11:42 2020

@author: cukel
"""

# 55

import math
from itertools import combinations_with_replacement as cm
import itertools


def isPrime(n):
    for ii in range(2,int(math.sqrt(n)+1)):
        if n%ii==0:
            return False
    return True

def list2num(n):
    # Convers list of integers to number
    # ex: [1,2,3] -> 123
    st_n=''
    for n0 in n: st_n+=str(n0)
    return int(st_n)

def num2list(n):
    # Convert number to list of integers
    # ex: 123 -> [1,2,3]
    st_n=str(n); n_list=[]
    for n0 in st_n: n_list.append(int(n0))
    return n_list

def getRotations(n):
    # Gets all rotations of list n
    # Ex: [1,9,7] returns 197, 971, 719
    # Uses list because thats how cm outputs 
    if all(elem == n[0] for elem in n):
        # Checks if all elements are the same
        return [n]
    rotations=[]; n0=n; flag=True;
    # Flag used to bypass first try
    while n0!=n or flag:
        flag=False;
        # Helper h for 1 level nest comprehension
        h = [[n0[-1]],n0[:-1]]
        n0 = [j for i in h for j in i]
        rotations.append(n0)
    return rotations

def isCircular(n):
    # Returns if n is a circular prime using helpers
    if not isPrime(n):
        return False
    for rot in getRotations(num2list(n)):
        if not isPrime(list2num(rot)):
                return False
    return True
                
circs=[];
for ii in range(2,1000000):
    if isCircular(ii):
        circs.append(ii)