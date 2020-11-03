import pandas as pd
from sklearn.datasets import load_digits
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

digits = load_digits()

x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=30, stratify=digits.target)

parameter = {
    "n_inputs" : digits.data.shape[1],
    "n_outputs" : len(np.unique(digits.target)),
    "n_epochs" : 100,
    "batch_size" : 20,
    "num_trains" : len(x_train),
    "learning_rate" : 0.01
}

dense = {
    "nodes" : [4,8],
    "activation" : tf.nn.relu
}

inputs = tf.placeholder(tf.float32, shape=(None, parameter["n_inputs"]), name="inputs") 
targets = tf.placeholder(tf.int64, shape=(None), name="targets")
one_hot_ecoded_targets = tf.one_hot(targets, parameter["n_outputs"])

hiddens = []
for i,d in enumerate(dense["nodes"]):

    hiddens.append(tf.layers.dense( hiddens[i-1] if i > 0 else inputs ,d, activation=dense["activation"], name=f"dense{i}"))

outputs = tf.layers.dense (hiddens[-1], parameter["n_outputs"], name="outputs")

loss = tf.nn.softmax_cross_entropy_with_logits_v2(labels=one_hot_ecoded_targets, logits=outputs)
total_loss = tf.reduce_mean(loss, name="total_loss")

optimizer = tf.train.GradientDescentOptimizer(parameter["learning_rate"])
training_op = optimizer.minimize(total_loss)

correct_list = tf.nn.in_top_k(outputs, targets, 1)

accuracy = tf.reduce_mean(tf.cast(correct_list, tf.float32))

acc_train_summary = tf.summary.scalar("train_acc",accuracy)
acc_test_summary = tf.summary.scalar("test_acc",accuracy)
total_loss_summary = tf.summary.scalar("total_loss",total_loss)

init = tf.global_variables_initializer()
saver = tf.train.Saver()

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

    with tf.summary.FileWriter(r"DeepLearning\과제\graphs",sess.graph, max_queue=1) as writer:

        init.run()

        for epoch in range(parameter["n_epochs"]):
            start = 0

            for iteration in range(parameter["num_trains"] // parameter["batch_size"]):
                batch_x, batch_y, start = next_batch(x_train, y_train, start, parameter["batch_size"])

                loss_summary,_ = sess.run(
                    [total_loss_summary, training_op],
                    feed_dict = {inputs: batch_x,
                                targets: batch_y})

                acc_train, train_sumarry = sess.run(
                                [accuracy,acc_train_summary],
                                feed_dict= {inputs: x_train,
                                            targets: y_train}
                            )

                acc_test, test_summary = sess.run(
                                [accuracy,acc_test_summary],
                                feed_dict= {inputs: x_test,
                                            targets: y_test}
                            )

                writer.add_summary(loss_summary,epoch)
                writer.add_summary(train_sumarry,epoch)
                writer.add_summary(test_summary,epoch)

            print(epoch, "Train accuracy:", acc_train, "Test accuracy:", acc_test)

        save_path = saver.save(sess, "./my_model_final.ckpt")
