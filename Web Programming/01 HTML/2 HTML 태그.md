HTML 태그
===

## form 태그

### ● POST 방식

입력 내용이 URL에 나타나지 않으며 주로 데이터를 **전달**할 때 사용합니다.
전달할 데이터가 많을 때 사용하며, 속도가 느립니다.

~~~
<form action="search.jsp" method="post">
    <input type="text" title="검색">
    <input type="submit" value="검색">
</form>
~~~

<form action="search.jsp" method="post">
    <input type="text" title="검색">
    <input type="submit" value="검색">
</form>

### ● GET 방식

입력했던 모든 내용이 URL에 나타나며 주로 데이터를 **요청**할 때 사용합니다.
URL의 최대길이는 2048이므로 긴 데이터에 대해서는 사용할 수 없습니다. 그리고 속도가 빠릅니다.

~~~
<form action="search.jsp" method="get">
    <input type="text" title="검색">
    <input type="submit" value="검색">
</form>
~~~

<form action="search.jsp" method="get">
    <input type="text" title="검색">
    <input type="submit" value="검색">
</form>

---

## label 태그

~~~
<label>
    ID
    <input tpye="text">
</label>
~~~

<label>
    ID
    <input tpye="text">
</label>


### ● 포커싱

지정된 id를 for로 지정하면 레이블을 클릭시 input 박스에 커서에 생김

~~~
<input tpye="text" id="user-id">
<label for="user-id">
    ID
</label>
~~~

<input tpye="text" id="user-id">
<label for="user-id">
    ID
</label>

---

## fieldset 태그

하나의 폼 안에서 여러 구역을 나구고 싶을 때 사용합니다.

---

## input 태그

~~~
<input type="text" id="user-name" size="10">
<input type="text" id="addr" size="10">
~~~

<input type="text" id="user-name" size="10">
<input type="text" id="addr" size="10">

### ● type 종류

1. text
~~~
<input type="text" id="text" size="10">
~~~
<input type="text" id="text" size="10">

2. hidden
~~~
<input type="hidden" id="hidden" size="10">
~~~
<input type="hidden" id="hidden" size="10">

3. search
~~~
<input type="search" id="search" size="10">
~~~
<input type="search" id="search" size="10">

4. email
~~~
<input type="email" id="email" size="10">
~~~
<input type="email" id="email" size="10">

5. text
~~~
<input type="text" id="text" size="10">
~~~
<input type="text" id="text" size="10">

6. url
~~~
<input type="url" id="url" size="10">
~~~
<input type="url" id="url" size="10">

7. password
~~~
<input type="password" id="password" size="10">
~~~
<input type="password" id="password" size="10">

8. tel
~~~
<input type="tel" id="tel" size="10">
~~~
<input type="tel" id="tel" size="10">

9. radio

~~~
<filedset>
    <legend> 졸업여행 </legend>
    <input type="radio" name="site" id="jeju" value="jeju"><label for="jeju">제주도</label> 
    <input type="radio" name="site" id="kumoh" value="kumoh"><label for="kumoh">금오산</label> 
    <input type="radio" name="site" id="danag" value="danag"><label for="danag">다낭</label> 
</filedset>
~~~

<filedset>
    <legend> 졸업여행 </legend>
    <input type="radio" name="site" id="jeju" value="jeju"><label for="jeju">제주도</label> 
    <input type="radio" name="site" id="kumoh" value="kumoh"><label for="kumoh">금오산</label> 
    <input type="radio" name="site" id="danag" value="danag"><label for="danag">다낭</label> 
</filedset>

10. checkbox

~~~
<filedset>
    <legend> 메뉴 </legend>
    <input type="checkbox" name="menu" id="beef" value="beef"><label for="beef">소고기</label> 
    <input type="checkbox" name="menu" id="kimchi" value="kimchi"><label for="kimchi">김치</label> 
    <input type="checkbox" name="menu" id="pizza" value="pizza"><label for="pizza">피자</label> 
</filedset>
~~~

<filedset>
    <legend> 메뉴 </legend>
    <input type="checkbox" name="menu" id="beef" value="beef"><label for="beef">소고기</label> 
    <input type="checkbox" name="menu" id="kimchi" value="kimchi"><label for="kimchi">김치</label> 
    <input type="checkbox" name="menu" id="pizza" value="pizza"><label for="pizza">피자</label> 
</filedset>

11. submit

~~~
<form action="register.php" method="post">
    <label>메일주소<input type="text"></label>
    <input type="submit" value="제출">
    <input type="reset" value="다시입력">
</form>
~~~

<form action="register.php" method="post">
    <label>메일주소<input type="text"></label>
    <input type="submit" value="제출">
    <input type="reset" value="다시입력">
</form>

12. image

~~~
<fomr>
    <label>아이디<input type="text" size="15"><label>
    <label>비밀번호<input type="password" size="15"><label>
    <input type="image" id="button" src="../img/펭카.jpg" alt="login">
</fomr>
~~~

<fomr>
    <label>아이디<input type="text" size="15"><label>
    <label>비밀번호<input type="password" size="15"><label>
    <input type="image" id="button" src="../img/펭카.jpg" alt="login">
</fomr>

### ● 속성 종류

1. autofocus

2. placeholder

3. readonly

4. required

---

## select 태그

~~~
<select id="class">
    <option value="archi">건축공학과</option>
    <option value="mechanic">기계공학과</option>
    <option value="industry">산업공학과</option>
    <option value="electro">전기전자공학과</option>
    <option value="computer" selected>컴퓨터공학과</option>
    <option value="chemical">화학공학과</option>
</select>
~~~

<select id="class">
    <option value="archi">건축공학과</option>
    <option value="mechanic">기계공학과</option>
    <option value="industry">산업공학과</option>
    <option value="electro">전기전자공학과</option>
    <option value="computer" selected>컴퓨터공학과</option>
    <option value="chemical">화학공학과</option>
</select>

---

