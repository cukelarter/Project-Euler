# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:19:42 2020

@author: cukel
"""

# You got this right first but fucked up adding 30.5
# All roots in this series have imaginary val of
# 6.383572667401852 j

import math

def isPrime(n):
    if n%2==0:
        return False
    for ii in range(3,int(math.sqrt(abs(n)))+1,2):
        if n%ii==0:
            return False
    return True

def quadratic(n,a,b):
    return (n**2)+(a*n)+b


greatest=0
g_a=0; g_b=0;


for aa in range(-80,80):
    for bb in range(-1002,1002):
        nn=0
        while nn<100:
            if isPrime(quadratic(nn,aa,bb)):
                nn+=1
            else:
                break
        if nn>greatest:
            greatest=nn
            g_a=aa
            g_b=bb

print(greatest)
print(g_a,g_b)