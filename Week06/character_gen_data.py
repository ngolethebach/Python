# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:40:28 2021

@author: The Bach
"""

# Character Generator
import json
try:
    with open("char_classes.json") as f:
        data=json.load(f)
except FileNotFoundError:
    print("File doesn't exist")
else:
    print("{:14} {:9} {:14} {:10} {:10} {:13}".format("Class","Strength","Intelligence","Wisdom","Dexterity","Constitution"))
    for i in data:
        print("{:12}".format(i), end=" ")
        for j in data[i]:
            print("{:>6}".format(data[i][j]), end="      ")
        print()
finally:
    print("")
            