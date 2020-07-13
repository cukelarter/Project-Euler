# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:49:59 2020

@author: cukel
"""


def digPow(n,a):
    n0 = str(n)
    total=0;
    for ii in range(len(n0)):
        total+=int(n0[ii])**a
    if total==n:
        return True
    else:
        return False

col=[];
for ii in range(2,10000000):
    if digPow(ii,5):
        col.append(ii)