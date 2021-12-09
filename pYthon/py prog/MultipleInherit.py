# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:39:21 2019

@author: faculty
"""


    
class B:
    def sum1(self):
        print("return subtracted value")
    
class A:
    def sum1(self):
        print("returns sum of values")
        
class C(B,A):
    pass

c = C()

c.sum1()
        