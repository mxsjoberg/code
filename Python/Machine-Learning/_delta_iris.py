# https://en.wikipedia.org/wiki/Delta_rule
import numpy as np
from prettytable import PrettyTable

# load iris dataset
# -----------------------------------------
from sklearn import datasets

iris = datasets.load_iris()

# test data
# -----------------------------------------------------------
S_test = np.array([
	[1, 9, 0, 4, 5, 6, 7],
	[9, 0, 4, 5, 6, 7, 1],
	[0, 4, 5, 6, 7, 1, 9],
	[4, 5, 6, 7, 1, 9, 0]]
)
S_test = S_test / np.array([2.3, 4, 1.5, 4]).reshape(-1, 1)

# X_test
X_test = S_test + np.array([4, 2, 1, 0]).reshape(-1, 1)
X_test = X_test.transpose()

# augment
X_test = np.insert(X_test, 0, np.ones(1), axis=1)

# configuration variables
# -----------------------------------------------------------
# initial values
w = [1, 2, 3, 4, 5]
#w = [s3, -s4, s5, -s6, s7] # ONLY CHANGE THIS

# learning rate
n = 0.1

# iterations (note: 2 epochs)
iterations = 2 * len(iris.data)

# dataset
# -----------------------------------------------------------
#X = [[1, 0, 2], [1, 1, 2], [1, 2, 1], [1, -3, 1], [1, -2, -1], [1, -3, -2]]
X = iris.data

t = []
A = []
for i in range(len(iris.target)):
	c = iris.target[i]
	if (c == 0):
		t.append(1)
		# augment iris data
		A.append([1, X[i][0], X[i][1], X[i][2], X[i][3]])
	else:
		t.append(0)
		# augment iris data
		A.append([0, X[i][0], X[i][1], X[i][2], X[i][3]])

X = A

# transfer_function (note: Heaviside function)
# -----------------------------------------------------------
def transfer_function(w, x):
	wx = np.dot(w, x)

	if (wx > 0):
		return 1
	elif (wx == 0):
		return 0.5
	else:
		return 0

assert (transfer_function([0.1, -0.5, 0.4], [0.1, -0.5, 0.4]) == 1)
assert (transfer_function([0.1, -0.5, 0.4], [0.1, 0.5, 0.4]) == 0)
assert (transfer_function([0, 0, 0], [0, 0, 0]) == 0.5)

# sequential delta learning algorithm
# -----------------------------------------------------------
result = []
for o in range(int(iterations / len(X))):
	for i in range(len(X)):
		if ((i + 1 + (len(X) * o)) > iterations): break

		w_prev = w
		x = X[i]
		y = transfer_function(w, x)

		# calculate update part
		update = np.zeros(len(x))
		for j in range(len(x)): update[j] = n * (t[i] - y) * x[j]

		# add update part to a
		w = np.add(w, update)

		# append result
		result.append((str(i + 1 + (len(X) * o)), np.round(w_prev, 4), np.round(x, 4), np.round(y, 4), np.round(t[i], 4), np.round(w, 4)))

# prettytable
# -----------------------------------------------------------
pt = PrettyTable(('iteration', 'w', 'x', 'y = H(wx)', 't', 'w_new'))
for row in result: pt.add_row(row)

pt.align['iteration'] = 'c'
pt.align['w'] = 'l'
pt.align['x'] = 'l'
pt.align['y = H(wx)'] = 'l'
pt.align['t'] = 'c'
pt.align['w_new'] = 'l'

print(pt)

#print(pt[150 - 1]) # epoch 1
#print(pt[-1]) # epoch 2

# pt_w_1 = PrettyTable(('sample, w=[0.4, -2.71, 5.83, -2.9, 1.93]', 'class'))
# for sample in X_test:
# 	pt_w_1.add_row([sample, transfer_function([0.4, -2.71, 5.83, -2.9, 1.93], sample)])

# print(pt_w_1)

# pt_w_2 = PrettyTable(('sample, w=[0.5, -2.26, 6.06, -2.77, 1.96]', 'class'))
# for sample in X_test:
# 	pt_w_2.add_row([sample, transfer_function([0.5, -2.26, 6.06, -2.77, 1.96], sample)])

# print(pt_w_2)

# TEST: accuracy
# -----------------------------------------------------------
# X_test = X
# result = []
# pt_test = PrettyTable(('sample, w=[0.4, -2.71, 5.83, -2.9, 1.93]', 'class', 'correct?'))
# for sample in X_test:
# 	c = transfer_function([0.4, -2.71, 5.83, -2.9, 1.93], sample)
# 	pt_test.add_row([sample, c, c == sample[0]])

# 	# append to result
# 	result.append(c == sample[0])

# print(pt_test)
# print(result.count(True) / len(result))
