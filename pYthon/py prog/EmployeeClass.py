# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:45:21 2019

@author: faculty
"""

class Employee:
    "this is a demo of Class concept"
    inc = 1.2
    def __init__(self,fname,lname,sal):
        self.f_name=fname
        self.l_name = lname
        self.salary = sal
    def showDetails(self):
        print("employee name: ",self.f_name+" "+self.l_name)
        print("salary amount: ",self.salary)
    def sal_Increase(self):
        self.salary = int(self.salary*self.inc)
        return self.salary
    
class PartTimers(Employee):
    def __init__(self,fname,lname,sal,days):
        Employee.__init__(self,fname,lname,sal)
        self.days=days
    
    def showDetails(self):
        print("employee name: ",self.f_name+" "+self.l_name)
        print("salary amount: ",self.salary)
        print("no of working days ",self.days)

class FullTimers(Employee):
    def __init__(self,fname,lname,sal,shift):
        Employee.__init__(self,fname,lname,sal)
        self.shift=shift
    
    def showDetails(self):
        print("employee name: ",self.f_name+" "+self.l_name)
        print("salary amount: ",self.salary)
        print("working shift ",self.shift)

e1 = FullTimers("Ram","Dhalal",25000,"Day")
e2 = FullTimers("Sam","Johnson",30000,"Night")


'''print(Employee.__doc__)
print("Employee one details ",e1.__dict__)
print("Employee two details ",e2.__dict__)'''

e1.showDetails()
e2.showDetails()

