import tensorflow as tf

_1 = tf.zeros([2,3], tf.int32)
print(_1)
# [[0,0,0],[0,0,0]]

input_tensor = tf.constant([[1,2,3],[4,5,6]])
_2 = tf.zeros_like(input_tensor)
print(_2)
# [[0,0,0],[0,0,0]]


_3 = tf.ones([2,3], tf.int32)
print(_3)

_4 = tf.fill([2,3],7)
print(_4)
# [[7,7,7],[7,7,7]]

_5 = tf.linspace(10.0,13.0,4)    # min, max, count
print(_5)
# [10.0, 11.0, 12.0, 13.0]

start, limit, delta = (1,10,2) 
_6 = tf.range(start, limit, delta)
print(_6)

_7 = tf.range(limit)
print(_7)
# [0, 1, 2, 3, 4, 5]

# tf.random_normal()
# tf.random_uniform()
# tf.random_shuffle()