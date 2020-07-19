# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 04:00:25 2020

@author: cukel
"""

# solution is found at n=7, current program runs until n=9
# 7652413


import math

def isPan(n,N=9):
    # Modified based on assumption
    # n is str of length N
    for ii in range(1,N+1):
        if str(ii) not in str(n):
            return False
    return True

def isPrime(n):
    if n==1:
        return False
    for ii in range(2,int(math.sqrt(n))+1):
        if n%ii==0:
            return False
    return True

def list2num(n):
    # Convers list of integers to number
    # ex: [1,2,3] -> 123
    st_n=''
    for n0 in n: st_n+=str(n0)
    return int(st_n)

largest=0

for ii in range(10,100000000):
    if isPan(ii,len(str(ii))):
        if isPrime(ii):
            if ii>largest:
                largest=ii