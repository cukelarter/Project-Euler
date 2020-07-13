# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:21:31 2020

@author: cukel
"""


[1,3,5,7,9,13,17,21,25]

n=[]
ii=1
i0=2
c=0
d=0
while d<=(1001-3)/2:
    if c>=4:
        c=0;
        i0+=2;
        d+=1
    n.append(ii)
    ii+=i0;
    c+=1
    
# d 4 11
# d 3 9
# d 2 7
# d 1 5
