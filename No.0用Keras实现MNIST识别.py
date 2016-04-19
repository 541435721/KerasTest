# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/04/08_14:18 '

from numpy import *
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.datasets import mnist

model = Sequential()
model.add(Dense(784, 500, init='glorot_uniform'))  # 输入层，28*28=784
