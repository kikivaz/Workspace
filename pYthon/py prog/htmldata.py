# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:37:01 2019

@author: faculty
"""
import pandas as pd
import re
url = "https://en.wikipedia.org/wiki/List_of_airports_by_IATA_code:_A"
url_read = pd.read_html(url, header = 0)[0]
space = re.compile(r'\s+')
def fix_string_spaces(colToFix):
    tempColName=[]
    for item in colToFix:
        if space.search(item):
            tempColName.append('_'.join(space.split(item)))
        else:
            tempColName.append(item)
    return tempColName
url_read.columns = fix_string_spaces(url_read.columns)
print(url_read.columns)

url_read.dropna(thresh=2,inplace=True)

url_read.index = range(0,len(url_read))
print(url_read.head(10))

