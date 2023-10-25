# https://en.wikipedia.org/wiki/Convolutional_neural_network
import os
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from tqdm.keras import TqdmCallback

# avoid libiomp5 error and less noise
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
os.environ['CUDA_VISIBLE_DEVICES'] = ''

# configuration
batch_size = 128
n_classes = 10
epochs = 5

# https://keras.io/datasets
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# reshape and set type
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
# normalize
X_train = X_train / 255
X_test = X_test / 255
# https://en.wikipedia.org/wiki/One-hot
Y_train = to_categorical(Y_train, n_classes)
Y_test = to_categorical(Y_test, n_classes)
print(Y_train.shape)
print(Y_test.shape)

# https://keras.io/models/sequential
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

# https://keras.io/optimizers
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adadelta')

# train model
model.fit(
    X_train,
    Y_train,
    validation_data=(X_test, Y_test),
    epochs=epochs,
    batch_size=batch_size,
    verbose=0,
    callbacks=[TqdmCallback(verbose=1)]
)
# evaluate
metrics = model.evaluate(X_test, Y_test, verbose=2)
# metrics
loss = metrics[0]
accuracy = metrics[1]
print(loss)
print(accuracy)
# 0.029002553918152263
# 0.9906
