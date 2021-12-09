# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 17:39:30 2019

@author: faculty
"""

import pandas as pd

def normalize(col):
    return (col-col.min())/(col.max()-col.min())

def standerdize(col):
    return (col - col.mean())/col.std()

FileName = "D:\\April\\impute\\realEs_price_imptd.csv"
n_writeFileName = "D:\\April\\impute\\n_data.csv"
s_writeFileName = "D:\\April\\impute\\s_data.csv"

csv_read = pd.read_csv(FileName)

csv_read['n_price_mean'] = normalize(csv_read['price_mean'])  
csv_read['s_price_mean'] = standerdize(csv_read['price_mean'])   

with open(n_writeFileName,'w') as write_csv_n:
    write_csv_n.write(csv_read.to_csv(sep=',',index=False))
write_csv_n.close()

with open(s_writeFileName,'w') as write_csv_s:
    write_csv_s.write(csv_read.to_csv(sep=',',index=False))
write_csv_s.close()

