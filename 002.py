# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 14:04:44 2020

@author: cukel
"""

def fib(N):
    a=1;
    b=1;
    total=0;
    while b<N and a+b<N:
        b0=a+b;
        if b0%2==0:
            total+=b0;
        a=b;
        b=b0;
    return total;
        
print(fib(4E6));