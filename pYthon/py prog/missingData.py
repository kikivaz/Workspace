# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:47:41 2019

@author: faculty
"""

import pandas as pd

readFileName = "D:\\April\\impute\\realEs_less_dirty.csv"
writeFileName = "D:\\April\\impute\\realEs_price_imptd.csv"

csv_read = pd.read_csv(readFileName)


csv_read['price_mean'] = csv_read['price'].fillna(csv_read.groupby('zip')['price'].transform('mean'),inplace=False)
#csv_read['price0'] = csv_read['price'].fillna(method='bfill',inplace=False)


with open(writeFileName,'w') as write_csv:
    write_csv.write(csv_read.to_csv(sep=',',index=False))