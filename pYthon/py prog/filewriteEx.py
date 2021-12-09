# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:05:47 2019

@author: faculty
"""

#file write operation

fp = open(r"D:\April\file1.txt","r")

lst = fp.read()
print(lst)
fp.close()