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

## Speckle Noise

Speckle Noise는 Gaussian Noise와 반대로 밝기값에 노이즈가 포함된 영상 $I(1+N)$ 입니다. 그림(a)는 Gaussian Noise 영상, (b)는 Speckle Nosize 영상이다.

![](image/08%20Gaussian%20Noise%20and%20Speckle%20Noise.png)

## Periodic Noise

Periodic Noise는 이름 그대로 주기적인 노이즈를 띄는 것을 말합니다.