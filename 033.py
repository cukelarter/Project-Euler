# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 21:58:49 2020

@author: cukel
"""

# It's messy, don't worry about it
# demon = 100

nontriv=[]
for ii in range(1,10):
    for jj in range(1,10):
        for kk in range(1,10):
            des=ii/jj
            t1=int(str(kk)+str(ii))/int(str(kk)+str(jj))
            if t1==des and t1<1:
                nontriv.append(str(kk)+str(ii)+str(kk)+str(jj))
            t2=int(str(kk)+str(ii))/int(str(jj)+str(kk))
            if t2==des and t2<1:
                nontriv.append(str(kk)+str(ii)+str(jj)+str(kk))
            t3=int(str(ii)+str(kk))/int(str(kk)+str(jj))
            if t3==des and t3<1:
                nontriv.append(str(ii)+str(kk)+str(kk)+str(jj))
            t4=int(str(ii)+str(kk))/int(str(jj)+str(kk))
            if t4==des and t4<1:
                nontriv.append(str(ii)+str(kk)+str(jj)+str(kk))
            
            
numer=16*19*26*49
denom=64*95*65*98