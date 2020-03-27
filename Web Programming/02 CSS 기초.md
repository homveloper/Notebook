02 CSS 기초
===

CSS(Cascading Style Sheet)

## 1. 스타일

### 1.1 스타일 형식

선택자 { 속성 : 값}

### 1.2 주석

1. /*  */

---

## 2. 스타일 시트

### 2.1. 내부 스타일 시트

### 2.2. 외부 스타일 시트

### 2.3. 인라인 스타일 시트

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

## 3. 선택자

### 3.1. 전체 선택자

### 3.2. 태그 선택자

### 3.3. 클래스와 id 선택자

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

### 3.4. 그룹 선택자

```
태그명1, 태그명2 {
    속성 : 값;
}
```

## 4. cascade

cascading이란 "위에서 아래로 흐른다"를 의미한다.이는 하나의 요소에 여러 스타일을 명시 했을 때 어떤 것을 따라야 하는가?에 대한 명확한 기준이 필요하다. cascading에는 2가지 원칙이 있다.

### 4.1. 스타일 충돌

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

### 4.2. 스타일 우선순위

### 4.3. 스타일 상속


