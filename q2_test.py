# -*- coding: utf-8 -*-
"""Q2_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R-h6mR7sy_h7Yi1dKE4xCb8nKprgkVDj
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from linearRegression.linear_regression import LinearRegression
from metrics import *

np.random.seed(45)

N = 90
P = 10
X = pd.DataFrame(np.random.randn(N, P))
y = pd.Series(np.random.randn(N))
print(X.shape)

# Compute the analytical gradient of the unregularized mse_loss and mse_loss with ridge reg.
LR = LinearRegression(fit_intercept=True)
LR.fit_normal_equations(X,y)
grad = LR.compute_gradient(X,y,penalty = 'l2',c=2)
print(grad)

# print('Batch Gradient Descent with manual gradient computation for unregularized objective : ')


# LR = LinearRegression(fit_intercept=True)
# # Call Gradient Descent here

# y_hat = LR.predict(X)
# batchsize = 3
# print(' Batch size=',batchsize,', RMSE: ', rmse(y_hat, y))
# print(' Batch size=',batchsize,', MAE: ', mae(y_hat, y))
  
# print("---------------------------")


# #TODO :  Call the different variants of gradient descent here (as given in Q2)

#Evaluating solution of linear regression using gradient descent
# LR = LinearRegression(fit_intercept=True)
# LR._gradient(X,y,penalty = 'unregularized',iterations = 1000, alpha = 0.01)
# y_hat = LR.predict_gd(X)
# print('For linear regression using gradient descent : \n')
# print('RMSE: ', rmse(y_hat, y))
# print('MAE: ', mae(y_hat, y))
# print("---------------------------")