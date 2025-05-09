# -*- coding: utf-8 -*-
"""
Created on Wed May  7 09:46:51 2025

@author: RENUKA
"""

#importing library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import dataset
dataset = pd.read_csv(r"C:\Users\RENUKA\OneDrive\Desktop\vijay\logit classification.csv")

x= dataset.iloc[:,[2,3]].values
y= dataset.iloc[:,-1].values

#split the date
from sklearn.model_selection import train_test_split
#x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=0)
#below code will work if give train size
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)

print(x_train.shape);
print(x_test.shape);
print(y_train.shape);
print(y_test.shape);
from sklearn.preprocessing import StandardScaler
sc= StandardScaler()
x_train = sc.fit_transform(x_train)   
x_test = sc.transform(x_test)