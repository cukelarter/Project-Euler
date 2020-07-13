# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:28:04 2020

@author: cukel
"""


def num2words(abcd):
    # Converts string abcd to representative word
    # ex. 0014 -> fourteen
    # Usable for up to 1000, represented using digits
    
    ret='';
    a = int(abcd[0]);b=int(abcd[1]);c=int(abcd[2]);d=int(abcd[3]);
    n=['','one','two','three','four','five','six','seven','eight','nine'];
    teens=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    hunds=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    m=['thousand','hundred']
    if a>0:
        ret+=n[a];
        ret+=m[0];
    if b>0:
        ret+=n[b];
        ret+=m[1];
        if c+d>0:
            ret+='and'
    if c==0:
        ret+=n[d];
    elif c==1:
        ret+=teens[d];
    else:
        ret+=(hunds[c]+n[d])
    return ret
        
def prepper(n):
    # Returns abcd from n
    abcd=str(n);
    while len(abcd)<4:
        abcd='0'+abcd;
    return abcd

total=0;
for ii in range(1,1001):
    yo=num2words(prepper(ii))
    print(len(yo),yo)
    total+=len(yo)
print(total)