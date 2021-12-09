# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:42:46 2019

@author: faculty
"""

import numpy as np
import pandas as pd
#test set size
test_size = 0.33
# names of the files to output the samples
w_filenameTrain = 'D:\\April\\trainset.csv'
w_filenameTest  = 'D:\\April\\testset.csv'

data = pd.read_csv("D:\\April\\employees.csv")
# create a variable to flag the training sample
data['train']  = np.random.rand(len(data)) < (1 - test_size)

# split the data into training and testing
train = data[data.train]
test  = data[~data.train]

print(train)
#print(test)

# output the samples to files
with open(w_filenameTrain,'w') as write_csv:
    write_csv.write(train.to_csv(sep=',', index=False))

with open(w_filenameTest,'w') as write_csv:
    write_csv.write(test.to_csv(sep=',', index=False))