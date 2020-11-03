import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np



class NN:

    def __init__(self, parameter,dense):
        self.parameter = parameter
        self.dense = dense
        self.saver = tf.train.Saver()
        self.init = tf.global_variables_initializer()

    def load_model(self,x,y):

        inputs = tf.placeholder(tf.float32,shape=(None,x.shpae[1]), name="inputs")
        labels = tf.placeholder(tf.float32,shape=(None),name="labels")
        one_hot_ecoded_targets = tf.one_hot(labels, self.parameter.n_output)

        dense_layers = []

        tf.layers.dense(inputs,)

        for i,d in enumerate(self.dense):
             dense_layers.append(tf.layers.dense( dense_layers[i-1] if i > 0 else inputs ,d.nodes[i], activation=self.dense.activation, name=f"dense{i}"))

        outputs = tf.layers.dense(dense_layers[-1],self.parameter.n_output,name="output")

        loss = tf.nn.softmax_cross_entropy_with_logits_v2(labels=labels, logits=output)
        total_loss = tf.reduce_mean(loss,name="total_loss")

        optimizer = tf.train.GradientDescentOptimizer(self.parameter.learning_rate)
        training_optimizer = optimizer.minimize(optimizer)
        
        correct_list = tf.nn.in_top_k(outputs,labels, 1)

        accuracy = tf.reduce_mean(tf.cast(correct_list, tf.float32))

    def next_batch(self,X, y, start, batch_size):
        num_examples = len(X) # X.shape[0]
        assert batch_size <= num_examples
        end = start + batch_size
        
        if end > num_examples:
            remain = batch_size - (num_examples % batch_size)
            perm = np.arange(num_examples)
            np.random.shuffle(perm)
            X = np.concatenate((X[start:], X[perm[:remain]]), axis=0)
            y = np.concatenate((y[start:],y[perm[:remain]]), axis=0)
            return X, y, 0

        return X[start:end], y[start:end], end


digits = load_digits()
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=0, stratify=digits.target)

parameter = {
    "learning_rate" : 0.01,
    "n_output" : 10,
    "n_epochs" : 400,
    "batch_size" : 5,
    "num_trains" : len(x_train)
}

dense = {
    "nodes"  : [4,4,4],
    "activation" : tf.nn.relu
}

NN.load_model(digits.data,digits.target)

with tf.Session() as session:

# x_train, x_test, y_train, y_test =train_test_split(x,y, train_size = 0.8, random_state = 15)

# scaler = StandardScaler()
# scaled_x_train = scaler.fit_transform(x_train)
# scaled_x_test = scaler.transform(x_test)

# print("평균", " : ", scaler.mean_)
# print("편차", " : ", scaler.var_)