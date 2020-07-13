# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 23:42:48 2020

@author: cukel
"""

import math
def genTri(n):
    # Generates the nth triangle number
    total=0;
    for ii in range(1,n+1):
        total+=ii;
    return total

def divisors(n):
    # Returns the divisors of n, integer
    counter=0;
    for ii in range(1,int(math.sqrt(n))+1):
        if n%ii==0:
            counter+=2;
    return counter

ii = 0;
while ii<1000000:
    if divisors(genTri(ii))>500:
        print(genTri(ii))
        break
    ii+=1