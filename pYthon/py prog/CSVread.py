# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:34:05 2019

@author: faculty
"""

import pandas as pd
csv_file_Read = "D:\\April\\TechCrunchcontinentalUSA.csv"
csv_file_Write = "D:\\April\\NewTSVData.tsv"

csv_read = pd.read_csv(csv_file_Read)

#print(csv_read.tail(5))

with open(csv_file_Write,'w') as csv_write:
    csv_write.write(csv_read.to_csv(sep='\t',index=False))




csv_write.close()
