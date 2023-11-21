# https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# suppress url ssl error (not on our end)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# assign column names
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# read dataset into dataframe
dataset = pd.read_csv(url, names=names)
# dataset.head()

# preprocessing (selecting data)
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

# train-test split: 80% is training data, 20% is testing data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)

# apply feature scaling
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# training and predictions
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, Y_train)

Y_prediction = classifier.predict(X_test)
# Y_prediction

# evaluate
print(confusion_matrix(Y_test, Y_prediction))
print(classification_report(Y_test, Y_prediction))

# [[ 8  0  0]
#  [ 0 11  1]
#  [ 0  0 10]]
#                  precision    recall  f1-score   support
#
#     Iris-setosa       1.00      1.00      1.00         8
# Iris-versicolor       1.00      0.92      0.96        12
#  Iris-virginica       0.91      1.00      0.95        10
#
#        accuracy                           0.97        30
#       macro avg       0.97      0.97      0.97        30
#    weighted avg       0.97      0.97      0.97        30

'''
Michael Sjoeberg
2020-04-10
https://github.com/michaelsjoeberg/python-playground/blob/master/machine-learning/k-nearest-neighbors-with-sklearn.py
'''