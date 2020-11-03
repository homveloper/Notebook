08 Image Restoration
===

이번 장에서는 노이즈가 심한 영상을 복원하는 방법에 대해 배웁니다. 아래 영상은 solt&pepper noise라고 하며 이를 제거한 영상입니다.

![](image/08%20overview.png)

영상 복원은 영상 획득 과정에서 발생한 영상 저하를 제거하는 것을 의미합니다. 대부분의 영상 복원 방법은 이웃 기반을 사용합니다. 다른 방법으로는 주파수 기반 처리를 수행합니다.

영상 복원의 원리는 간단합니다. 원본 영상 f와 특정 필터 h가 있으며 복원한 영상을 g라고 합니다. f와 h를 곱하여 g를 얻어냅니다.

$$ h(x,y) = f(x,y)*h(x,y)$$

여기서 노이즈 n을 고려한 식은 $h(x,y) = f(x,y)*h(x,y) + n(x,y)$입니다.

기존 공간 도메인(점,기하 기반) 방식에서 convolution 연산의 시간복잡도는 $O(n^4)$입니다. 반면 주파수 도메인 방식은 $O(n^2)$입니다.

# 1. Noise

노이즈는 외부 환경에 의해 영상 신호에 저하를 발생시키는 요인입니다.

## Salt and Pepper Noise

Salt and Pepper Noise는 다른 말로 impluse noise라고 부릅니다. 영상 찰영시 순간적인 빛에 의해 노이즈가 발생한 것을 의미합니다.

![](image/08%20Salt%20and%20Pepper%20noise.png)

## Gaussian Noise

Gaussian Noise는 이상적인 white noise입니다. 영상을 I, Gaussian Nosise를 N이라 했을때 노이즈 영상은 $I + N$ 입니다. 그러므로 밝기 값과 독립적인 노이즈입니다.

```python
im_gaussian = imnoise(image,'gaussian')
```

## Speckle Noise

Speckle Noise는 Gaussian Noise와 반대로 밝기값에 노이즈가 포함된 영상 $I(1+N)$ 입니다. 그림(a)는 Gaussian Noise 영상, (b)는 Speckle Nosize 영상이다.

```python
im_gaussian = imnoise(image,'speckle')
```

![](image/08%20Gaussian%20Noise%20and%20Speckle%20Noise.png)

## Periodic Noise

Periodic Noise는 이름 그대로 주기적인 노이즈를 띄는 것을 말합니다.

```python
height,width = image.size
```

# 2. Cleaning Salt and Pepper Image

## Low-Pass Filtering

Salt and Pepper 영상을 Low-Pass 필터를 통해 복원하는 방법에 대해 알아보겠습니다. 

```python
mask = fspecial('average')
restore_image = filter2(mask,image)
```

만약 아직도 salt and pepper가 보인다면 filter 사이즈를 키워주면 됩니다.

```python
mask = fspecial('average',[7,7])
restore_image = filter2(mask,image)
```

하지만 Low-Pass Filtering으로 Salt and Pepper를 지우면 사진이 뭉개져 버립니다.

![](image/08%20Salt%20and%20Pepper%20image%20restoration%20with%20low-pass%20filtering.png)

## Median Filtering

Median Filtering은 마스크의 중간값을 이용한 방식입니다. 중간값을 알아내려면 정렬이 필요하며 $O(Nlog(N))$ 의 복잡도와 모든 픽셀에 접근해야 하므로 $O(N^2)$ 이 되어, 총 $O(N^3 log(N))$의 시간 복잡도가 됩니다.

![](image/08%20Cleaning%20salt%20and%20pepper%20noise%20with%20a%20median%20filter.png)

```python
restore_image = medfilt2(image)
```

아래 그림은 인위적으로 salt and pepper를 넣어 복원한 그림입니다.

![](image/08%20after%20median%20filtering.png)

## Rank-Order Filtering

Median Filtering은 정렬과 픽셀 접근으로 인해 시간복잡도가 $O(N^2 log(N))$인 문제점이 있었습니다. Rank-Order Filtering은 정렬을 하지 않고 마스크의 중간 지점만 알아내어 적용하는 방식입니다.

![](image/08%20Rank-Order%20Filtering.png)

## Outlier Method

기존 Median Filtering은 속도가 느립니다. Outlier Method는 정렬 과정이 없으므로 $O(N^2)$의 시간 복잡도를 가집니다.

1. Threshold 값 D를 정합니다.
2. 영상의 픽셀 중 하나 p와 그 이웃한 8개 픽셀의 평균인 m이 있습니다.
3. $if |p-m| > D\; then\; pixel\; p\; is\; noise$
4. 픽셀 p가 노이즈라면 p의 값을 m으로 변경하며 그렇지 않다면 변하지 않습니다.

마스크를 이용하여 평균 m을 구할 수 있을까요? 마스크의 중앙 값을 제외한 평균이므로 다음과 같이 지정하면 됩니다.

| 0.125 | 0.125 | 0.125 |
| :---: | :---: | :---: |
| 0.125 |   0   | 0.125 |
| 0.125 | 0.125 | 0.125 |

아래 영상들은 treshold에 따른 노이즈가 제거된 영상입니다.

![](image/08%20Appling%20Outlier%20Method.png)

# 3. Cleaning Gaussian Noise

## Image Averaging

Gaussian Noise가 있는 영상 하나를 100개의 영상과 노이즈로 복사합니다.

$$
M^` = \frac{1}{100} \displaystyle\sum_{i=1}^{100} (M+N_i)   \\

    = \frac{1}{100} \displaystyle\sum_{i=1}^{100} M + \frac{1}{100} \displaystyle\sum_{i=1}^{100} N_i   \\

    = M + \displaystyle\sum_{i=1}^{100} N_i \\
$$

## Adaptive Filtering

마스크 아래에 있는 픽셀들의 grayscale 값의 특징을 파악하여 다양한 filter를 적용하는 방식입니다.

### Minimum mean-square error filter

$m_f + \frac{{\sigma_f}^2}{{\sigma_f}^2 + {\sigma_g}^2} (g-m_f)$

### Wiener filter

$m_f + \frac{ max(0, {\sigma_f}^2 - n) }{max({\sigma_f}^2, n)} (g-m_f)$

# 4. Cleaning Periodic Noise

주기적인 노이즈가 있는 영상을 Fast Fourier Transform을 통해서 주파수 형태로 변환합니다. 흰 점이 있는 부분이 저주파가 있는 곳입니다.

## Band Reject Filtering

주파수 형태로 변환된 영상에서 흰 점 부분을 다 0으로 변환하여 노이즈를 제거합니다.

![](image/08%20Band%20Reject%20Filtering.png)

## Notch Filtering

![](image/08%20Notch%20Filtering.png)

## Inverse Filtering

![](image/08%20Inverse%20Filtering.png)

# 4. Motion Deblurring

카메라로 영상을 찍는 동안 CCD에 감지되는 빛이 흔들리면서 다른 빛이 들어옵니다. 그러면 블러링이 발생하게 됩니다.

![](image/08%20Motion%20Blur.png)

블러를 제거하기 위해서는 주파수 도메인으로 

## Wiener Filtering