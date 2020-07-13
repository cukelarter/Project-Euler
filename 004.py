# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:10:24 2020

@author: cukel
"""


def isPal(x):
    X = str(x)
    N=len(X);
    for ii in range(int(N/2)):
        if X[ii] != X[-1-ii]:
            return 0;
    return 1
    
a=999;
a0=900;
largest=0;

while a>a0:
    b=999;
    b0=900;
    while b>b0:
        k=a*b;
        if isPal(k) and k>largest:
            largest=k;
        b-=1
    a-=1

print(largest)
    