import tensorflow as tf

i = tf.Variable(1)
sum = tf.Variable(0)
summing = sum.assign_add(i)
increasing = i.assign_add(1)

init = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(init)

    for i in range(5):
        summing.eval()
        increasing.eval()

    print(sum.eval())