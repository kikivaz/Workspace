# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:25:22 2019

@author: faculty
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
'''
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
'''
data = pd.read_csv('D:\\April\\AirPassengers.csv')
print(data.head())
print('\n Data Types:')
print(data.dtypes)

from datetime import datetime
con=data['Month']
data['Month']=pd.to_datetime(data['Month'])
data.set_index('Month', inplace=True)
#check datatype of index
data.index
'''
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col='Month',date_parser=dateparse)
print data.head()
data.index
'''
#convert to time series:
ts = data['#Passengers']
ts.head(10)

#Specific the index as a string constant:
ts['1949-01-01']
#or use this
'''
ts[datetime(1949,1,1)]
'''

#Specify the entire range:
ts['1949-01-01':'1949-05-01']

#or use this

#Use ':' if one of the indices is at ends:
ts[:'1949-05-01']

#plot a graph
plt.plot(ts)

#define function for ADF test
from statsmodels.tsa.stattools import adfuller
def adf_test(timeseries):
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
       dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)

#apply adf test on the series
adf_test(data['#Passengers'])

#Kwiatkowski-Phillips   -Schmidt-Shin
#define function for kpss test
from statsmodels.tsa.stattools import kpss
#define KPSS
def kpss_test(timeseries):
    print ('Results of KPSS Test:')
    kpsstest = kpss(timeseries, regression='c')
    kpss_output = pd.Series(kpsstest[0:3], index=['Test Statistic','p-value','Lags Used'])
    for key,value in kpsstest[3].items():
        kpss_output['Critical Value (%s)'%key] = value
    print(kpss_output)

kpss_test(data['#Passengers'])
               
#data['#Passengers_diff'] = data['#Passengers']-data['#Passengers'].shift(1)
#data['#Passengers_diff'].dropna().plot()
data['#Passengers_log'] = np.log(data['#Passengers'])
data['#Passengers_log_diff'] = data['#Passengers_log']-data['#Passengers_log'].shift(1)
data['#Passengers_log_diff'].dropna().plot()