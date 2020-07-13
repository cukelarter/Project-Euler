# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 00:01:20 2020

@author: cukel
"""


def collatz(n):
    if n%2==0:
        return collatz(n/2)+1
    elif n==1:
        return 1
    else:
        return collatz(3*n+1)+1

stNum=0;
chLen=0;    
for ii in range(1,1000000):
    chLen0=collatz(ii);
    if chLen0>chLen:
        chLen=chLen0;
        stNum=ii;
