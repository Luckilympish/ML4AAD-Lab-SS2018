import sys
import re
import math
import logging
import numpy
import keras
from keras import optimizers
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import tensorflow
from abstractBlackBoxWrapper import AbstractBlackBoxWrapper

class KerasWrapper(AbstractBlackBoxWrapper):
    
    def __init__(self):
        logging.basicConfig()
        AbstractBlackBoxWrapper.__init__(self)
        
    def get_value(self, instance, config):
        return self._get_accuracy_value(instance, config)

    def _get_accuracy_value(self, instance, cfg):
        numpy.random.seed(1)
        tensorflow.set_random_seed(2)
        num_classes = 10
        img_rows, img_cols = 28, 28
        databounds = numpy.loadtxt(instance, delimiter=",", dtype='int')
        train_index = databounds[0]
        test_index = databounds[1]
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        if K.image_data_format() == 'channels_first':
            x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
            x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
            x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)

        x_train = x_train.astype('float32')
        x_test = x_test.astype('float32')
        x_train /= 255
        x_train=x_train[train_index[0]:train_index[1],:,:,:]
        x_test /= 255
        x_test=x_test[test_index[0]:test_index[1],:,:,:]
	# convert class vectors to binary class matrices
        y_train = keras.utils.to_categorical(y_train[train_index[0]:train_index[1]], num_classes)
        y_test = keras.utils.to_categorical(y_test[test_index[0]:test_index[1]], num_classes)

        model = Sequential()
        model.add(Conv2D(int(cfg["neurons_1"]), kernel_size=(3, 3),activation=cfg["activation_1"],input_shape=input_shape))
        model.add(Conv2D(int(cfg["neurons_2"]), (3, 3), activation=cfg["activation_2"]))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(float(cfg["dropout_1"])))
        model.add(Flatten())
        model.add(Dense(int(cfg["neurons_3"]), activation=cfg["activation_3"]))
        model.add(Dropout(float(cfg["dropout_2"])))
        model.add(Dense(num_classes, activation=cfg["activation_4"]))

        optimizer_str = cfg["optimizer"]
        if optimizer_str == 'SGD':
            nesterov = False
            if cfg["opt_nesterov"] == 'true':
                nesterov = True
            optimizer = optimizers.SGD(lr=float(cfg["opt_lr"]), momentum=float(cfg["opt_momentum"]), decay=float(cfg["opt_decay"]), nesterov=nesterov)
        elif optimizer_str == 'RMSprop':
            optimizer = optimizers.RMSprop(lr=float(cfg["opt_lr"]), rho=float(cfg["opt_rho"]), decay=float(cfg["opt_decay"]))
        elif optimizer_str == 'Adagrad':
            optimizer = optimizers.Adagrad(lr=float(cfg["opt_lr"]), decay=float(cfg["opt_decay"]))
        elif optimizer_str == 'Adadelta':
            optimizer = optimizers.Adadelta(lr=float(cfg["opt_lr"]), rho=float(cfg["opt_rho"]), decay=float(cfg["opt_decay"]))
        elif optimizer_str == 'Adam':
            optimizer = optimizers.Adam(lr=float(cfg["opt_lr"]), beta_1=float(cfg["opt_beta1"]), beta_2=float(cfg["opt_beta2"]), decay=float(cfg["opt_decay"]))
        elif optimizer_str == 'Adamax':
            optimizer = optimizers.Adamax(lr=float(cfg["opt_lr"]), beta_1=float(cfg["opt_beta1"]), beta_2=float(cfg["opt_beta2"]), decay=float(cfg["opt_decay"]))
        else :
            optimizer = optimizers.Nadam(lr=float(cfg["opt_lr"]), beta_1=float(cfg["opt_beta1"]), beta_2=float(cfg["opt_beta2"]))
        model.compile(loss=keras.losses.categorical_crossentropy, optimizer=optimizer, metrics=['accuracy'])

        model.fit(x_train, y_train, batch_size=int(cfg["batch_size"]), epochs=int(cfg["epochs"]), verbose=1, validation_data=(x_test, y_test))
        score = model.evaluate(x_test, y_test, verbose=0)
        return score[1]

if __name__ == "__main__":
    wrapper = KerasWrapper()
    wrapper.main()    
