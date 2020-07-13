# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:59:50 2020

@author: cukel
"""
from itertools import combinations as cm

def recFill(t,n):
    # Returns number of combos
    # Recursively fills to t using vals of array n
    # Array in descending order
    # ex [10,5,2,1]
    if t==0:
        return 1
    elif t<0:
        return 0
    tot_branch=0 # Total of this branch of searching
    for n0 in n:
        tot_branch+=recFill(t-n0, n[n.index(n0):])
    return tot_branch


# Old Code, doesn't work
"""
def sort2(n):
    n0=[]
    for ii in n:
        n0.append(sorted(ii))
    return n0

coins=[1,2,5,10,20,50,100,200];

def longFunc(n):
    # Takes too fucking long
    counter=1;
    group=[];
    for ii in range(1,n):
        comb = list(cm(coins,ii))  
        for jj in comb:
            g0=sort2(group)
            if sum(jj)==200 :
                if sorted(jj) not in g0:
                    group.append(sorted(jj))
    return group 
"""