# https://en.wikipedia.org/wiki/Convolutional_neural_network
import os
import numpy as np
import matplotlib.pyplot as plt

# keras
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
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

# reshape and set type
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

# normalize
X_train = X_train / 255
X_test = X_test / 255

# one-hot encoding (https://en.wikipedia.org/wiki/One-hot)
Y_train = np_utils.to_categorical(Y_train, n_classes)
Y_test = np_utils.to_categorical(Y_test, n_classes)
#print(Y_train.shape)
#print(Y_test.shape)

# neural network: sequential model (https://keras.io/models/sequential/)
# -----------------------------------------------------------------
model = Sequential()

# layers
model.add(Conv2D(filters=32, kernel_size=(5, 5), activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(n_classes, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(n_classes, activation='softmax'))

# plot model
#plot_model(model, to_file='plot.png', show_shapes=True)

# training (https://keras.io/optimizers/)
# -----------------------------------------------------------------
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adadelta')

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

# 0.029002553918152263
# 0.9906

'''
Michael Sjoeberg
2020-04-10
https://github.com/michaelsjoeberg/python-playground/blob/master/neural-networks/convolutional-neural-network-with-keras.py
'''