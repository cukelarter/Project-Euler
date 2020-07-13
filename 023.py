# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:56:31 2020

@author: cukel
"""

# Fuck this, takes fucking forever but it worked
# 4179871

def divs(n):
    divs=[];
    for ii in range(1,int(n/2)+1):
        if n%ii==0 and ii not in divs:
            divs.append(ii);
    return divs

def isAbundant(n):
    if sum(divs(n))>n:
        return True
    else:
        return False 

aNums=[]
for ii in range(12,28123):
    if isAbundant(ii):
        aNums.append(ii)

print('Done getting abundants')

aNums0=[]
for jj in range(len(aNums)):
    for kk in range(jj,len(aNums)):
        new=aNums[jj]+aNums[kk]
        if new>28123:
            continue
        else:
            aNums0.append(new)

print('Done getting sums of abundants')
total=0
for ii in range(1,28123):
    if ii not in aNums0:
        total+=ii

print(total)
# Old code, restarting from scratch

"""

  
def divAb(n):
    # Returns if n is abundant but without helper
    divs=[];
    for ii in range(1,int(n/2)+1):
        if n%ii==0 and ii not in divs:
            divs.append(ii);
        if sum(divs)>n:
            return True
    return False
abund=[]
for ii in range(1,15000):
    if divAb(ii):
        abund.append(ii)
tot=0
for jj in range(1,28123):
    if jj%2==0:
        if jj in abund:
            continue
            # Check first terms of abund, dont go full
       
    tot+=jj
aNums=[]
for ii in range(12,28124):
    if isAbundant(ii):
        aNums.append(ii)
print("Done generating abundants.")
total=0;
for jj in range(1,28123):
    if jj%2==0:
        if jj in aNums or jj>40:
            continue
        else:
            total+=jj
    else:
        total+=jj
print(total)
"""