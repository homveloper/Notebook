BOM이란
===

# BOM

BOM(Browser Object Model)은 브라우저에 계층적으로 내장되어 브라우저를 제어하는데 사용하는 객체입니다.

자주사용하는 함수 목록은 다음과 같다.

- alert(str) : 경고창을 띄운다
- confirm() : confirm박스를 띄운다.
- prompt() : prompt창을 띄운다.
- open() : 새로운 브라우저 창을 연다.
- close() : 현재의 브라우저를 종료시킨다.
- focus() : 현재의 윈도우로 포커스를 옮긴다.
- moveBy(x, y) : 윈도우를 (x,y)로 이동(상대좌표)
- moveTo(x, y) : 윈도우를 (x,y)로 이동(절대좌표)
- resizeTo() : 창의 크기를 변경시킬 때 사용
- print() : 인쇄 창을 띄운다.
- setInterval() : 일정 간격으로 지속적인 실행문을 실행할 때
- setTimeout() : 일정 간격으로 한 번만 실행문을 실행할 때
- clearInterval(ID) : Interval 중지
- clearTimeout(ID) : Timeout 중지

# 2. 함수

## 2.1 open()

주로 팝업을 띄울 때 사용합니다.

```JavaScript
    window.open('url경로','대상','옵션')
```

### 대상

- blank : 새 창에 열림 기본값
- _parent : 부모 프레임에 열림
- self : 현재 페이지를 대체
- top : 로드된 프레임셋을 대체
- 임의의 이름 : 새 창이 열리고 창의 이름을 지정 , 동일한 이름에 다시 open() 을 하면 기존의 열린 창의 내용이 바뀜

### 옵션

- width : 창의 너비
- height : 창의 높이
- history : 네비게이션 경로를 담고 있는 object
- location : 창의 URL 주소 입력 영역 노출 여부를 결정 숨김 = 노출 =yes
- opener : open() 함수로 현재 윈도우를 열어준 부모 윈도우 부모와 자식 연결
- toolbars : 창의 도구 상자 노출 여부를 결정 숨김 = 노출 =yes
- scrollbars : 창의 스크롤 막대 노출 여부를 결정 숨김 = 노출 =yes
- status : 창의 상태 영역 노출 여부를 결정 숨김 = 노출 =yes
- left : 창의 좌 우 수평 위치를 설정
- top : 창의 상 하 수직 위치를 설정

## 2.2 setInterval()와 clearInterval()

일정한 간격으로 반복적으로 함수를 실행한다.

```JavaScript
var 참조변수 = setInterval ('스크립트 실행문 (함수)', 시간 간격(ms))
clearInterval(참조변수); //setInterval 을 종료
```

## 2.3 setTimeout()와 clearTimeout()

일정한 시간이후에 한번만 실행한다.

```JavaScript
var 참조변수 = setTimeout ('스크립트 실행문', 시간 간격 ms )
clearTimeout(참조변수); //setTimeout 을 종료
```

