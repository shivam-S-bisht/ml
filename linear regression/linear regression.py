import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importng the dataset
dataset = pd.read_csv('Salary_Data.csv')


#independent and dependent variables
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


#training and testing 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)


#imprting the linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#predict the values on test set
y_predict = regressor.predict(X_test)
print(y_predict)
print(y_test)

# visualising thhe data
plt.scatter(X_test, y_test, color = 'blue')
plt.plot(X_test, y_predict, color = 'red')
plt.show()