import sys
import re
import math
import logging
import numpy
import keras
import tensorflow
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from abstractBlackBoxWrapper import AbstractBlackBoxWrapper

class KerasWrapper(AbstractBlackBoxWrapper):
    
    def __init__(self):
        logging.basicConfig()
        AbstractBlackBoxWrapper.__init__(self)
        
    def get_value(self, instance, config):
        return self._get_accuracy_value(instance, config)
    def read_instance(self, instance):
        dataset = numpy.loadtxt(instance, delimiter=",")
        X = dataset.split("\n")
        X1 = []
        X3 = []
        for row in X:
            X1.append(row.split(","))
        for row in range(len(X1)):
            X2 = []
            for item in range(len(X1[row])):
                X2.append(float(X1[row][item]))
            X3.append(X2)
        return X3

    def _get_accuracy_value(self, instance, cfg):
        numpy.random.seed(1)
        tensorflow.set_random_seed(2)
        dataset = numpy.loadtxt(instance, delimiter=",")
        X = dataset[:,0:8]
        Y = dataset[:,8]
        X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.2)
	# create model
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(int(cfg["neurons"]), input_dim=8, kernel_initializer=cfg["kernel_initializer"], activation=cfg["activation"]))
        print(dataset)
        model.add(keras.layers.Dense(1, activation='sigmoid'))
        # Compile model
        model.compile(loss='binary_crossentropy', optimizer=cfg["optimizer"], metrics=['accuracy'])
        model.fit(X_train, y_train, batch_size=int(cfg["batch_size"]), epochs=int(cfg["epochs"]))
        y_pred = model.predict(X_test)
        y_pred = (y_pred > 0.5)
        return accuracy_score(y_test, y_pred)

if __name__ == "__main__":
    wrapper = KerasWrapper()
    wrapper.main()    
