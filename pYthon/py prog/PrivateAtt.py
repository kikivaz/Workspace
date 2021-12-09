# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 13:31:16 2019

@author: faculty
"""

class Sample:
    def __init__(self,x,y,z):
        self.x=x
        self.__y=y
        self._z=z
    def display(self):
        print(self.x)
        print(self.__y)
        print(self._z)

class NewSample(Sample):
    
    def show(self):
        print(self.x)
        print(self.__y)
        print(self._z)

n = NewSample(1,20,4)
n.show()

