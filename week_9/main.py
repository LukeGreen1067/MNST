# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 14:40:56 2022

@author: lukeg
"""

import numpy as np


from Perceptron import Perceptron


data_path = "./"
train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")

target_digit = 7
# Replacing first letter with a bias value
train_input = [ np.append([1],d[1:]) for d in train_data]# Separating the labels from the image
train_label = [ int(d[0]==target_digit) for d in train_data]

test_input = [ np.append([1],d[1:]) for d in test_data]# Separating the labels from the image
test_label = [ int(d[0]==target_digit) for d in test_data]

no_inputs = 785

P = Perceptron(no_inputs)


logic_input = []
logic_input.append(np.array([1, 0, 0]))
logic_input.append(np.array([1, 0, 1]))
logic_input.append(np.array([1, 1, 0]))
logic_input.append(np.array([1, 1, 1]))
 
logic_input2 = []
logic_input2.append(np.array([1, 0, 0]))
logic_input2.append(np.array([1, 0, 1]))

logic_label_or = [0, 1, 1, 1]
logic_label_and = [0, 0, 0, 1]
logic_label_not = [1, 0]



print(P.print_details())
P.test(test_data, (P.train(train_input, train_label)))