import tensorflow as tf

x = tf.constant(2,name='x')
y = tf.constant(3,name='y')
# z = tf.add(x,y,name='addition')
z = x+2;
# w = tf.multiply(x,z,name='multiply')
w = x * z;

with tf.Session() as session:
    # run = session.run(w)
    # print(run)

    # print(w.eval())
    # print(y.eval())

    w_eval,y_eval = session.run([w,y])


# graph 형태 확인
# for node in tf.get_default_graph().get_operations():
#     print(str(node))