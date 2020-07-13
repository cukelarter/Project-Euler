 # -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:24:08 2020

@author: cukel
"""
# Uses Pascal triangle to generate number of paths

import numpy as np
def genTri(n):
    # Generates Pascal triangle of nxn dimension
    tri = np.zeros((n,n));
    tri[:,0]=1;
    tri[0,:]=1;
    return tri
    
    
def recGen(arr,ii,jj):
    # Recursively generates based on grid index
   a=arr[(ii-1,jj)];
   b=arr[(ii,jj-1)];
   if a==0:
       a=recGen(arr,ii-1,jj);
   if b==0:
       b=recGen(arr,ii,jj-1);
   return a+b
       
def linGen(arr,n):
    # Generates pascal triangle linearly, returns grid
    for ii in range(1,n):
        for jj in range(1,n):
            if arr[(ii,jj)]==0:
                arr[(ii,jj)]=arr[(ii-1,jj)]+arr[(ii,jj-1)];
    return arr
N=21
tri=genTri(N)
print(linGen(tri,N)[(N-1,N-1)])