# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:40:13 2020

@author: cukel
"""

# Multiplying things and then checking sucks
# Let's try the reverse - it worked!
# 45228

import math

def is9Pan(n):
    # Takes n as string, returns if it is pandigital
    n0=n
    for ii in range(1,10):
        if str(ii) not in n0:
            return False
        else:
            n0=n0.replace(str(ii),'')
    if len(n0)==0:
        return True
    else:
        return False

def isPan(n):
    # Modified based on assumption
    # n is str of length 9
    for ii in range(1,10):
        if str(ii) not in n:
            return False
    return True
        
def divPan(n):
    # Returns if n has some product to make it pan
    # n is integer
    # Uses some neat divisors tricks
    for ii in range(2,int(math.sqrt(n)+1)):
        if n%ii==0:
            n0=str(ii)+str(int(n/ii))+str(n)
            if len(n0)==9:
                if isPan(n0):
                    return True
    return False

pans=[]
total=0
for ii in range(1,99999):
    if divPan(ii):
        total+=ii
        pans.append(ii)