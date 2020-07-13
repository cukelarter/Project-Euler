# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:19:31 2020

@author: cukel
"""

# 40730

facts=[1]

def fact(n):
    total=1
    for ii in range(1,n+1):
        total*=ii
    return total

# add them all to list for simplcity
    
for ii in range(1,10):
    facts.append(fact(ii))
    
t=[]

def numDig(n):
    # returns the digits in n as a string
    n0=str(n);digs=[];
    for dig in n0:
        digs.append(int(dig))
    return digs

for ii in range(3,999999):
    tot=0
    for dig in numDig(ii):
        tot+=facts[dig]
    if tot==ii:
        t.append(ii)