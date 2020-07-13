# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:59:50 2020

@author: cukel
"""


total=0;
for i in range(1000):
    if i%3==0 or i%5==0:
        total+=i;
print(total)