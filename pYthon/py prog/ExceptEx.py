# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 18:56:36 2019

@author: faculty
"""

lst = [12,13,14,17]

try:
    n = int(input("enter a number"))
    res = lst[2]/n
except IndexError as i:
    print(i," out of list")

except (TypeError,ValueError) as t:
    print(t," error in type of value passed")
else:
    print(res)
print("end of program")