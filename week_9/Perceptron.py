import numpy as np


class Perceptron(object):

    #==========================================#
    # The init method is called when an object #
    # is created. It can be used to initialize #
    # the attributes of the class.             #
    #==========================================#
    def __init__(self, no_inputs, max_iterations=20, learning_rate=0.1):
        self.no_inputs = no_inputs
        self.weights = np.ones(no_inputs) / no_inputs
        self.max_iterations = max_iterations
        self.learning_rate = learning_rate

    #=======================================#
    # Prints the details of the perceptron. #
    #=======================================#
    def print_details(self):
        print("No. inputs:\t" + str(self.no_inputs))
        print("Max iterations:\t" + str(self.max_iterations))
        print("Learning rate:\t" + str(self.learning_rate))

    #=========================================#
    # Performs feed-forward prediction on one #
    # set of inputs.                          #
    #=========================================#
    def predict(self, inputs):
        a = np.dot(inputs,self.weights)
        if a > 0:
            return 1
        elif a <= 0:
            return 0

    #======================================#
    # Trains the perceptron using labelled #
    # training data.                       #
    #======================================#
    def train(self, training_data, labels):
        assert len(training_data) == len(labels)
        
        #w_bar = w_bar + r (t - y) x_bar
        
        #x_bar = learning vector, training_data
        #w_bar = weights, self.weights
        #t = label, labels
        #y = predicted value, self.predict(training_data[i][w_i])
        #r = learning rate, self.learning_rate
        self.test(training_data, labels)
        
        for _ in range(self.max_iterations):
            for i in range(len(training_data)):
                y = self.predict(training_data[i])
                err = labels[i] - y
                for w_i in range(len(self.weights)):
                    self.weights[w_i] += (err * training_data[i][w_i]) * self.learning_rate
        
        return labels
                
    #=========================================#
    # Tests the prediction on each element of #
    # the testing data.
    #=========================================#
    def test(self, testing_data, labels):
        accuracy = 0.0
        j = 0
        # All of labels compair to all predicted weights
        for i in range(len(testing_data)):
            print("Actual " + str(labels[i]) + " est " + str(self.predict(testing_data[i])))
            if labels[i] == self.predict(testing_data[i]):
                j += 1
        
        accuracy = (j / len(labels)) * 100 
        print("Accuracy:\t"+str(accuracy))


