# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:34:15 2019

@author: faculty
"""

import pandas as pd 

data = pd.read_csv("D:\\April\\employees.csv") 
  
# generating one row  
sampledata1 = data.sample(frac=0.5) #if using n give integer value

print(sampledata1)


