# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 14:52:19 2020

@author: cukel
"""


def primeFactors(x):
    x0=x
    ii = 2;
    primes=[];
    while ii<x0:
        if x0%ii==0:
            primes.append(ii)
            x0=x0/ii;
            ii=2;
        else:
            ii+=1;
    primes.append(int(x0))
    return primes

print(primeFactors(600851475143));