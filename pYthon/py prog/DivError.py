# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 18:39:45 2019

@author: faculty
"""

def div(a,b):
    res = a/b
    return res

x = int(input("Enter the numerator"))
y = int(input("Enter the denominator"))
print("Division operation")
result=0
try:
    result = div(x,y)
except ZeroDivisionError as z:
    print(z," Denominator is zero")
except Exception:
    print("error occured")
finally:
    print(result)
print("end of program")