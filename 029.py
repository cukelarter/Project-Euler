# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:36:48 2020

@author: cukel
"""

terms=[];
for ii in range(2,101):
    for jj in range(2,101):
        n=ii**jj
        if n not in terms:
            terms.append(n)