# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:49:41 2020

@author: cukel
"""


def longDiv(n,a):
    # Long divides n by a
    c=0; #Counter
    n0=n;
    rList=[]
    while n0>0 and n0 not in rList:
        if n0<a:
            n0*=10;
            c+=1
            continue
        else:
            rList.append(n0);
            n1=n0%a
            n0=n1;
            
    return rList

g=0
index=0;
for ii in range(1,1000):
    
    g0=len(longDiv(1.0,ii));
    if g0>g:
        g=g0
        index=ii
    print(ii,g,g0,index)
    
# Uses a guessing method, can run into problems
# when the repeating decimal starts later