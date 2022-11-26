# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:10:59 2021

@author: The Bach
"""

# Alphabetical


sort_list=["","","","",""]
for item in range(0,5):
    sort_list[item]=input("Enter string {}: ".format(item+1))
sort_list.sort()
for item in sort_list:
    print(item)