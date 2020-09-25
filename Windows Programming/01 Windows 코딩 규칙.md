01 Windows 코딩 규칙
===

# 시작

여러분들이 처음 윈도우 프로젝트를 보시게 되면 DWORD_PTR이나 LPRECT와 같은 이상한 자료형들로 인해 혼란이 오실겁니다. 이번 과정을 통해 윈도우의 코딩 규칙을 배워보도록 하겠습니다.

Winodws API는 함수나 COM(Component Object Model)인터페이스들로 구성되어 있습니다. Windows API는 C++로 구현되어있지만 C++ 클래스는 거의 사용하지 않습니다. 대신 C++에서 제공하는 Typedefs를 통해 새롭게 정의한 자료형을 사용하고 있습니다.

# Typedefs

Windows 헤더는 여러가지 typedefs를 포함하고 있습니다. 이런 것들은 WinDef.h 파일에 정의되어 있습니다. 앞으로도 자주 보시게 될것입니다.

## Integer 형

|Data type|Size|Signed|
|:---:|:---:|:---:|
|BYTE|8bits|Unsigned|
|DWORD|32bits|Unsigned|
|INT32|32bits|Signed|
|INT64|64bits|Signed|
|LONG|32bits|Signed|
|LONGLONG|64bits|Signed|
|UINT32|32bits|Unsigned|
|UINT64|64bits|Unsigned|
|ULONG|32bits|Unsigned|
|ULONGULONG|64bits|Unsigned|
|WORD|16bits|Unsigned|

위의 표에서 나오듯이 중복된 자료형이 있습니다. 이는 Windows API의 발전 과정에 따른 영향입니다. 여기에 있는 자료형들은 고정된 사이즈를 가지고 32bit와 64bit 어플리케이션에서 모두 동일하게 적용됩니다. 예를 들어, DWORD형은 항상 32bits입니다.

## Boolean Type

BOOL은 Boolean 형태를 사용하기 위해 정수형 값을 typedef한 자료형입니다. 헤더 파일은 WinDef.h에 BOOL형태로 두가지가 정의되어 있습니다.

```c++
//C++
#define FALSE 0
#define TRUE 1
```

TRUE가 정의되어 있지만 BOOL 유형을 반환하는 대부분의 함수는 0이 아닌값을 반환하여 bool 진리를 나타냅니다. 따라서 항상 다음과 같이 작성하셔야 합니다.

```c++
// Yes!!
BOOL result = function();
if(result){
    ...
}
```

그리고 이렇게 사용해서는 안됩니다.

```c++
// No!!
if(result == TRUE){
    ...
}
```

> 주의!! BOOL형은 정수 자료형으로 정의한 것이지 C++의 bool 자료형과 동일하지 않다는 것을 주의해야 합니다.

## Pointer Types

Winodws는 pointer-to-X 형식의 다양한 자료형을 정의하고 있습니다. 이런 자료형들은 보통 이름에 접두사 P나 LP가 붙습니다. 예를 들어, LPRECT는 RECT의 포인터이며, RECT는 사각형을 표현하는 구조체입니다. 아래의 예시는 모두 동일한 의미를 가지고 있습니다.

```c++
//C++
RECT*   rect;   // Rect 구조체의 포인터
LPRECT  rect;   // 동일합니다.
PRECT   rect;   // 이것도 동일한 사용법입니다.
```

옛날부터 P는 pointer, LP는 long pointer를 의미했습니다. Long pointers(=far pointers)는 16bit Windows에서 현재 세그먼트 외부의 메모리 범위를 처리하는데 필요한 holdover입니다. LP 접두사는 16bits 코드를 32bits Winodws에 쉽게 포팅하기 위해 있습니다. 현재는 구별이 없습니다. 포인터는 포인터일 뿐입니다.

## Pointer Precision Types

아래의 자료형은 32bit 어플리케이션에서는 32bits로, 64bit 어플리케이션에서는 64bits로 포인터의 크기가 정해집니다. 이 사이즈는 컴파일시에 결정됩니다. 32bit 어플리케이션이 64bit Winodws에서 동작되더라도 자료형의 크기는 여전히 32bit입니다.

> 참고. 64bit 어플리케이션은 32bit Windows에서 동작하지 않습니다.

- DWORD_PTR
- INT_PTR
- LONG_PTR
- ULONG_PTR
- UINT_PTR

위의 자료형은 정수형을 포인터로 형변환 할 때 사용됩니다. 또 포인터 산술 변수를 정의하고 메모리 버퍼의 전체 바이트 범위에 걸쳐 반복하는 루프 카운터를 정의하는데도 사용됩니다. 일반적으로는 32bit 값을 64bit Winodws에 64bit로 확장할 때 사용됩니다.

## Hungarian Notation

MSDN의 대부분의 예제들은 헝가리안 표기법을 사용하고 있지만 꼭 접두사(예. index의 i, row의 rw)를 기억하고 있을 필요는 없습니다.

헝가리안 표기법은 컴퓨터 프로그래밍에서 변수나 함수의 이름에 그 종류, 즉 자료형을 명시하는 표기법으로, 명명 규칙의 일종이다. 고안자인 찰스 시모니가 헝가리인이었던 것에서 헝가리안 표기법으로 불립니다.

