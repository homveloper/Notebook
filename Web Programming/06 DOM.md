06 DOM
===
- [06 DOM](#06-dom)
- [1. DOM](#1-dom)
- [2. 대상 선택하기](#2-%eb%8c%80%ec%83%81-%ec%84%a0%ed%83%9d%ed%95%98%ea%b8%b0)
- [3. Document 객체](#3-document-%ea%b0%9d%ec%b2%b4)

# 1. DOM

DOM(Document Object Model)은 XML이나 HTML과 같은 문서(Document)를 트리구조로 표현하며 각 노드를 객체(Object)로 하여 자바스크립트로 제어하기 위한 객체 모델이다.

즉, DOM은 JavaScript와 웹페이지 사이의 인터페이스이다.

# 2. 대상 선택하기

HTML문서네 객체는 Get 메서드를 이용하여 제어할 수 있다.

```JavaScript

// 태그명을 통해 모든 요소 선택
document.getElementsByTagName

// 클래스명을 통해 모든 요소 선택
document.getElementByClassName

// 아이디명을 통해 요소 선택
document.getElementById

// CSS 선택자를 이용해 가장 처음 나오는 요소 하나를 선택
document.querySelector

// CSS 선택자를 이용해 모든 요소 선택
document.querySelectorAll
```

# 3. Document 객체

![alt](img/DOM구조.png)

Document 객체는 HTML 태그들 중 최상위 노드입니다.

```HTML
<!DOCTYPE html>
<html>
<body>

<p>An unordered list:</p>
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>

<p>Click the button to display the innerHTML of the second li element (index 1).</p>

<button onclick="myFunction()">Try it</button>

<p id="demo"></p>

<script>
function myFunction() {
  var x = document.getElementsByTagName("LI");
  document.getElementById("demo").innerHTML = x[1].innerHTML;
}
</script>

</body>
</html>
```

