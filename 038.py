# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 19:32:07 2020

@author: cukel
"""

# 9327 * (1,2) = 932718654

def isPan(n):
    # Modified based on assumption
    # n is str of length 9
    for ii in range(1,10):
        if str(ii) not in n:
            return False
    return True

greatest=0;
for ii in range(1,10000):
    nPan=''; jj=1;
    while len(nPan)<9:
        nPan+=str(jj*ii)
        jj+=1
    if isPan(nPan) and len(nPan)==9 and int(nPan)>greatest:
        greatest=int(nPan)
        print(ii)