# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:59:24 2020

@author: cukel
"""

m2d = [31,28,31,30,31,30,31,31,30,31,30,31];

def dater(start,stop):
    # Sunday is first day of week
    # Start = [1901,01,19, 2]
    # Stop = [2000,12,31, 0]
    sunCount=0;
    year=start[0];
    month=start[1];
    day=start[2];
    wkday=start[3];
    while year<stop[0]:
        #print(year)
        while month<12:
            #print('m',month)
            if wkday==0:
                sunCount+=1;
            while day<=m2d[month]:
               # print('d',day)
                day+=1
                wkday+=1
                if wkday>6:
                    wkday=0;
            if month==1:
                if year%4==0:
                    day+=1
                    wkday+=1
                    if wkday>6:
                        wkday=0
            day=1;
            month+=1;
        month=0
        year+=1;
    return sunCount
    