#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:40:49 2020

@author: colors
"""
#bubble sort
list1=[5,4,7,3,9,2,8,1,6]
print("list1:",list1)
list2=[]
k=0
for j in range(len(list1)):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]: 
            list1[i],list1[i+1]= list1[i+1],list1[i]
            
    list2.append(list1[i+1+k])
    k=k-1
print("ascending order of the list is ",list1)
print("descending order of the list is",list2)


