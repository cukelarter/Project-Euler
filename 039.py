# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 20:05:26 2020

@author: cukel
"""

# 840
# Brute forces solution
    
def abFinder(c):
    # Tries to find a+b from c
    # As in, the pythagorean theorem
    # Doesn't generate duplicates
    ret=[];
    for ii in range(1,c):
        for jj in range(c,ii,-1):
            if ii**2 + jj**2==c**2:
                ret.append([ii,jj])
    return(ret)

freq_dict = {}

for ii in range(5,600):
    for ab in abFinder(ii):
        freq_dict[sum(ab,ii)]=freq_dict.get(sum(ab,ii),0)+1

"""        
def finder(n,a_r=3/12,b_r=4/12,c_r=5/12):
    # Unitilized
    # Returns triange sides given n
    # Uses 3:4:5 ratio unless otherwise specified
    a=n*(a_r);b=n*(b_r);c=n*(c_r);
    if a**2+b**2==c**2:
        return([a,b,c])
    else:
        return False
"""