# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:12:30 2019

@author: faculty
"""

class Student:
    
    def __init__(self,fname,lname,course):
        self.fname = fname
        self.lname = lname
        self.course = course
    
    def printDetails(self):
        print("Strudent name: ",self.fname+" "+self.lname)
        print("Student course: ",self.course)
        
class Dayscholar(Student):
    def __init__(self,fname,lname,course,route_no):
        Student.__init__(self,fname,lname,course)
        self.route_no=route_no
        
    def printDetails(self):
        print("Strudent name: ",self.fname+" "+self.lname)
        print("Student course: ",self.course)
        print("Student route: ",self.route_no)

class HostelStudent(Student):
    def __init__(self,fname,lname,course,room_no):
        Student.__init__(self,fname,lname,course)
        self.room_no=room_no
        
    def printDetails(self):
        print("Strudent name: ",self.fname+" "+self.lname)
        print("Student course: ",self.course)
        print("Student room no: ",self.room_no)

h = HostelStudent("Sam","Anderson","ECE",102)
h.printDetails()
d = Dayscholar("Ram","Kumar","MECH",47);
d.printDetails()
print(help(Student))