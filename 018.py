# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:49:43 2020

@author: cukel
"""


import numpy as np
k = open('txt_018.txt','r');
l = k.read();
m = l.split('\n')
steps=[];
for ii in range(len(m)):
    s = m[ii].split()
    steps.append(s)
# Adds 0 to buffer

#t = [[3],[7,4],[2,4,6],[8,5,9,3]]
#t0=[[3]]
    
t=steps
t0=[[75]]


for ii in range(1,len(t)):
    n=t[ii]
    n0=t0[ii-1]+[0]
    n1=[]
    for jj in range(len(n)):
        n1+=(max([int(n[jj])+int(n0[jj])],[int(n[jj])+int(n0[jj-1])]))
    t0.append(n1)

"""
def recPath(s,ii,n):
    # Recursively helps generate path
    print(s,ii,n)
    print(s[ii][n])
    print(n, ii)
    while n>=0 and ii>=0:
        try:
            #print(s[n-1][ii-1])
            if s[n-1][ii-1]>s[n-1][ii]:
                print('a')
                return s[n][ii]+recPath(s,ii-1,n-ii)
            else:
                print('b')
                return s[n][ii]+recPath(s,ii,n-ii)
        except:
            try:
                print('c')
                return s[n][ii]+recPath(s,ii-1,n-ii)
            except:
                try:
                    print('d')
                    return s[n][ii]+recPath(s,ii,n-ii)
                except:
                    print('e')
                    return s[n][ii]
def pather(s):
    # Paths by starting at end of triangle and going up
    for ii in range(len(s)-1,-1,-1):
        recPath(s,ii,0)

"""
