import pandas as pd
from sklearn.datasets import load_iris
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

n_inputs = 4 
n_hidden1 = 10
n_hidden2 = 5
n_outputs = 3

inputs = tf.placeholder(tf.float32, shape=(None, n_inputs), name="inputs") 
targets = tf.placeholder(tf.int64, shape=(None), name="targets")
one_hot_ecoded_targets = tf.one_hot(targets, n_outputs)

hidden1 = tf.layers.dense(inputs, n_hidden1, activation=tf.nn.relu, name="hidden1")
hidden2 = tf.layers.dense(hidden1, n_hidden2, activation=tf.nn.relu, name="hidden2")

outputs = tf.layers.dense (hidden2, n_outputs, name="outputs")

loss = tf.nn.softmax_cross_entropy_with_logits_v2(labels=one_hot_ecoded_targets, logits=outputs)
total_loss = tf.reduce_mean(loss, name="total_loss")

learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
training_op = optimizer.minimize(total_loss)

correct_list = tf.nn.in_top_k(outputs, targets, 1)

accuracy = tf.reduce_mean(tf.cast(correct_list, tf.float32))

init = tf.global_variables_initializer()
saver = tf.train.Saver()

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=0, stratify=iris.target)

n_epochs = 400; batch_size = 5; num_trains = len(x_train)

def next_batch(X, y, start, batch_size):
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

with tf.Session() as sess:
    init.run()

    for epoch in range(n_epochs):
        start = 0

        for iteration in range(num_trains // batch_size):
            batch_x, batch_y, start = next_batch(x_train, y_train, start, batch_size)

            sess.run(
                training_op,
                feed_dict = {inputs: batch_x,
                            targets: batch_y})

            acc_train = accuracy.eval(
                feed_dict= {inputs: x_train,
                            targets: y_train})

            acc_test = accuracy.eval(
                feed_dict= {inputs: x_test,
                           targets: y_test})

        print(epoch, "Train accuracy:", acc_train, "Test accuracy:", acc_test)

    save_path = saver.save(sess, "./my_model_final.ckpt")
