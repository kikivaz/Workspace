# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:04:33 2019

@author: faculty
"""
import csv

csv_file_Read = "D:\\April\\TechCrunchcontinentalUSA.csv"
csv_lable=[]
csv_data=[]
with open(csv_file_Read,'r') as CSVread:
    csv_info = csv.reader(CSVread)
    csv_lable = csv_info.__next__()
    for rows in csv_info:
        csv_data.append(rows)
print(csv_lable,'\n')
print(csv_data[0:10],'\n')




