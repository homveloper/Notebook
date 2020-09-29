07 Image Segmentation.md
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

배
    고

        
    프

    다

        
고
    배

        
    프

    다

        
프
    배

    고

    다

다
    배

    고

    프


# 2. Edge Detection