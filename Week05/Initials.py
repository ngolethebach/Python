# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:54:36 2021

@author: The Bach
"""

# Initials


def print_initial_name(user_name):
    
    if len(user_name) == 0:
        return
    words = user_name.split()
    for word in words:
        print(word[0].upper(), end = " ")
    
    
user_name = input("Enter your name: ")
print_initial_name(user_name)
    
    
   