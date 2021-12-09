# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:02:38 2019

@author: faculty
"""

from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report
actual = [1, 1, 0, 1, 0, 0, 1, 0, 1, 0] 
predicted = [1, 1, 1, 1, 0, 0, 1, 0, 0, 0] 

#using confusion matrix to analyse the data
results = confusion_matrix(actual, predicted) 

print('Confusion Matrix :')
print(results) 
accuracy  = accuracy_score(actual,predicted)
print("accuracy: ",accuracy)
print('report: ')
print(classification_report(actual,predicted))