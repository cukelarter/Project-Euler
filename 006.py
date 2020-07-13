# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 17:37:41 2020

@author: cukel
"""


def sumSq(N):
    total=0;
    for ii in range(1,N+1):
        total+=ii**2
    return total

def sqSum(N):
    total=0;
    for ii in range(1,N+1):
            total+=ii
    return total**2