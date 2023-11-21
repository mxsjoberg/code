# https://en.wikipedia.org/wiki/Multilayer_perceptron
import os
import numpy as np
import matplotlib.pyplot as plt

# keras
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation
from keras.utils import np_utils, plot_model

# avoid libiomp5 error and less noise
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
os.environ['CUDA_VISIBLE_DEVICES'] = ''

# configuration variables
# -----------------------------------------------------------------
batch_size = 128
n_classes = 10
epochs = 5

# load data (https://keras.io/datasets/)
# -----------------------------------------------------------------
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# plt.figure()
# for i in range(9):
#   plt.subplot(3, 3, i + 1)
#   plt.tight_layout()
#   plt.imshow(X_train[i], cmap='gray', interpolation='none')
#   plt.title("{}".format(Y_train[i]))
#   plt.xticks([])
#   plt.yticks([])
# plt.savefig('figure.png')

# print(X_train.shape)
# print(X_test.shape)

# reshape and set type
X_train = X_train.reshape(X_train.shape[0], 784)
X_test = X_test.reshape(X_test.shape[0], 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

# normalize
X_train = X_train / 255
X_test = X_test / 255
# print(X_train.shape)
# print(X_test.shape)

# one-hot encoding (https://en.wikipedia.org/wiki/One-hot)
Y_train = np_utils.to_categorical(Y_train, n_classes)
Y_test = np_utils.to_categorical(Y_test, n_classes)
# print(Y_train.shape)
# print(Y_test.shape)

# neural network: sequential model (https://keras.io/models/sequential/)
# -----------------------------------------------------------------
model = Sequential()

# layer 1
model.add(Dense(512, input_shape=(784, )))
model.add(Activation('relu'))
model.add(Dropout(0.2))

# layer 2
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))

# layer 3
model.add(Dense(n_classes))
model.add(Activation('softmax'))

# plot model
# plot_model(model, to_file='mnist_mlp_network.png', show_shapes=True)

# training (https://keras.io/optimizers/)
# -----------------------------------------------------------------
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

# train model
model.fit(
    X_train,
    Y_train,
    validation_data=(X_test, Y_test),
    epochs=epochs,
    batch_size=batch_size,
    verbose=2
)

# evaluate
# -----------------------------------------------------------------
metrics = model.evaluate(X_test, Y_test, verbose=2)

loss = metrics[0]
accuracy = metrics[1]
print(loss)
print(accuracy)

# 0.060108443084184546
# 0.9802