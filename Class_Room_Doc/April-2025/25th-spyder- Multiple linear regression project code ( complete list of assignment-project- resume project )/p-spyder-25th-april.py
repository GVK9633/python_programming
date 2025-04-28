# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 09:06:17 2025

@author: RENUKA
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r'C:\Users\RENUKA\OneDrive\Desktop\vijay\GitRepo\python_programming\Class_Room_Doc\April-2025\investment.csv')
#independe
x= dataset.iloc[:,:-1]
#dependentvariable
y=dataset.iloc[:,4]
x=pd.get_dummies(x,dtype=int)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

m_coef = regressor.coef_
print(m_coef)

c_inter = regressor.intercept_
print(c_inter)

x=np.append(arr=np.ones((50,1)).astype(int),values=x,axis=1)

''''
arr = np.ones((50, 1)).astype(int)  # Create an array of ones with shape (50, 1) and type int
x = np.append(arr, values, axis=1) 
'''

import statsmodels.api as sm
x_opt=x[:,[0,1,2,3,4,5]]
#ordinaryLastSquares
regressor_OLS = sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

# recursive feature eliminate

import statsmodels.api as sm
x_opt=x[:,[0,1,2,3,5]]
#ordinaryLastSquares
regressor_OLS = sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

import statsmodels.api as sm
x_opt=x[:,[0,1,2,3]]
#ordinaryLastSquares
regressor_OLS = sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

import statsmodels.api as sm
x_opt=x[:,[0,1,3]]
#ordinaryLastSquares
regressor_OLS = sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

import statsmodels.api as sm
x_opt=x[:,[0,1]]
#ordinaryLastSquares
regressor_OLS = sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

