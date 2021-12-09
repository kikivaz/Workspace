# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:58:49 2019

@author: faculty
"""

import pickle

lst1 = ['Ravi','Shyam','Ragav']
lst2 = ['Python','JAVA','Python']

fp = open("D:\\April\\task1.txt","wb")
pickle.dump(lst1,fp)
pickle.dump(lst2,fp)
fp.close()