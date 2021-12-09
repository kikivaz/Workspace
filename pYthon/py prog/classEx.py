# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 18:18:44 2019

@author: faculty
"""

class Student:
   x=10
   
   def __init__(self,name,age):
       self.name = name
       self.age = age
   
   def getval(self):
       print(self.name)
       print(self.age)
   
   @staticmethod
   def printx():
       print(Student.x)
        

s = Student('Ravi',26)
s1 = Student('Ron',22)

Student.printx()
s.getval()

s1.getval()