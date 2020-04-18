02 CSS 기초
===

CSS(Cascading Style Sheet)

# 1. 스타일

## 1.1 스타일 형식

선택자 { 속성 : 값}

## 1.2 주석

1. /*  */

---

# 2. 스타일 시트

## 2.1. 내부 스타일 시트

## 2.2. 외부 스타일 시트

## 2.3. 인라인 스타일 시트

~~~
<ul style="color:blue; list-style:square;">
    <li>시드니</li>
    <li>서울</li>
    <li>베이징</li>
</ul>
~~~

<ul style="color:blue; list-style:square;">
    <li>시드니</li>
    <li>서울</li>
    <li>베이징</li>
</ul>

# 3. 선택자

## 3.1. 전체 선택자

## 3.2. 태그 선택자

## 3.3. 클래스와 id 선택자

1. 클래스 선택자

```
.클래스명 {
    속성 : 값;
}
```

2. id 선택자

```
#아이디명 {
    속성 : 값;
}
```

## 3.4. 그룹 선택자

```
태그명1, 태그명2 {
    속성 : 값;
}
```

## 3.5 연결 선택자

요소 간의 관계성을 이용하여 특정 요소를 선택

1. 자식선택자
   부모 요소의 바로 하위 요소 하나에만 스타일을 적용

    ```CSS
    
    parent > h1 { color : blue;}

    ```

2. 하위 선택자

    부모 요소에 포함된 모든 하위 요소에 스타일을 적용

    다음은 parent 태그 아래 모든 div 태그의 요소의 색을 파란색으로 지정하는 것이다.

    ```CSS
    parent p { color : blue;}

    <style>
        #container ul{
            border : 1px dotted blue;
        }
    </style>

    <div id="container">
    <header><h1>예약 방법 및 요금</h1></header>

    <p> 요안도라에 예약하려면?
    <ul>
        <li> 예야강법
            <ul>
                <li>직접 통화</li>
                <li>문자남기기</li>
            </ul>
        </li>
        <li>요금
            <ul>
                <li>1인 : 40,000원</li>
                <li>2인 : 60,000원</li>
            </ul>
        </li>
    </ul>
    </p>
    </div>
    ```

3. 인접 형제 선택자

    같은 부모를 가진 형제 요소 중 첫 번째 동생 요소에만 스타일을 적용

    ```CSS
    h1 + p { text-decoration : underline;}
    ```

4. 형제 선택자

    ```CSS
    h1 ~ p { text ~~}
    ```

5. 속성 선택자
    
    a태그에 href속성을 가진 태그에 대해 배경색을 노랑으로 적용

    ```CSS
    a[href] {backgroud : yellow;}   
    ```

6. 속성 값 선택자

    주어진 속성과 속성 값이 일치하는 요소에 스타일을 적용

    ```CSS
    a[target="_blank"] { padding-right : 30px;}
    ```

# 4. cascade

cascading이란 "위에서 아래로 흐른다"를 의미한다.이는 하나의 요소에 여러 스타일을 명시 했을 때 어떤 것을 따라야 하는가?에 대한 명확한 기준이 필요하다. cascading에는 2가지 원칙이 있다.

## 4.1. 스타일 충돌

```
<html>
<head>
    <style>
        h1 { color : blue;}
        #habor { color: green;}
        .cascade { color : red;}
    </style>
</head>
<body>
    <h1 class="cascade" id="habor">Hello world</h1>
</body>
</html>
```
<html>
<head>
    <style>
        h1 { color : blue;}
        #habor { color: green;}
        .cascade { color : red;}
    </style>
</head>
<body>
    <h1 id="habor" class="cascade">Hello world</h1>
</body>
</html>

## 4.2. 스타일 우선순위

## 4.3. 스타일 상속

# 5. 가상클래스

가상클래스()는 html 문서에 코드로 명시되어 있지 않지만 사용자 동작에 반응하는 것을 말한다.

## 5.1 구조 가상 클래스

- nth-child(n) : n번째 요소에 대해 스타일을 적용

## 5.2 가상 요소

특정 태그의 위치에 요소를 넣는 것

- ::first-line : 특정 요소의 첫 번째 줄에 스타일 적용
- ::first-letter : 특정 요소의 첫 번째 글자에 스타일 적용
- ::before : 특정 요소 앞에 지정한 내용을 추가
- ::after : 특정 요소 뒤에 지정한 내용을 추가
