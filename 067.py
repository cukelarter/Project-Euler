# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:49:43 2020

@author: cukel

This is just a copy of 018.py but with a different import
"""


import numpy as np
k = open('txt_067.txt','r');
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
t0=[[59]]


for ii in range(1,len(t)):
    n=t[ii]
    n0=t0[ii-1]+[0]
    n1=[]
    for jj in range(len(n)):
        n1+=(max([int(n[jj])+int(n0[jj])],[int(n[jj])+int(n0[jj-1])]))
    t0.append(n1)

