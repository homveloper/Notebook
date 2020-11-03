06 Image Geometry
===

# 1. Interploation

## NN(Nearest Neighborhood)

NN은 최근접 이웃으로 $x^`_2$는 가장 가까운 $x^`_1$의 값을 가진다.

- 장점 : 최근접한 값으로 치환하므로 Linear에 비해 빠르다.

- 단점 : 데이터 손실이 있으므로 화질이 안좋다.

## Linear

두 점을 함수화하여 $x^`_2$와 $x^`_3$에 채워넣는 방식이다. 두 점 $x_1 \; x_2$의 밝기값은 각각 $f(x_1) \; f(x_2)$이다. 그리고 중간의 임의의 점 F에 대해서 기울기를 구하면 다음과 같은 같다.

${F-f(x_1) \over \lambda}={f(x_2)-f(x_1) \over 1}$

$F = \lambda f(x_2) + (1 - \lambda) f(x_1)$


- 장점 : 두 점 사이의 연속적인 값으로 채워 넣으므로 NN에 비해 화질이 좋다.

- 단점 : 함수화한 값을 각 지점에 비례하여 적용하므로 연산이 많다.


다음 그림은 2차원 평면에서 보간을 하는 과정이다. 사각형의 각 꼭짓점의 좌표에서 검은 점의 값을 보정한다.

![](image/06%20Interpolation%20between%20four%20image%20points.png)

- $f(x,y^`) = \mu f(x,y+1) + (1 - \mu)f(x,y)$
- $f(x+1,y^`) = \mu f(x+1,y+1) + (1 - \mu)f(x+1,y)$
- $f(x^`,y^`) = \lambda f(x+1,y^`) + (1-\lambda) f(x,y^`)$

좀 더 응용해보겠습니다. 앞서 사각형의 각 꼭짓점에 값이 주어져 있다면 $f(x^`,y^`)$의 밝기값은 어떻게 될까요?

---

## General Interpolation

일반적인 보간 방법은 다음 수식을 따릅니다. R은 보간을 위한 특정 함수이며, 임의로 정의할 수 있습니다.

- $f(x^`) = R(-\lambda)f(x_1) + R(1-\lambda)f(x_2$

cubic interpolation
  
# 2. Rotation

회전을 하면 기존 이미지의 특정 좌표가 틀어지게 된다. 즉, 이미지 회전에도 보간이 필요하다. 