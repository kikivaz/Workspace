# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:27:55 2019

@author: faculty
"""

import pandas as pd
n_writeFileName = "D:\\April\\impute\\n_data.csv"

csv_read = pd.read_csv(n_writeFileName)

csv_read.hist(column='price_mean',by='beds',xlabelsize=8,ylabelsize=8,sharex=True,sharey=True,figsize=(9,9))
