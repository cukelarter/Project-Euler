# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:31:59 2020

@author: cukel
"""


numb = 2**1000;
strN = str(numb);
total=0;
for ii in range(len(strN)):
    total+=int(strN[ii])
print(total)