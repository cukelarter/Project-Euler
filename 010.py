# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 00:04:00 2020

@author: cukel
"""


from imp_007 import isPrime

N=2000000
total=2
for ii in range(3,N,2):
    if isPrime(ii):
        total+=ii

print(total)