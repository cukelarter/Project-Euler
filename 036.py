# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:19:25 2020

@author: cukel
"""

# 872187

def isPal(s):
    return s==s[::-1]

double_pals=[]
for ii in range(1,1000000):
    if isPal(str(ii)) and isPal(bin(ii)[2:]):
        double_pals.append(ii)