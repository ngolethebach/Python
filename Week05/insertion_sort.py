# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:25:03 2021

@author: The Bach
"""

def insertion_sort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] =array[j]
            j -= 1
        array[j+1] = key
        
        
array = []
for i in range(5):
    number = int(input("Enter 5 numbers: "))
    array.append(number)
insertion_sort(array)
print("Sorted array is: ")
for i in range(5):
    print("{}".format(array[i]))
            