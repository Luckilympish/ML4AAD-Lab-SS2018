# Machine Learning For Automated Algorithm Design
## Exercise 2
#### Authors:
- Gresa Shala
- Youssef El Hassani
- Jan Reisacher

### Task 1:
Run via jupyter notebook or colab

### Task 2:
Run via jupyter notebook or colab

### Task 3:
Plots for the performance comparison between the default configuration and each incumbent can be found at

* lpg_depots/validate1/plot_validation.png
* lpg_depots/validate2/plot_validation.png
* lpg_depots/validate3/plot_validation.png
* lpg_depots/validate4/plot_validation.png

### Task 4:
As our benchmark, we chose a simple convnet on the MNIST dataset using the Keras package.
Keras is a user-friendly package for working with neural networks in Python.
The model of the convolutional network was taken from the examples which are provided in the keras package GitHub:
https://github.com/keras-team/keras/blob/master/examples/mnist_cnn.py

Thus, our target algorithm is a python function, whose return value (1 - accuracy of the model) will be optimized by SMAC.
Since there already was an AbstractBlackBoxWrapper for python functions provided in the examples of GenericWrapper4AC, we made use of that script: https://github.com/mlindauer/GenericWrapper4AC/blob/master/examples/BlackBoxPython/abstractBlackBoxWrapper.py

The configuration space we chose for SMAC consists of:

* optimizer - *the optimizer for the model*
* opt_lr - *the learning rate of the optimizer*
* opt_momentum - *the momentum of the optimizer (useful only for optimizer 'SGD')*
* opt_decay - *the decay (useful for all except for 'Nadam')*
* opt_nesterov - *useful only for 'SGD'*
* opt_rho - *useful for 'RMSprop' and 'Adadelta'*
* opt_beta1 - *useful for 'Adam', 'Adamax', 'Nadam'*
* opt_beta2 - *useful for 'Adam', 'Adamax', 'Nadam'*
* batch_size - *batch size of the input*
* epochs - *number of epochs of training*
* activation_1 - *activation function to be applied to input of layer 1*
* activation_2 - *activation function to be applied to input of layer 2*
* activation_3 - *activation function to be applied to input of layer 3*
* activation_4 - *activation function to be applied to input of layer 4*
* neurons_1 - *number of neurons in the first layer of the model*
* neurons_2 - *number of neurons in the second layer of the model*
* neurons_3 - *number of neurons in the third layer of the model*
* dropout_1 - *dropout of the input*
* dropout_2 - *dropout of the input*

The default values as well as the boundaries of the values of the configuration parameters can be found in 
*HPO_deep_neural_net/dn_net/params.pcs*

As for the instance sets for the configuration, we decided to separate the 60000 training data images MNIST contains in 6 equal parts which will serve as individual training instances.

The indexes of the boundaries for each of the instances are written in instances/train.instanceX.csv, where X is 1,...,6. The data is loaded in the code from the keras.datasets library and then split accordingly.

The plot for the comparison of the performance of SMAC's incumbents to the default configuration can be found in 
*HPO_deep_neural_nets/plot_SMAC.png*

The plot for the comparison of the performance of SMAC and ROAR can be found in 
*HPO_deep_neural_nets/plot_SMAC_vs_ROAR.png*
