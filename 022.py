# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:54:04 2020

@author: cukel
"""

k = open('txt_022.txt','r');
l = k.read();
m = l.split(',')

def alph(a,b):
    # Returns whether a is alphabetically before b
    for ii in range(min([len(a),len(b)])):
        a0=ord(a[ii]); b0=ord(points[ii]);
        if a0==34 or b0==34:
            continue
        if a0<b0:
            return True
        elif a0>b0:
            return False
    # Only gets here if words are the same to the ends
    # Ex: 'car' and 'cart'
    if len(a)<len(b):
        return True
    else:
        return False
    
def points(a):
    total=0;
    for ii in range(len(a)):
        a0=ord(a[ii]);
        if a0==34:
            continue
        total+=ord(a[ii])-64;
    return total

m0=sorted(m);
total=0;
for ii in range(1,len(m0)+1):
    total+=points(m0[ii-1])*ii