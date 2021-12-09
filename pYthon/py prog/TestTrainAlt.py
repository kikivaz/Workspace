# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:28:32 2019

@author: faculty
"""

from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

w_filenameTrain = 'D:\\April\\trainset1New.csv'
w_filenameTest  = 'D:\\April\\testsetNew.csv'


data = pd.read_csv("D:\\April\\realEstate_trans.csv")

#print(data.columns)

x = data[['zip', 'beds', 'sq__ft']]
y=data['price'].to_frame()


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

#print(type(y_test))

train = pd.DataFrame(np.append(x_train,y_train,1),columns=['zip', 'beds', 'sq__ft', 'price'])
#print(train)

test = pd.DataFrame(np.append(x_test, y_test,1),columns=['zip', 'beds', 'sq__ft', 'price'])
#print(test)
with open(w_filenameTrain,'w') as write_csv:
    write_csv.write(train.to_csv(sep=',', index=False))

with open(w_filenameTest,'w') as write_csv:
    write_csv.write(test.to_csv(sep=',', index=False)) 