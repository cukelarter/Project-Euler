# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:20:30 2020

@author: cukel
"""

def Pn(n):
    # Returns pentagonal number n
    return int(n*(3*n-1)/2)

def Dn0k(k,n0):
    # Returns difference values between two pentagonal numbers
    # k is index of first/starting pentagonal number
    # j is index of ending pentagonal number
    # n0 is the difference in between k and j
    return(1/2)*(n0)*(1-3*n0-6*k)

def isPn(n):
    # Returns if n is pentagonal
    ii=1;
    while Pn(ii)<n:
        ii+=1
    if Pn(ii)==n:
        return True
    return False

lowest=1000000; #arbitrary
k_pot=[];n0_pot=[];
for kk in range(1,10):
    for n0 in range(1,10):
        d=abs(Pn(kk)-Pn(kk+n0))
        s=abs(Pn(kk)+Pn(kk+n0))
        if isPn(d) and isPn(s):
            if d<lowest:
                print('ding!')
                lowest=d
                k_pot.append(kk)
                n0_pot.append(n0)

"""
        
# Generate pentagona numbers first
def genPen(N):
    # returns all pentagonal numbers between P0 and PN, inclu
    # ex: N=4: [1,5,12,22]
    n=1; pens=[]; p_n=n*(3*n-1)/2;
    while n<=N:
        pens.append(int(p_n))
        n+=1; p_n=n*(3*n-1)/2;
    return pens

def isPen(num):
    # returns if n is pentagonal
    # computationally less complex than 'in' function
    n=1; p_n=n*(3*n-1)/2;
    while p_n<num:\
        n+=1; p_n=n*(3*n-1)/2;
    if p_n==num:
        return True
    return False


# search through pens incrementally
def searcher(pens,d=1):
    # searches through pens to find vals that meet criteria
    # d = k-j, a set range to be searched
    #pens=genPen(N)
    low=1000000; # Arbitrarily high number
    for ii in range(len(pens)-d):
        pk=pens[ii]; pj=pens[ii+d];
        S = pk+pj; D = abs(pk-pj)
        if isPen(S) and isPen(D):
            if D<low:
                low=D
    return low


lowest=1000000
N=10000;
pens=genPen(N)
for d in range(1,100):
    if d%10==0:
        print(lowest)
    low0=searcher(pens,d)
    if low0<lowest:
        lowest=low0
"""