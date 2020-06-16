document.writeln(1+1 + "<br>");
document.writeln(1.1+1.3);
document.writeln(2*4);
document.writeln(3/2);

document.writeln(Math.pow(3,2));
document.writeln(Math.round(1.4));
document.writeln(Math.sqrt(4));
document.writeln(Math.random());

document.writeln("string은 큰 따옴표나 작은 따옴표 안에");
document.writeln("숫자는 따옴표에서는 문자");
document.writeln("데이터형은 typeof()", typeof("1"));
document.writeln("문자와 숫자를 더한 데이터형은? : ",typeof(1+1 + "<br>"))


document.writeln("strig " + "합치기");
document.writeln("문자열의 길이 : " + "hello".length);

var a = b = 1;
document.writeln(a+"<br>");
document.writeln(b+"<br>")

if ( a==b)
    document.writeln("hello world<br>");


// == : 값이 일치
document.writeln(1 == "1","<br>");

// === : 데이터 형과 값이 일치
document.writeln(1 === "1","<br>");

document.writeln(undefined == null,"<br>");
document.writeln(undefined === null,"<br>");

document.writeln(0 === -0,"<br>");

// NaN : 0/0과 같은 연산으로 만들어지는 특수한 데이터 형
document.writeln(NaN === NaN,"<br>");

// != : !는 부정
// !== : 데이터형과 값이 정확하게 일치하지 않다면

if(true){
    document.writeln("hello world");
}else if("1"){
    document.writeln("dad")
}
else{
    document.writeln("world hello");
}

if("1"){
    document.writeln("조건문에 string : true","<br>")
}else{
    document.writeln("조건문에 string : false","<br>")
}

if(1){
    document.writeln("조건문에 int : true","<br>")
}else{
    document.writeln("조건문에 int : false","<br>")
}

if(0)
    document.writeln("int 0이면 실행안됨?","<br>")

var a = 5
switch(a){
    case 1 :
        document.writeln("hello world","<br>");
        break;
    default :
        document.writeln("default","<br>")
        break;
}

var b = "hello"
switch(b){
    case "hello" :
        document.writeln("hello world","<br>");
        break;
    default :
        document.writeln("default","<br>")
        break;
}

a = 1;
b = "1";

if(a&&b){
    document.writeln("string과 int는 논리연산자? : true","<br>");
}else{
    document.writeln("string과 int는 논리연산자? : false","<br>");
}



var c;
if(!c)
    document.writeln("c는 값이 없다.<br>");

if(!undefined)
    document.writeln("undefined <br>");

if(!null)
    document.writeln("null <br>");

if(!NaN)
    document.writeln("NaN<br>");

document.writeln(2/0);
document.writeln(0/0);

document.writeln("<br>")

var i = 5;
while(i--){
    document.writeln("hello world",i,"<br>")
}

for(var i = 0; i<10; i++){
    document.writeln("world hello world"+i+"<br>")
}

function mul(a,b){
    return a*b
}

var a = 2, b= 4;
document.writeln(a+" * "+b+" = "+mul(a,b)+"<br>");

var name = [1,2,3,4,5];
document.write(name.length+"<br>");
document.write(name+"<br>");

// name.push(6);
// name.concat([7,8]);
// name.unshift(0);
// name.splice(2,0,1.5);
// name.shift(0);
// name.pop(8);

// name.reverse();
// name.sort();

document.write(name+"<br>");



// 객체 선언 및 초기화의 방법
var human = {
    "name" : "철수", 
    "age" : 10, 
    "gender" : "남",

    "show" : function(){
        document.write("name : "+this.name+"<br>")
        document.write("age : "+this.age+"<br>")
        document.write("gender : "+this.gender+"<br>")
    }
};

var human = {};
human["name"] = "철수";
human["age"] = 10;
human["gender"] = "남";

var human = new Object();
human["name"] = "철수";
human["age"] = 10;
human["gender"] = "남";

// 객체 멤버 접근
document.write(human.name + "의 나이는 "+human["age"]+"살 입니다.<br>");

document.write("철수의 정보<br>")
for(key in human){
    document.write(key + " value : "+human[key]+"<br>");
}

// 객체 멤버 제거
delete human.gender

document.write("철수의 정보<br>")
for(key in human){
    document.write(key + " value : "+human[key]+"<br>");
}

// 유용한 유틸
document.write("human의 멤버 변수의 갯수 : " + Object.keys(human).length + "<br>");


// Object 객체
// 자바 스크립트의 최상위 객체로 모든 하위 js 객체는 다음과 같은 메서드를 가짐

document.write(human.constructor() + "<br>");
document.write(human.hasOwnProperty('age') + "<br>");
document.write(human.propertyIsEnumerable('age') + "<br>");
document.write(human.age.toString() + "<br>");

var text = new String("hello world")
document.write(text + "<br>");

var is = new Boolean(false)



//Number 객체
var num = new Number(123);
var num = new Number('123');
var num2 = 234;

document.write("num : " + num + "<br>");
document.write("num2 : " + num2 + "<br>");

if(num instanceof Number)
    document.write("num is Number ?" + "<br>");

if(num2 instanceof Number)
document.write("num2 is Number ?" + "<br>");

/*
    num2는 Number 객체가 아니지만, Number객체에서 
    제공하는 property와 method를 사용할 수 있다.
*/

/*
    Auto Boxing

    new 키워드를 사용하지 않아도 String, Number, Boolean은 
    원시 타입이면서 객체 처럼 동작합니다. 앞에서 num2가 Number 객체가 아님에도 해당
    property와 method를 사용할 수 있는 이유입니다.
*/

