# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:37:39 2020

@author: cukel
"""

def propDiv(n):
    # Finds sum of proper divisors of n
    total=0;
    for ii in range(1,int(n/2)+1):
        if n%ii==0:
            total+=ii
    return total

amic=[]
for ii in range(1,10000):
    if propDiv(propDiv(ii))==ii and ii!=propDiv(ii) and ii not in amic:
        amic.append(ii);
        amic.append(propDiv(ii))
        