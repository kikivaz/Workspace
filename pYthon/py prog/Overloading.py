# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:46:48 2019

@author: faculty
"""

class OverLoading:
    
    def __init__(self,a):
        self.a=a
    
    def printval(self):
        print(self.a)
    def __add__(self,other):
        return self.a + other.a
    def __sub__(self,other):
        return self.a-other.a
    def __gt__(self,other):
        if self.a>other.a:
            return self.a
        else:
            return other.a
o1 = OverLoading(10)
o2 = OverLoading(20)
o1.printval()
o2.printval()
print(o1>o2)