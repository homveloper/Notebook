07 Image Segmentation
===

분할(segmentation)은 이미지를 구성 요소 부분 또는 별도의 개체로 분할하는 작업을 말한다. 이 장에서는 임계값(threshold) 지정과 에지(edge detection) 감지라는 두 가지 매우 중요한 개념을 배운다.

# 1. Thresholding

$A \ pixel \ becomes \begin{cases} white & gray\ level\ is > T, \\ black & gray\ level\ is \le T. \end{cases}$

두 분포의 히스토그램에서 교차점을 찾는 방법은 다음과 같다. 두 히스토그램 $w(k),\ u(k)$가 있다. $p_i$는 확률이다.

- $\omega(k) = \displaystyle \sum_{i=0}^k p_i$
- $\mu(k) = \displaystyle \sum_{i=k+1}^{L-1} p_i$

두 히스토그램을 더한 결과는 항상 1이 된다.

- $\omega(k)+\mu(k) = \displaystyle \sum_{i=0}^{L-1} p_i=1$


## Adaptive Threshold

영상이 밝기값에 따라 구분감이 없을 경우에는 

# 2. Edge Detection

우리는 영상의 밝기값이 급변하는 부분을 경계선이 있다고 느낍니다.  

![alt](image/07%20Block%20of%20pixels.png)

하지만 아래 그림 처럼 Ramp 영상의 경계를 어떻게 식별해야 할까요? step edge에서는 두 경계면 사이의 밝기 차이를 가지고 계산합니다. 

![alt](image/07%20edge%20and%20their%20profiles.png)

![](image/07%20the%20derivative%20of%20the%20edge%20profiles.png)

두 점의 밝기 값 차이는 $f(x+1,y)-f(x,y)$입니다. 하지만 모든 점에 대해 일일이 다 하는 것 보다는 convolution 연산을 통해 경계를 찾아낼 수 있습니다. Prewitt이 제안한 다음 필터는 가로와 세로에 대해서 경계선을 추출하며 경계선을 두드러지게 나타냅니다.

$P_x = \quad \begin{bmatrix}
    -1 & 0 & 1 \\
    -1 & 0 & 1 \\
    -1 & 0 & 1
\end{bmatrix} \; P_x = \quad \begin{bmatrix}
    -1 & -1 & -1 \\
    0 & 0 & 0 \\
    1 &1 &1
\end{bmatrix}$

여기서 Sobel이 가로와 세로 방향에 대한 경계를 모두 추출하기 위한 방법을 고안했다.

$\quad \begin{bmatrix}
    -1 & 0 & 1 \\
    -2 & 0 & 2 \\
    -1 & 0 & 1
\end{bmatrix} \; and \quad \begin{bmatrix}
    -1 & -2 & -1 \\
    0 & 0 & 0 \\
    1 &2 &1
\end{bmatrix}$

---

지금 까지는 step edge에 대한 경계 추출을 보았는데 ramp edge에 대해서는 어떻게 할까요?

ramp edge에 대해서 1차 미분을 수행합니다. 두 점 사이의 밝기값의 차이를 저장합니다. 

$$f(x+1,y)-f(x,y)$$

나온 결과에 다시 1차 미분을 수행합니다. 1차 미분을 두번 수행했으므로 2차 미분이라고 합니다. 

$$f(x+1,y)-f(x,y)$$

그다음 절대 값을 취하면 ramp edge에 대한 경계를 찾아낼 수 있습니다.

![](image/07%20second%20derivatives%20of%20an%20edge%20function.png)

ramp edge 또한 convolution을 이용하여 할 수 있습니다. 대표적인 것인 Laplacian 필터입니다. Laplacian은 2차 미분을 수행합니다.

$$\begin{bmatrix}
    0 & 1 & 0 \\   
    1 & -4 & 1 \\
    0 & 1 & 0    
\end{bmatrix}$$

Laplacian은 Isotropic filter라고도 하며, 노이즈에 매우 민감합니다.

![](image/07%20laplacian.png)

2차 미분의 결과는 교차점에서 밝기 값이 반대로 있으므로 흐릿하게 보입니다. 여기서 절대 값을 취할려면 교차점을 찾아내야 합니다. 

## Zero Crossing

교차점을 찾아내는 방식을 Zero Crossing이라고 합니다. 즉 원점을 통과하는 지점, 부호가 변하는 지점을 찾아내는 것 입니다.

아래 그림은 step edge와 ramp edge에 대해 2차 미분을 수행한 결과입니다.

![](image/07%20Edges%20and%20second%20difference.png)

하지만 Laplacian은 노이즈에 대해 민감합니다. 그래서 Marr-Hildreth은 다음과 같은 방법을 제안했습니다.

1. Gaussian filter를 통해 영상을 부드럽게 합니다.
2. Laplacian filter를 통해 경계선을 추출합니다.
3. Zero crossing을 찾아냅니다.

> 1,2를 모두 적용한 Laplacian of Gaussian filter도 존재합니다.
>
> $$ \begin{bmatrix}
0&1&1&2&2&2&1&1&0 \\    
1&2&4&5&5&5&4&2&1 \\
1&4&5&3&0&3&5&4&1 \\
2&5&3&-12&-24&-12&3&5&2 \\
2&5&0&-24&-40&-24&0&5&2 \\
2&5&3&-12&-24&-12&3&5&2 \\
1&4&5&3&0&3&5&4&1 \\    
1&2&4&5&5&5&4&2&1 \\
0&1&1&2&2&2&1&1&0 \\
\end{bmatrix}$$

## Hough Transform

일반적인 직선의 방정식은 $y=ax+b$입니다. 그리고 그 그래프는 아래와 같습니다. 직선의 방정식을 b에 대해 정리하면 $b=ax-y$가 되며 점(1,1)에 대한 선이 나타납니다.

![alt](image/07%20A%20point%20in%20%20an%20image%20and%20its%20corresponding%20line%20in%20the%20transform.png)

만약 기울기가 90도라면 a가 무한대가 됩니다. 그렇다면 다른 방법으로 어떤 선이든 직선과 원점 사이의 수직인 거리 r과 그 수직인 직선과 x축과의 각도 $\theta$로 표현이 가능합니다.

![](image/07%20Line%20and%20its%20parameters.png)

### 곡선

지금 까지는 직선 성분에 대한 경계선을 추출하였는데 곡선이나 원은 어떻게 찾을까요? hough transform을 응용한 circular hough transform을 이용합니다.

일반적인 원의 방정식은 $(x-a)^2 + (y-b)^2 = r^2$ 입니다. 이를 a와 b에 대해서 나타내면 $(a-x)^2 + (b-y)^2 = r^2$입니다.

이를 그래프로 나타내면 원뿔 형태로 나타납니다. 하지만 이 방식은 (a,b,r)을 찾아내는 3차원 방식이므로 연산이 많습니다.

