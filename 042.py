# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 13:32:00 2020

@author: cukel
"""

# 162

k=open('txt_042.txt','r')
l=k.read()
m=l.split('","')

# First generate triangle numbers
# Find maximum number by finding length of largest word
# And assuming each letter is maximum value (Z=26)
# Ex: ADMINISTRATION -> ZZZZZZZZZZZZZZ

n=1; tri_nums=[]; tri=(1/2)*n*(n+1)
while tri<len(max(m,key=len))*26:
    tri_nums.append(int(tri))
    n+=1
    tri=(1/2)*n*(n+1)


# Then go through each word and see if its a triangle val
def letVal(c):
    # Returns letter value of string character c
    # Small helper function
    v_raw=ord(c)
    if v_raw<65 or v_raw>90:
        # Outside of normal capital letter range
        return 0
    else:
        return v_raw-64
    
def wordVal(st):
    # Returns word value of word c
    # Uses letVal as helper
    total=0
    for c in st:
        total+=letVal(c)
    return total

# Once word val is generated, it will search through triangle
# value list created previously. using 'in' function scales 
# poorly but when len(tri_nums)=26 it's still fast
t_count=0 
for word in m:
    if wordVal(word) in tri_nums:
        t_count+=1