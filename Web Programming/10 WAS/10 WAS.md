10 WAS
===

# 1. Web Server

웹클라이언트로 부터 HTTP 요청을 받아들이고 적절하게 응답하는 역할을 한다.

웹서버는 웹 클라이언트(브라우저)로 부터 HTTP를 통해 온 요청을 처리하여 HTTP로 응답을 합니다.

<img width="50%" src="../img/WebServer.png">

게시판을 작성하려면 어떻게 해야 할까요? 여기 제시된 코드가 있습니다. 하나의 게시글을 표현할 때 마다 이 코드를 작성할 필요는 없습니다. 

```HTML
<table style="border : 1px solid black;">
    <tr>
        <th>번호</th>
        <th>제목</th>
        <th>글쓴이</th>
        <th>날짜</th>
        <th>조회수</th>
    </tr>

    <tr>
        <td>공지</td>
        <td>[학사] 2020년 2학기 교내 성적장학생 선발관련 외국어 성적표 제출 안내 (~6/30,화)</td>
        <td>[조교]</td>
        <td>2020.04.28</td>
        <td>98</td>
    <tr>
</table>
```

1. 데이터베이스에서 전체 게시글의 정보를 조회
2. tr,td를 반복적으로 실행하는 코드 작성
3. 이러한 코드를 실행하는 환경(Web Container)


## 페이지

- 정적 페이지 : 항상 동일한 파일

- 동적 페이지 : 요청에 맞는 동적인 콘텐츠

## Web Container의 역할

- 통신 지원 : sevlet과 웹 서버가 서로 통신할 수 있는 손쉬운 방법 제공
- 생명주기 관리 : sevlet이 생성되어 동작한뒤 사라지는 과정을 알아서 관리
- 멀티스레딩 지원 : Container는 요청이 들어오면 그 요청을 전담하는 새로운 자바 스레드를 생성
- 보안
- JSP(Java Server Page) 지원


# 2. WAS(Web Application Server)

웹서버와 Web Container를 포함한 것으로, Web Container는 Servlet, ASP, JSP, PHP 등의 웹 언어로 작성된 웹 어플리케이션을 서버단에서 실행한다. 데이터베이스 작업과 웹 서비스 제공이 주요 기능이다.

# 3. Servlet

Servlet은 Java를 사용하여 웹페이지를 동적으로 생성하는 서버측 프로그램 혹은 그 사양을 말한다. 즉 Servlet은 웹 서버의 성능을 향상하기 위해 사용되는 Java Class의 일종이다. 

JSP가 HTML 문서 안에 Java 코드를 포함하고 있는 반면, Servlet은 Java 코드 안에 HTML을 포함하고 있다.

## 특징

- 클라이언트의 요청에 대해 동적으로 작동하는 웹 어플리케이션 컴포넌트

- HTML을 사용하여 요청에 응답한다.

- Java Thread를 이용하여 동작하다.

- MVC 패턴에서 Controller로 이용된다.

- HTTP 프로토콜 서비스를 지원하는 javax.servlet.http.HttpServlet 클래스를 상속받는다. UDP보다 속도가 느리다.

- HTML 변경 시 Servlet을 재컴파일해야 하는 단점이 있다.
  
## 생명주기

![alt](../img/servlet%20생명주기.png)

## 동작 방식

<img width="" src="../img/Servlet%20동작.png">

## Servlet Container

Servlet Container는 Sevlet을 관리해주는 Container입니다. 예를 들어, 서블릿이 어떠한 역할을 수행하는 정의서라고 보면, 서블릿 컨테이너는 그 정의서를 보고 수행한다고 볼 수 있습니다. **서블릿 컨테이너는 클라이언트의 요청(Request)을 받아주고 응답(Response)할 수 있게**, 웹서버와 소켓을 만들어 통신하며 대표적인 예로 **톰캣(Tomcat)**이 있습니다. 톰캣은 실제로 웹서버와 통신하여 JSP(자바 서버 페이지)와 Servlet이 작동하는 환경을 제공해줍니다.

## JSP. Java Server Page

Servlet은 Java 소스코드 안에 HTML 코드가 있는 반면, JSP는 Java 코드가 들어가 있는 HTML 코드가 있는 웹 어플리케이션 프로그래밍 기술입니다. HTML 속에 자바코드는  <% 소스코드 %> 또는 <%= 소스코드 =%>형태로 들어갑니다. 자바 소스코드로 작성된 이 부분은 웹 브라우저로 보내는 것이아니라 웹 서버에서 실행되는 부분입니다.

Servlet의 규칙이 꽤나 복잡하기 때문에 JSP가 나오게 되었습니다. JSP는 WAS에 의하여 Servlet Class로 변환하여 사용되어 집니다.

<img width="" src="../img/JSP%20동작.png">

## HttpServletRequest

요청 유형, 쿠기, 세션 등 HTTP 요청에 대한 인터페이스를 추상화한 것으로 **HTTP 요청 관련 메소드를 포함**하고 있습니다. 요청에 대한 모든 정보를 담고 있습니다.


request에는 사용자의 입력에 대한 정보도 포함하고 있습니다.

- request.getParameter(String name) : html의 tag에 설정된 name으로 가져옵니다.
- request.getParameterValues(String name) : name으로 설정된 모든 tag의 값을 배열로 가져옵니다.
- request.getParameterNames() : 웹브라우저가 전송한 parameter의 이름을 조회합니다.
- request.getParameterMap() 

## HttpServletResponse