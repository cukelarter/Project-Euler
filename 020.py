# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:33:57 2020

@author: cukel
"""


def recFact(n):
    # Returns factorial of n, recursively
    if n==1:
        return 1
    else:
        return n*recFact(n-1)

hun=str(recFact(100))
total=0;
for ii in range(len(hun)):
    total+=int(hun[ii]);