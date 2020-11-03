10 Mathematical Morphology
===

Morphology는 영상에서 형태를 분석하는데 매우 유용합니다. 보통 이진 영상(0,1)을 기준으로 개발되었으며, 여기서는 회색조 영상으로 적용하는 방법에 대해 배워보겠습니다.

# 1. 기초

## Translation(이동)

$A_w = \{(a,b) + (x,y) : (a,b) \in A\}$

## Relection(반사)

$\hat{A} = \{(-x, -y) : (x, y) \in A\}$

## Dilation(팽창)

$A \oplus B = \cup_{x \in B} A_x$

A는 이진 영상, B는 마스크입니다. 특정 threshold D 이상을 1, 미만을 0으로 적용하면 A 영상을 얻어낼 수 있습니다. 여기서 회색 영역으 원래 A 영상이며, 화색 영역 밖은 새롭게 추가된 밝기값입니다. B에서 빨간 점은 새롭게 추가할 밝기값입니다. 

![](image/10%20Dilation.png)


## Erosion(침식)

$A \ominus B = \{ w:B_w \subseteq A \}$

A는 이진 영상, B는 마스크입니다. B에 모두 포함된 영역에 대해서만 중앙 점만 남아있게 되며, 나머지는 사라집니다.

![](image/08%20Erosion%20A.png)

![](image/08%20Erosion.png)

Erosion을 활용하며 영상에 부분적으로 있는 노이즈를 제거할 수 있습니다.

![](image/08%20Erosion%20of%20a%20binary%20image.png)

# 2. Dilation과 Erosion 활용

팽창과 침식을 이용하면 이미지의 경계선을 알아낼 수 있습니다.

- $A - (A \ominus B) : interal boundary$
- $(A \oplus B) - A : external boundary$
- $(A \oplus B) - (A \ominus B) : morphological gradient$

![interal](image/10%20Morphological%20edge%20detection.png)
![alt](image/10%20Morphological%20edge%20detection2.png)

# 3. Opening & Closing

## Opening

$A \circ B = (A \ominus B) \oplus B$

![alt](image/10%20Opening.png)

## Closing

$A \bullet B = (A \oplus B) \ominus B$

![alt](image/10%20Closing.png)

## 노이즈 제거

Opening과 Closing을 이용하여 Salt&Peppers 노이즈를 제거할 수 있습니다. a는 원본 영상이며, b는 4방향에 이웃한 지점에 대한 연산이며, c는 8방향에 이웃한 지점에 대한 연산의 결과입니다.

![alt](image/10%20A%20nosiy%20binary%20image%20and%20results%20after%20morphological%20filtering%20with%20different%20structuring%20elements.png)

# 4. 그외 Morphology 알고리즘

## Skeletonization

영상에서 도형의 뼈대만 남기는 방법이다. 즉, 영상에서 어떤 형체를 선으로 표현한다.

![alt](image/10%20Skeletonization%20of%20a%20binary%20image.png)

## GrayScale

