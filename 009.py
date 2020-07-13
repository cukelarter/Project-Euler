# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:51:24 2020

@author: cukel
"""


def isPythagTrip(a,b,c):
    if (a**2 + b**2 ==c**2):
        return 1
    return 0

def pTrip(N):
    a=1;
    b=1;
    c=1;
    while a<N:
        b=1
        while b<N:
            c=1
            while c<N:
                if a+b+c==N and isPythagTrip(a,b,c):
                    return a*b*c
                c+=1
            b+=1
        a+=1
