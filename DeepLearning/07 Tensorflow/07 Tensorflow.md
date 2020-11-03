07 Tensorflow
===

## 예제

$3 * 2 +  3 / 2$ 수식을 계산하는 텐서플로우 그래프를 정의하고 그 결과를 출력하라.

# 상수

앞서 constant 이외에도 다양한 상수 생성 연산들을 제공하고 있다. 

```python
tf.zeros([2,3], tf.int32)
# [[0,0,0],[0,0,0]]

input_tensor = tf.constant([[1,2,3],[4,5,6]])
tf.zeros_like(input_tensor)
# [[0,0,0],[0,0,0]]

tf.ones([2,3], tf.int32)

tf.fill([2,3],7)
# [[7,7,7],[7,7,7]]

tf.linspace(10.0,13.0,4)    # min, max, count
# [10.0, 11.0, 12.0, 13.0]

tf.range(start, limit, delta)

tr.range(limit)
# [0, 1, 2, 3, 4, 5]

tf.random_normal()
tf.random_uniform()
tf.random_shuffle()
```

# 연산

## 덧셈

```python
import tensorflow as tf

a = tf.constant([3,6])
b = tf.constant([2,2,2])
c = tf.add(a,b)

with tf.Session() as session:
    x = session.run(c)
    print(x)    #Error. Shape가 동일하지 않음
```

## 곱셈

행렬 곱셈은 matmul(matrix multiply)를 사용

# 자료형

텐서플로우는 문자열, 정수형, 실수형 등 파이썬의 기본 자료형을 지원하지만 텐서플로우에서 제공하는 자료형이 있다.

constant 연산으로 텐서를 생성할때 정수는 tf.int32이며, 실수는 tf.float32가 기본값이다.

> 연산시 자료형이 일치하지 않으면 오류가 발생합니다.

```python
import tensorflow as tf

a = tf.constant([3,6,7,9])  # default tf.int32
b = tf.constant([[2,2],[4,8]], dtype=tf.float32)
c = tf.add(a,b) # Error. 
```

```python
import tensorflow as tf

a = tf.constant([3,6,7,9])  # default tf.int32
b = tf.constant([[2,2],[4,8]], dtype=tf.float32)
a = tf.cast(a, dtype=tf.float32)
a = tf.reshape(a,[2,2])
c = tf.add(a,b) # Error.
```

# 변수

지금 까지는 상수를 생성하는 방법에 배웠습니다. 실행 중에 그 값이 변하는 텐서를 생성하려면 변수가 필요합니다.

```python
import tensorflow as tf

x =tf.Variable(3, name='x')
y = tf.Variable(4, name='y')
f = x^2 * y + 2
```

> 주의. 변수는 선언시 초기값을 가지지 않으며 실행 되기 전에 초기화를 해야합니다.

```python
import tensorflow as tf

x =tf.Variable(3, name='x')
y = tf.Variable(4, name='y')
f = x^2 * y + 2

with tf.Session() as session:
    session.run(x.initializer)
    session.run(y.initializer)
    z = session.run(f)
    print(z)
```

## 여러개의 변수 초기화

여러개의 변수를 한번에 초기화 할 경우에는 tf.variables_initializer를 사용합니다.

```python
init_xy = tf.variable_initializer([x,y], name='init_xy')
with tf.Session() as session:
    session.run(init_xy)
```

모든 변수를 초기화하려면 tf.global_variables_initializer를 사용합니다.

```python
init = tf.globaL_variables_initializer()

with tf.Session() as session:
    session.run(init)
```

## tf.assign

tf.Variable은 assign 과 assign_add, assign_sub로 저장된 값을 업데이트 할 수 있습니다. 이때 assign을 했더라도 실행하지 않으면 적용되지 않습니다. 변수 w에 assign한 결과를 저장하여 실행해야 7로 변경됩니다.

```python
import tensorflow as tf

v = tf.Variable(0)
w = v.assign(7)

with tf.Session() as session:
    v.initializer.run()
    w.eval()
    print(v.eval())
```

## tf.Session

tf.Session 객체는 독립적으로 실행되며, 다른 세션에 영향을 끼치지 않습니다.

```python
import tensorflow as tf

x = tf.Variable(3)
session1 = tf.Session();    session2 = tf.Session()
session1.run(x.initializer)
session2.run(x.initializer)

print(session1.run(x.assign_add(5)))    # 8
print(session2.run(x.assign_sub(1)))    # 2
print(session1.run(x.assign_add(10)))   # 18
print(session2.run(x.assign_sub(5)))    # -3

session1.close()
session2.close()
```

## 예제

1 ~ 5까지의 합을 구하는 예제입니다. 

```python
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
```

## 변수 저장 및 읽기

텐서플로우 그래프는 파일로 저장할 수 있습니다. 학습 데이터를 사용하여 모델을 학습한 후에 그 모델의 가중치 값들을 저장하여 사용할 수 있습니다. 변수 저장은 그래프를 구성하고 tf.train.Saver로 객체를 생성하여 save()로 저장할 수 있습니다.

