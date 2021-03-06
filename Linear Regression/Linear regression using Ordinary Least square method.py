# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:22:44 2020

@author: pulki
"""


#https://acadgild.com/blog/2linear-regression-case-study-2
#X = number of claims, Y = total payment for all the claims in thousands of Swedish Kronor for geographical zones in Sweden

#import Necessary Libraries

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)


#https://s3.amazonaws.com/acadgildsite/wordpress_images/datasets/slr06/slr06.xls
data=pd.read_excel('https://s3.amazonaws.com/acadgildsite/wordpress_images/datasets/slr06/slr06.xls')
data.values
print(data.shape)
data.head().values

X = data.iloc[:,0].values
X
Y = data.iloc[:,1].values
Y

mean_x = np.mean(X)
mean_y = np.mean(Y)
# Total number of values
m = len(X)
m
numer = 0
denom = 0
for i in range(m):
   numer += (X[i] - mean_x)*(Y[i] - mean_y)
   denom += (X[i] - mean_x)**2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)
# Print coefficients
print(b1, b0)

# Plotting Values and Regression Line
max_x = np.max(X) + 100
min_x = np.min(X) - 100
# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x
# Ploting Line
plt.plot(x, y, color='#58b970', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')
plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()


# Calculating Root Mean Squares Error
rmse = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]
    rmse += (Y[i] - y_pred) ** 2
rmse = np.sqrt(rmse/m)
print(rmse)

ss_t = 0
ss_r = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print(r2)


