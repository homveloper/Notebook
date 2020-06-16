06 DOM
===
- [06 DOM](#06-dom)
- [1. DOM](#1-dom)
- [2. 대상 선택하기](#2-대상-선택하기)
- [3. Document 객체](#3-document-객체)
- [4. 요소 가져오기](#4-요소-가져오기)
  - [단점](#단점)
  - [해결법](#해결법)
- [5. 요소 조작하기](#5-요소-조작하기)

# 1. DOM

DOM(Document Object Model)은 XML이나 HTML과 같은 문서(Document)를 트리구조로 표현하며 각 노드를 객체(Object)로 하여 자바스크립트로 제어하기 위한 객체 모델이다.

즉, DOM은 JavaScript와 웹페이지 사이의 인터페이스이다. 웹페이지가 load되면 브라우저는 웹페이지의 DOM을 생성한다. 

# 2. 대상 선택하기

HTML문서네 객체는 Get 메서드를 이용하여 제어할 수 있다. CSS 선택자에서 ID를 사용할시에는 ID가 중복되어도 오류가 나타나지 않으므로 ID의 유일성 검사를 해야한다.

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

Document 객체는 HTML 태그들 중 최상위 노드입니다. windows 객체 아래에 있으므로 window.document로 접근해야 하지만, 'window.'은 암묵적으로 생략이 가능하다. window는 전역 변수로 창 그 자체를 의미한다.

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

# 4. 요소 가져오기

1. getElementsByTagName()

```javascript
<p>unordered list</p>

<ul>
    <li>coffee</li>
    <li>tea</li>
    <li>milk</li>
</ul>

<button onclick="myFunction()">Try it</button>
<p id="demo"></p>

<script>
    function myFunction(){
        var x = document.getElementsByTagName("li");
        document.getElementById("demo").innerHTML = x[1].innerHTML;

        for(var i in [...x]){
            x[i].style.color = 'green';
        }
    }
</script>
```

2. getElementsByName()

```javascript
First Name : <input name="fname" type="text" value="범휘"><br>
Last Name : <input name="fname" type="text" value="최">

<p>click the button</p>

<button onclick="myFunction()">Try it</button>

<p id="demo"></p>

<script>
    function myFunction(){
        var x = document.getElementsByName("fname")[0].tagName;
        document.getElementById("demo").innerHTML = x;
    }
</script>
```

3. getElementById()

```javascript

<p id="demo">Click the button to change the text in this paragraph.</p>

<button onclick="myFunction()">Try it</button>

<script>
    function myFunction(){
        document.getElementById("demo").innerHTML = "hello world";
    }
</script>
```

4. querySelector()

## 단점

CSS 선택자를 사용할 순 있지만, 가상 클래스"(nth-child(n))"를 사용하는 것이 번거롭다.

## 해결법

대신 firstElement, lastElement, nextElementSibling으로 해당 기능을 대신할 수 있다.

```javascript
<h2 class="example">A heading</h2>
<p class="example">A paragraph</p>

<ul id="myList">
  <li>coffee</li>
  <li>tea</li>
</ul>

<p>Click the button to change the text in this paragraph.</p>

<button onclick="myFunction()">Try it</button>
<button onclick="myFunction2()">Try it2</button>

<p id="demo"></p>

<script>
    function myFunction(){
        document.querySelector(".example").style.backgroundColor = "red";
    }

    function myFunction2(){
      var list = document.getElementById("myList").firstElementChild.innerHTML;
      document.getElementById("demo").innerHTML = list;
      var list = document.getElementById("myList").lastElementChild.innerHTML;
      document.getElementById("demo").innerHTML = list;
    }
</script>
```

# 5. 요소 조작하기

- 속성 가져오기

  ```javascript
  <div id="myDiv" class="bd" title="Body text" lang="en" dir="Itr"></div>

  <script>
    var div = document.getElementById('myDiv');
    console.log(1, div.id);

    // class가 아닌 className이라는점 주의하세요.
    console.log(2, div.className);
    console.log(3, div.title);
    console.log(4, div.lang);
    console.log(5, div.dir);

    console.log(1, div.getAttribut('id'));
    console.log(2, div.getAttribut('class'))
    console.log(3, div.getAttribut('title'))
    console.log(4, div.getAttribut('lang'))
    console.log(5, div.getAttribut('dir'))
  </script>
  ```

- 속성 설정하기(CSS 조작)

  1. property를 직접 수정하는 방법

    style 관련 네이밍은 카멜표기법을 따릅니다. (ex. fontSize, textAlign)

    ```javascript
    <script>
        var button = document.getElementById('button');
        var anchor = document.getElementById('anchor');
        var para = document.getElementById('para');

        button.title = 'inputBtn';

        //  javascript 적용이 안된다.
        button.onclick = "alert('hello world')";

        anchor.href = 'http://se.kumoh.ac.kr';
        para.style.fontSize = '32px';
        para.style.textAlign = 'right';
    </script>
    ```

  2. setter 이용 

    모두 소문자를 이용하며, 하이픈(-)으로 구분합니다.
  
    ```javascript
    <script>
      var button = document.getElementById('button');
      var anchor = document.getElementById('anchor');
      var para = document.getElementById('para');

      anchor.setAttribute('href','http://se.kumoh.ac.kr');
      para.setAttribute('style','font-size:48px; text-align:center; border:1px solid blue');
    </script>
    ```

  3. class 속성 다루기

    - classList.add(class) : 클래스 추가
    - classList.contains(class) : 클래스가 있는지 검사
    - classList.item(index) : 클래스 반환
    - classList.remove(class) : 클래스 제거
    - classList.toggle(class) : 클래스가 없으면 추가, 있으면 제거

    ```javascript
    <script>
      var button = document.getElementById('button');
      var anchor = document.getElementById('anchor');
      var para = document.getElementById('para');

      // <div class="first">
      button.classList.add('first');

      // <div class="first second">
      button.classList.add('second');

      // second
      button.classList.item(1);
    </script>
    ```
- 요소 추가/삭제/교체

  appendchild()
  remove()
  replaceChild()

  ```html
    <h2> 축제하면 가장 먼저 생각나는 것 h2>
    <ol>
        <li class="festival">주점</li>
        <li class="festival">이벤트</li>
        <li class="festival">게임</li>
        <li class="festival">공연</li>
    </ol>

    <script>
        var li = document.createElement('li');
        var content = document.createTextNode('휴강');

        li.appendChild(content);
        // insertBefore(추가할 요소, 기준 요소)
        root.insertBefore(li, root.firstElementChild.nextElementSibling);

        var jujum = document.getElementByTagName('li')[0];
        jujum.remove()


        var newLi = document.createElement('li');
        newLi.textContent ='체육대회'
        root.replaceChild(newLi, root.lastElementChild);
    </script>
  ```
