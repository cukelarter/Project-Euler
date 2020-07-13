# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:38:18 2020

@author: cukel
"""


def fib(n):
    # Returns first fobancci number to contain n digits:
    index=3; fi=2; f0=1;
    while index<10000:   
        if len(str(fi))>=n:
            return index
        else:
            index+=1;
            fn=fi+f0;
            f0=fi;
            fi=fn;
            