# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:59:17 2020

@author: cukel
"""


def factDivis(x,N):
    toTest=list(range(1,N+1));
    n=N;
    while n>1 and toTest!=[]:
        if x%n!=0:
            return 0
        else:
            ii=len(toTest)-1
            while ii>=0 and toTest!=[]:
                if n%toTest[ii]==0:
                    toTest.remove(toTest[ii])
                ii-=1
            n-=1        
    return 1

ii=1
N=20
while ii<999999999999:
    if factDivis(ii,N):
        print(ii)
        break
    ii+=1
    
# 232792560