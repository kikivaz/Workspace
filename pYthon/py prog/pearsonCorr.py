# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:15:40 2019

@author: faculty
"""
import pandas as pd
n_writeFileName = "D:\\April\\impute\\n_data.csv"

csv_read = pd.read_csv(n_writeFileName)

csv_corr = csv_read.corr(method ='spearman').transpose()

print(csv_corr)