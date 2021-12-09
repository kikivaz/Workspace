# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 18:03:15 2019

@author: faculty
"""

import pickle

fp = open("D:\\April\\task1.txt","r")

content1 = pickle.load(fp)
content2 = pickle.load(fp)
print(content1)
print(content2)
fp.close()