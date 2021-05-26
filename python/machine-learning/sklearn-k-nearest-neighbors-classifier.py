# https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
import numpy as np
from prettytable import PrettyTable

# load iris dataset
# -----------------------------------------
from sklearn import datasets
iris = datasets.load_iris()

# sample test data
# -----------------------------------------
S_test = np.array([
    [1, 9, 0, 4, 5, 3, 2],
    [9, 0, 4, 5, 3, 2, 1],
    [0, 4, 5, 3, 2, 1, 9],
    [4, 5, 3, 2, 1, 9, 0]]
)
S_test = S_test / np.array([2.3, 4, 1.5, 4]).reshape(-1, 1)

# S_test
S_test = S_test + np.array([4, 2, 1, 0]).reshape(-1, 1)
S_test = S_test.transpose()

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
# Y_prediction = classifier.predict(X_test)
# print(confusion_matrix(Y_test, Y_prediction))
# print(classification_report(Y_test, Y_prediction))
# print(accuracy_score(Y_test, Y_prediction))

# sample classification
# -----------------------------------------
Y_prediction = classifier.predict(S_test)
# print(Y_prediction)

# prettytable
# -----------------------------------------------------------
pt = PrettyTable(('sample', 'class'))
for row in list(zip(np.round(S_test, 4), Y_prediction)): pt.add_row(row)

pt.align['sample'] = 'l'
pt.align['class'] = 'c'

print(pt)

# +-------------------------------+-------+
# | sample                        | class |
# +-------------------------------+-------+
# | [4.4348 4.25   1.     1.    ] |   0   |
# | [7.913  2.     3.6667 1.25  ] |   1   |
# | [4.     3.     4.3333 0.75  ] |   1   |
# | [5.7391 3.25   3.     0.5   ] |   1   |
# | [6.1739 2.75   2.3333 0.25  ] |   0   |
# | [5.3043 2.5    1.6667 2.25  ] |   0   |
# | [4.8696 2.25   7.     0.    ] |   2   |
# +-------------------------------+-------+