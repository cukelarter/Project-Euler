# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:48:53 2020

@author: cukel
"""
import math
def isPrime(n):
    if n%2==0:
        return 0
    for ii in range(3,int(math.sqrt(n)+1),2):
        if n%ii==0:
            return 0
    return 1

def probWrapper():
    index=2
    ii=5
    N=10001
    while index<N:
        if isPrime(ii):
            index+=1
            if index==N:
                break
            ii+=2
    return(ii)