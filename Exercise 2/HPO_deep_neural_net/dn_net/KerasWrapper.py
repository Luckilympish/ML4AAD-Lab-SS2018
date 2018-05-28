import sys
import re
import math
import logging

from abstractBlackBoxWrapper import AbstractBlackBoxWrapper

class KerasWrapper(AbstractBlackBoxWrapper):
    
    def __init__(self):
        logging.basicConfig()
        AbstractBlackBoxWrapper.__init__(self)
        
    def get_value(self, instance, config):
        return self._get_accuracy_value(instance, config)
    def read_instance(instance):
	    X = data.split("\n")
        X1 = []
        X3 = []
        for row in X:
        X1.append(row.split(","))
        for row in range(len(X1)):
            X2 = []
            for item in range(len(X1[row])):
                X2.appendfloat(X1[row][item]))
            X3.append(X2)
		return X3

    def _get_accuracy_value(self, instance, cfg):
	    dataset = self.read_instance(instance)
        X = dataset[:,0:8]
        Y = dataset[:,8]
        X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.2)
	    # create model
        model = Sequential()
        model.add(Dense(cfg["neurons"], input_dim=8, kernel_initializer=cfg["kernel_initializer"], activation=cfg["activation"]))
        model.add(Dense(1, activation='sigmoid'))
        # Compile model
        model.compile(loss='binary_crossentropy', optimizer=cfg["optimizer"], metrics=['accuracy'])
        model.fit(X_train, y_train, batch_size=cfg["batch_size"], epochs=cfg["epochs"])
        y_pred = model.predict(X_test)
        y_pred = (y_pred > 0.5)
        return accuracy_score(y_test, y_pred)

if __name__ == "__main__":
    wrapper = KerasWrapper()
    wrapper.main()    