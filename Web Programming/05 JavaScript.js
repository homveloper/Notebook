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
    document.writeln("hello world");


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

document.write(human.name + "의 나이는 "+human["age"]+"살 입니다.<br>");

document.write("철수의 정보<br>")
for(key in human){
    document.write(key + " value : "+human[key]+"<br>");
}

var vscope = "global";

function fscopse(){
    var vscope = "local";
    document.write(vscope+"<br>")
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


// Closer

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
ghost = factory_movie('Ghost in the shell');
matrix = factory_movie('Matrix');
 
alert(ghost.get_title());
alert(matrix.get_title());
 
ghost.set_title('공각기동대');
 
alert(ghost.get_title());
alert(matrix.get_title());



var arr = []
for(var i = 0; i < 5; i++){
    arr[i] = function(id) {
        return function(){
            return id;
        }
    }(i);
}
for(var index in arr) {
    console.log(arr[index]());
}

function Person(){

}

var p1 = new person();
