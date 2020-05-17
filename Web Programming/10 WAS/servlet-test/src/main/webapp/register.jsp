<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<body>
	    <form action="register", method="GET">
        <h1>회원가입</h1>
        <fieldset>
            <legend>로그인 정보</legend>
            <div>
                <label>아이디<input type="text" name="userid" autofocus></label>               
            </div>
            <div>                
                <label>비밀번호<input type="password" name="pwd" autofocus></label> 
            </div>
            <div>                
                <label>나이<input type="text" name="age" autofocus></label> 
            </div>
        </fieldset>
        <fieldset>
            <legend>개인정보</legend>
            <div>
                <label>이름</label>
                <input type="text">
            </div>
            <div>성별
                <input type="radio" name="gender" id="male" value="male"><label for="male">남</label>
                <input type="radio" name="gender" id="female" value="female"><label for="female">여</label>
            </div>
            <div>주소
                <select name="address">
                    <optgroup label="선산읍">
                        <option value="완전리">완전리</option>
                        <option value="동부리">동부리</option>
                        <option value="노상리">노상리</option>
                    </optgroup>
                    <optgroup label="고아읍">
                        <option value="관심리">관심리</option>
                        <option value="이례리">이례리</option>
                        <option value="오로리">오로리</option>
                    </optgroup>
                </select>
            </div>

            <label>메일주소<input type="email"></label>
            <label>전화번호<input type="tel"></label>

            <fieldset>
                <legend>관심분야</legend>
                <label><input type="checkbox" name="interests" value="주방제품">주방제품</label>
                <label><input type="checkbox" name="interests" value="가전제품">가전제품</label>
                <label><input type="checkbox" name="interests" value="패션">패션</label>
                <br>
                <label><input type="checkbox" name="interests" value="유아제품">유아제품</label>
                <label><input type="checkbox" name="interests" value="스포츠용품">스포츠용품</label>
                <label><input type="checkbox" name="interests" value="도서">도서</label>
            </fieldset>
        </fieldset>
        <input type="submit" value="회원가입">
        <input type="reset" value="입력취소">
    </form>
</body>
</body>
</body>
</html>