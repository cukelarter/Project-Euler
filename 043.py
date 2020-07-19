# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 13:49:23 2020

@author: cukel
"""

# 16695334890

from itertools import permutations as pm
import math

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

def ssDiv(n):
    # returns if n has sub string divisibility
    # Assumes 0 to 9 pandigital
    n_str=str(n)
    if len(n_str)<10:
        # catches pandigital numbers with leading 0
        n_str='0'+n_str
    for ii in range(len(primes)):
        if int(n_str[ii+1]+n_str[ii+2]+n_str[ii+3])%primes[ii]==0:
            continue
        else:
            return False
    return True
    
# Generate list of primes between 2 and 17, inclu
primes=[];
for ii in range(2,18):
    if isPrime(ii):
        primes.append(ii)
        
# Generate list of 0 to 9 pandigitals using itertools.permutations
total=0
pans=list(pm(list(range(0,10))))
# pans is huge, computational simplicity of functions
# allows problem to be solved in reasonable amount of time

for pan in pans:
    n=list2num(pan)
    if ssDiv(str(n)):
        total+=n

            