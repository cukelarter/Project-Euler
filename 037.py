# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:25:58 2020

@author: cukel
"""

# 748317

import math


def isPrime(n):
    if n==1:
        # This was a major roadblock, forgot 1 isn't prime
        return False
    for ii in range(2,int(math.sqrt(n)+1)):
        if n%ii==0:
            return False
    return True

def trunPrime(n):
    # returns list of truncated numbers based on n
    # returns both left and right truncated
    st_n=str(n); trun=[n];
    for ii in range(len(st_n)-1):
        trun.append(int(st_n[ii+1:]))
        trun.append(int(st_n[:-ii-1]))
    return trun

tp_list=[];
for ii in range(8,1000000):
    t_prime=True
    for tp in trunPrime(ii):
        if t_prime: #skip if already false
            if not isPrime(tp):
                t_prime=False;
    if t_prime:
        tp_list.append(ii)