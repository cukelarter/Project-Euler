# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 03:48:19 2020

@author: cukel
"""

ii=1
fract='0.'
digits=[1]
while len(fract)<1000002:
    # Generates fract, really large string
    # Calling fract in console will crash the file lol
    fract+=str(ii)
    ii+=1

os=1 # Offset
ans=1
for jj in range(7):
    ans*=int(fract[10**jj+os])
