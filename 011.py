# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 09:48:21 2020

@author: cukel
"""


import numpy as np
m = np.loadtxt('txt_011.txt')

def maxProd(dataSet,n):
    # Returns maximum product of n numbers in dataSet
    total=0;
    if len(dataSet)<n:
        return 0
    for ii in range(len(dataSet)-n+1):
        total0=1;
        for jj in range(n):
            total0*=dataSet[ii+jj]
        if total0>total:
            total=total0;
    return total

def minProd_jessie(dataSet,n):
    total=0;
    if len(dataSet)>n:
        return 0
    for ii in range (len(dataSet)-n+1):
        total0=1;
        for kk in range(n):
            total0*=dataSet[ii+kk]
            if total0<total:
                total=total0
    return total

def prepper(raw,n):
    # Returns set of arrays to be tested 
    greatest=0;
    for ii in range(len(raw[0,:])):
        # Assume matrix with n=m
        g0 = maxProd(raw[:,ii],n);
        g1 = maxProd(raw[ii,:],n);
        g2 = maxProd(np.diag(raw,ii),n);
        g3 = maxProd(np.diag(raw,-ii),n);
        g4 = maxProd(np.diag(np.fliplr(m),ii),n);
        g5 = maxProd(np.diag(np.fliplr(m),-ii),n);
        print([g0,g1,g2,g3,g4,g5])
        greatest = max([greatest,g0,g1,g2,g3,g4,g5]);
    return greatest
        
                
# 70600674