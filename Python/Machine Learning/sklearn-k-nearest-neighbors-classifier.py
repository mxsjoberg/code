# https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
import numpy as np
from sklearn import datasets
# https://pypi.org/project/tabulate/
from tabulate import tabulate

# load iris dataset
iris = datasets.load_iris()
# sample to test classifier
sample = np.array([
    [1, 9, 0, 4, 5, 3, 2],
    [9, 0, 4, 5, 3, 2, 1],
    [0, 4, 5, 3, 2, 1, 9],
    [4, 5, 3, 2, 1, 9, 0]
])
sample = sample / np.array([2.3, 4, 1.5, 4]).reshape(-1, 1)
sample = sample + np.array([4, 2, 1, 0]).reshape(-1, 1)
sample = sample.transpose()

# sklearn
# -----------------------------------------
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# split training dataset
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# training and predictions
classifier = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
classifier.fit(X_train, Y_train)

# evaluate
Y_prediction = classifier.predict(X_test)
# print(confusion_matrix(Y_test, Y_prediction))
print(classification_report(Y_test, Y_prediction))
#               precision    recall  f1-score   support

#            0       1.00      1.00      1.00        11
#            1       0.91      0.91      0.91        11
#            2       0.88      0.88      0.88         8

#     accuracy                           0.93        30
#    macro avg       0.93      0.93      0.93        30
# weighted avg       0.93      0.93      0.93        30
print(accuracy_score(Y_test, Y_prediction))
# 0.9333333333333333

# predict sample
Y_prediction = classifier.predict(sample)

table = list(zip([list(np.round(x, 1)) for x in sample], Y_prediction))
print(tabulate(table, headers=['sample', 'label'], tablefmt="simple"))
# sample                  label
# --------------------  -------
# [4.4, 4.2, 1.0, 1.0]        0
# [7.9, 2.0, 3.7, 1.2]        1
# [4.0, 3.0, 4.3, 0.8]        1
# [5.7, 3.2, 3.0, 0.5]        1
# [6.2, 2.8, 2.3, 0.2]        0
# [5.3, 2.5, 1.7, 2.2]        0
# [4.9, 2.2, 7.0, 0.0]        2
