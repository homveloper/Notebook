03 CSS 텍스트와 배경꾸미기
===

# 1. 텍스트 꾸미기

## 1.1 font-family 속성

웹 문서에서 사용할 글꼴을 지정합니다. 글꼴이 없는 경우를 대비해 여러 개의 글꼴을 지정할 수 있습니다. font-family 속성은 상속이 됩니다. 다음 body 태그에 스타일을 적용하면 문서 전체에 적용 됩니다.

```CSS
body { font-family :"맑은 고딕", 돋움, 굴림}
```

font-family는 web font가 있습니다. font를 web에서 다운받아서 표현하는 방식입니다. 구글에서 web font를 지원하고 있습니다.

```CSS
<style>
    @import
    url(http://fonts.googleapis.com/earlyaccess/nanumgothic.css);
    /* 구글 웹 폰트 */
    .ng-font {
    font-family:'Nanum Gothic', 돋움;
    }
    p {
    font-size:30px; /* 글자 크기 */
    }
</style>
<body>
    <p>브라우저 기본 글꼴 사용</p>
    <p class="ng-font">나눔고딕 웹 폰트 </p>
</body>

```

## 1.2 font-style 속성

tag로도 font-style를 적용할 수 있지만 유지보수를 용이하게 하기 위해서는 CSS를 이용하는게 바람직합니다.

- normal : 일반적인 형태
- italic : 이텔릭체
- oblique : d텔릭체

```CSS
<style>
    p {font-style:italic;}
    p#txt {font-style:normal;}
</style>
<h1>세계 3대 미항</h1>
<p>시드니(Sydney), 호주</p>
<p>리우데자네이루(Rio de Janeiro), 브라질</p>
<p id="txt">나폴리(Naples), 이탈리아</p>
```

## 1.2 font-variant 속성

소문자를 작은 대문자로 바꿉니다.

```CSS
<style>
    .accent {
    font-variant:small-caps; /* 작은 대문자 */
    font-weight:bold; /* 굵게 */
    }
</style>

<h1>세계 3대 미항</h1>
<p><span class="accent">시드니(Sydney)</span>, 호주</p>
<p><span class="accent">리우데자네이루(Rio de Janeiro)</span>, 브라질</p>
<p><span class="accent">나폴리(Naples)</span>, 이탈리아</p>
```
## 1.3 font-weight 속성

font의 굵기를 조절합니다.

- normal : 보통
- bold
- bolder
- lighter
- number
- inital
- inherit : 부모 요소의 속성값을 상속

## 1.4 font-size 속성

글자 크기를 조절하는 속성이다. 기본 값은 상대 크기인 medium으로 설정되어 있습니다. font-size 속성은 상속을 받습니다. font-size의 크기는 여러 유형을 갖습니다.

- 절대 크기 : 브라우저에서 지정한 글자 크기 (px, pt)
- 상대 크기 : 부모 요소의 글자 크기를 기준 (em, rem)
- 백분율 : 부모 요소의 글자 크기를 기준으로 % 지정
- 숫자 : 브라우저에 상관없이 글자 크기를 직접 지정

초기에는 px나 pt와 같은 고정 단위를 많이 사용했으나, 최근에는 반응형 웹이나 모바일 환경을 고려하여 em, % 단위를 많이 사용한다.

- em : 부모에 상대적인 크기를 가진다.
    1em = 16px이며, 1em은 부모 요소의 글자 크기에 1배를 의미한다.

    부모의 상대적인 크기를 가지므로 부모가 많아질 수록 비율을 계산하기가 어려워진다.

- **rem** : 루트에 상대적인 크기를 가진다.
    1rem = 16px이며, 1rem은 html의 크기에 1배를 의미한다.

    rem은 em보다 최근에 나온 개념이라 호환성 이슈가 존재한다.

## 1.5 font 속성

폰트 관련 속성들을 한꺼번에 묶어서 표기할 수 있다. 그 순서는 다음과 같다.
font-style, font-variant, font-weight, font-size/line-height, font-family 순으로 작성해야 한다. font-size와 font-family는 필수이며 다른 속성은 옵션이다.

```CSS
<style>
* {font:italic inherit bold x-small/160% verdana}
</style>
```

CSS에는 UI의 특징에 따른 font를 미리 지정해놨다.

```CSS
font:menu
font:caption
font:icon
```

## 1.6 글자 색