var name = "dog";
var age = 7;

// name은 원시 타입이지만 String의 length가 있음
document.write("name length : " + name.length + "<br>");
document.write("age" + age.toString() + "<br>");

// Date 객체

// Date(year, month+1, day)
var date = new Date(2020,6,8);
var date2 = new Date();     //현재 시간

document.write("date : " + date + "<br>")
document.write("date2 : " + date2 + "<br>")

var day= ['일요일', '월요일', '화요일', '수요일' ,'목요일' ,'금요일' ,'토요일'];

// getDay의 범위는 0~6이며 0은 일요일이다.
document.write("오늘의 요일  : " + day[date2.getDay()] + "<br>")

var birthday = new Date("1997-09-30");

document.write("만 나이 : " + (new Date().getFullYear() - birthday.getFullYear()) + "<br>");


/*
    자바스크립트 메모리 모델

    원시타입과 참조 타입 데이터의 저장 방식 이해하기

    var는 function-scoped 이고, let과 const는 block-scoped 입니다.

    var name = "Marcus";
    console.log(name);

    var name = "Jogeonsang";
    console.log(name);

    output: Marcus
    output: Jogeonsang

    다음과 같이 name이라는 변수를 2번 선언했는데도 에러가 나오지않고 각기 다른 값이 출력되는걸 볼 수 있다.
    
    var : 변수의 재 선언, 재 할당이 모두 가능하다.
    let : 변수의 재 선언이 불가능하다.            ex. 자바의 변수
    const : 변수의 재 선언, 재 할당이 불가능하다. ex. 자바의 final
*/

let myNumber = 23;
let newNumber = myNumber;   //myNumber의 주소로 할당됩니다.

if(myNumber === newNumber)
    document.write("둘의 주소가 동일<br>");

//하지만 myNumber는 원시타입이기 때문에, myNumber의 값이 변경되면 새로운
//주소에 할당되며, newNumber는 이전의 myNumber주소를 그대로 가리키고 있게됩니다.
myNumber = myNumber + 1;

if(myNumber !== newNumber)
    document.write("둘의 주소가 동일하지않음<br>");

// [중요!!] array는 let으로 선언하는 것이 아닌 const로 선언해야 주소가 변경되지 않는다.

const myArray = [];

myArray.push(1);
myArray.push(1);
myArray.push(1);
myArray.push(1);

let myArray2 = [];

myArray2.push(1);
myArray2.push(1);
myArray2.push(1);
myArray2.push(1);


/*
    함수

    자바스크립트에서는 함수도 객체입니다. 
    
    - 함수를 변수에 할당할 수 있음.
    - 함수를 함수의 인자로 사용할 수 있음
    - 함수를 반환값으로 사용할 수 있음
*/

// 함수를 변수에 할당
function getTitle(){
    return "hello world";
}

    // 1. 변수에 할당하거나
    var f = getTitle;
    document.write(f() + "<br>");

    // 2. 멤버변수에 할당하거나
    var message = {
        f : getTitle
    }
    document.write(message.f() + "<br>");

    // 3. 배열에 할당하거나
    var fArr = [1,2,3];
    fArr[0] = getTitle;
    document.write(fArr[0]() + "<br>");

// 함수 정의

    // 1. 함수 선언식
    function f1(a){
        return a;
    }

    // 2. 함수 표현식
    var f2 = function(a){
        return a*a;
    }

    // 3. 익명 함수 : 즉시 실행이 필요한 경우
    (function(a){
        return a * a * a;
    })(3);

var vscope = "global";

function fscopse(){
    var vscope = "local";
    // 종속변수
    document.write(vscope+"<br>")

    // 전역변수
    document.write(this.vscope+"<br>")
}
fscopse()


	
function a(){}

a = {
    b:function(){
    }
};

function cal(func, num){
    return func(num)
}
function increase(num){
    return num+1
}
function decrease(num){
    return num-1
}

document.write("1+1 : " +cal(increase,1)+"<br>");
document.write("1-1 : " +cal(decrease,1)+"<br>");


function cal2(mode){
    var funcs = {
        'plus' : function(left, right){return left + right},
        'minus' : function(left, right){return left - right}
    }
    return funcs[mode];
}
document.write(cal2('plus')(2,1)+"<br>");
document.write(cal2('minus')(2,1)+"<br>"); 


var process = [
    function(input){ return input + 10;},
    function(input){ return input * input;},
    function(input){ return input / 2;}
];
var input = 1;
for(var i = 0; i < process.length; i++){
    input = process[i](input);
    document.write(input+"<br>")
}


function sortNumber(a,b){
    // 위의 예제와 비교해서 a와 b의 순서를 바꾸면 정렬순서가 반대가 된다.
    return b-a;
}
var numbers = [20, 10, 9,8,7,6,5,4,3,2,1];
document.write(numbers.sort(sortNumber)); // array, [20,10,9,8,7,6,5,4,3,2,1]


// Closure
function factory_movie(title){
    return {
        get_title : function (){
            return title;
        },
        set_title : function(_title){
            title = _title
        }
    }
}

document.write("<br>")

ghost = factory_movie('Ghost in the shell');
matrix = factory_movie('Matrix');
 
document.write(ghost.get_title() + "<br>");
document.write(matrix.get_title() + "<br>");
 
ghost.set_title('공각기동대');
 
document.write(ghost.get_title() + "<br>");
document.write(matrix.get_title() + "<br>");



console.log(x);
var x = 3;
console.log(x);