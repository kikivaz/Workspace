# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:39:07 2019

@author: faculty
"""

import collections
co = collections.Counter()

fp = open("D:\\April\\file1.txt","r")
for line in fp:
    co.update(line.lower())

for letter,count in co.most_common(1):
    #print("%s %d" % (letter,count))
    print(letter,count)