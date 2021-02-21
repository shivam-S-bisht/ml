import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Position_Salaries.csv')
print(dataset)

X = dataset.iloc[:, 1:2]
y = dataset.iloc[:, 2]
print(X)

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 4)