```CSS
<style>
h1 {color:rgb(0,200,0);} /* rgb 값 사용(0~255) - 녹색 계열 */
h1 {color:rgba(0,200,0,0.3);} /* a는 투명도, 1은 불투명, 0은 완전 투명    */
h2 {color:blue;} /* 색상 이름 사용 - 파랑 */
.accent {color:#ff0000;} /* 16진수 사용 – 빨강 */
</style>
```

## 1.7 text-decoration 속성

텍스트에 밑줄을 긋거나 가로지르는 줄을 표시 할때 사용한다.

- none : 선을 만들지 않음
- line-through : 글자 중간에 선
- overline : 글자 위에 선
- underline : 글자 아래 선
- initial : 기본값
- inherit : 부모 요소의 속성값을 상속

## 1.8 text-align 속성

텍스트를 정렬해준다.

```CSS
/* 수평정렬 */
h1 {
text-align: center;
}
h2 {
text-align: left;
}
h3 {
text-align: right;
}
/* 양쪽 정렬 */
h4 {
text-align : justify;
}
```

수직정렬은 line-height 속성 값을 textBox의 height의 크기와 동일하게 맞춥니다.

## 1.8 text-indent 속성

텍스트를 들여쓸 때 사용한다.

## 1.9 line-height 속성

줄간격을 의미한다. 보통 글자 크기의 1.5 ~ 2배 정도를 설정한다.

```CSS
<style>
    /* 글자 크기 2배 */
    .big-line { line-height:2;}
    /* 글자 크기 0.7배 */
    .small-line { line-height: 0.7;}
</style>
```

## 1.10 text-transform 속성

영문 텍스트의 대문자나 소문자를 바꾸는 속성

- none : 입력된 그대로 출력
- capitalize : 단어의 첫번째 글자를 대문자
- uppercase : 모든 글자를 대문자
- lowercase : 모든 글자를 소문자로
- initial : 기본값으로 설정
- inherit : 부모 요소의 속성값을 상속

## 1.11 list-style-type 속성

순서 없는 목록의 불릿이나 순서 목록의 숫자를 바꾸는 속성이다.

- ul목록의 불릿 바꾸기
  - disc(채운원), circle(빈원), square
- ol목록의 불릿 바꾸기
  - decimal, decimal-leading-zero, lowerroman, upper-roman, lower-latin/ loweralpha, upper-alpha/upper-latin
- ul, ol불릿 없애기
  - none

```CSS
<style>
    .movie1 {
    list-style-type:decimal;
    }
    . movie2 {
    list-style-type: upper-roman;
    }
</style>
<ol class=“movie1">
    <li>명량</li>
    <li>극한직업</li>
    <li>신과함께</li>
    <li>국제시장</li>
</ol>
<ol class=“movie2">
    <li>명량</li>
    <li>극한직업</li>
    <li>신과함께</li>
    <li>국제시장</li>
</ol>
```

# 2. 배경 꾸미기

## 2.1 background-color 속성

```CSS


```

## 2.2 background-clip 속성

배경을 어디 까지 적용할지 지정한다.

- border-box : 박스 모델의 가장 외곽인 테두리까지 적용합니다.
- padding-box : 박스 모델에서 테두리를 뺀 패딩 범위까지 적용합니다
- content-box : 박스 모델에서 내용 부분에만 적용합니다.

## 2.3 background-image 속성

배경에 이미지를 지정한다.

```CSS
body { background-image: url('images/bg1.png'); }
```

## 2.4 background-repeat 속성

배경 이미지를 반복해서 채워 넣습니다.

- repeat(기본값) : 브라우저 화면에 가득 찰 때 까지 배경 이미지를 가로와 세로로 반복합니다.
- repeat-x : 브라우저 창 너비와 같아질 때 까지 배경 이미지를 가로로 반복합니다.
- repeat-y : 브라우저 창 높이와 같아질 때 까지 배경 이미지를 세로로 반복합니다.
- no-repeat : 배경 이미지를 한번만 표시하고 반복하지 않습니다.

## 2.5 background-size 속성

배경 이미지 크기 조절

```CSS
/* 원래 배경 이미지 크기 만큼 표시 */
.bg1{ background-size:auto;}

/* 크기 만큼 표시 */
.bg2 { background-size:200px 150px;}

/* 비율 만큼 표시 */
.bg3 { background-size:60% 40%; }

/*요소 안에 들어오도록 축소/확대*/
.bg4 { background-size:contain; }

/*배경 이미지로 요소를 모두 덮도록 확대/축소*/
.bg5 { background-size:cover; }

/* 원본 이미지 크기 만큼 표시 */
.bg6{ background-size:100% 100%; }
```