# -*- coding: utf-8 -*-
# """
# Created on Mon Apr 21 09:28:03 2025

# @author: RENUKA
# """

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
dataset = pd.read_csv(r"./21-April-Salary_Data.csv")
#dependent and independent variable
x= dataset.iloc[:,:-1].values
y= dataset.iloc[:,-1].values
#split the date
from sklearn.model_selection import train_test_split
#x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=0)
#below code will work if give train size
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred=regressor.predict(x_test)

plt.scatter(x_test, y_test, color ='red')
plt.plot(x_train,regressor.predict(x_train),color ='blue')
plt.title('salary vs experience (Test set)')
plt.xlabel("Years of experience")
plt.ylabel('salary')
plt.show()

m_slope = regressor.coef_
print(m_slope)

c_intercept = regressor.intercept_
print(c_intercept)

pred_12yr_emp_exp = m_slope*12+c_intercept
print(pred_12yr_emp_exp)

pred_20yr_emp_exp = m_slope*20+c_intercept
print(pred_12yr_emp_exp)

#22 april

# training score part-bias
bias = regressor.score(x_train,y_train)
print(bias)#94

#testing scroe part-variance
variance = regressor.score(x_test,y_test)
print(variance)#98

#stats for ml
dataset.mean()
dataset['Salary'].mean()
dataset['Salary'].median()
dataset['Salary'].mode()

#variance
dataset.var()
dataset['Salary'].var()

#standadar variaence
dataset.std()

#coefficient of variatiln 
from scipy.stats import variation
variation(dataset.values)
variation(dataset['Salary'])

#correlation range -1 to 1
dataset.corr()

#ssr
y_mean = np.mean(y)
SSR= np.sum((y_pred-y_mean)**2)
print(SSR)

#sse
y=y[0:6]
SSE=np.sum((y-y_pred)**2)
print(SSE)

#sst
mean_total = np.mean(dataset.values)
SST=np.sum((dataset.values-mean_total)**2)
print(SSE)

#r2
r_square = 1-SSR/SST
print(r_square)

import pickle

filename ='linear_regression_model.pkl'
with open(filename,'wb') as file:
    pickle.dump(regressor,file)
    
print("model has been pickled and saved")    

