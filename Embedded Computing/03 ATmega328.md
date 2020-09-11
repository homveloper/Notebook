03 ATmega328
===

# 1. AVR

ATmega328은 Atmel 회사에서 개발됬습니다. Atmel의 마이크로컨트롤러의 라인업은 다음과 같습니다.

- 8051 계열
- AVR 계열
- ARM 계열 : 스마트폰 AP에 사용된다.

AVR은 8비트 구조의 RISC방식으로 메모리는 하버드 구조로 되어 있습니다. 현재는 32비트 AVR도 생산되고 있습니다.

AVR은 메모리에 따라 다음과 같은 종류가 있습니다.

- 타이니 : 0.5~16kb
- 메가 : 4~512kb
- X-메가 : 16~384kb

# 2. ATmega328P-PU

ATmega328P-PU의 의미는 다음과 같습니다.

- P(Pico) : Pico power로 저전력 버전입니다.
- P(Plastic dual in-line package) : PDIP 형태 패키지
    > 추가적으로 A와 M이 있습니다.
    > 
    > A(Thin Quad Flat Package)
    > 
    > M(Quad Flat no-leads Package)
- U(Unleaded) : 친환경 소재를 사용합니다. 동작온도는 -40~85도 입니다. 

## 2.1 사양


![사양](img/ATmega328사양.png)


ATmega328 핀 구조

![핀구조](img/ATmega328Pin.jpg)

7, 8, 20, 21, 22는 전원을 위한 핀이다. PB와 PC는 Port B와 Port C를 의미한다. PB6과 PB7, PC6는 아두이노 보드의 기능을 위한 핀이다.

## 2.2 레지스터

ATmega328은 256개의 정의 가능한 레지스터 중 119개 레지스터가 정의되어 있습니다. 

## 2.3 아두이노 코딩

아두이노는 비전공자들을 위한 마이크로컨트롤러 플랫폼입니다. 많은 수의 레지스터를 쉽게 제어할 수 있는 추상화된 함수를 제공합니다. 다만 119개의 레지스터를 모두 다루는 함수는 제공하지 않으므로 고급 기법을 사용하기 위해서는 레지스터를 직접 조작할 수 있어야 합니다.

## 2.4 Flash 메모리

플래시 메모리는 프로그램 저장을 위한 메모리입니다. 크기는 32KByte이며 기계어 명령어는 16비트 또는 32비트 단위로 구성되어 있습니다. 즉 32KByte / 16bit = 16K개 주소가 필요합니다. 이는 14비트로 나타낼 수 있는 크기입니다.

![flashmemory](img/ATmega328플레시메모리.png)

플래시 메모리는 2개의 영역으로 나뉘어집니다.어플리케이션 프로그램 영역과 부트로더 영역입니다.

- 어플리케이션 프로그램 영역 : 프로그램 저장
- 부트로더 영역 : 마이크로컨트롤러의 초기 부팅 시점에서 실행되는 특수 목적용 프로그램이 설치
    
    부트로더의 사용 여부는 선택가능하며, 0.5~4KB 크기로 되어있습니다.

## 2.5 SRAM

SRAM은 데이터 저장을 위한 데이터 메모리입니다. 레지스터와 주소를 함께 사용합니다. 레지스터 256개는 0x0000~0x00FF번지 까지 사용하며 SRAM은 0x0100~0x08FF번지 까지 사용합니다.

2K = 2048이며, 2진수로 표현시 0000 0100 0000 0000 이며 0 부터 시작하면 0000 0000 0000 0000 ~ 0000 0011 1111 1111 까지 쓸 수있는 것 입니다.

레지스터가 0x00FF까지 사용하므로 SRAM은 0000 0001 0000 0000 ~ 0000 0100 1111 1111까지 입니다.

![메모리할당도](img/메모리할당도.png)

## 2.6 EEPRON

데이터 영구 저장을 위한 데이터 메모리입니다. 제 3의 주소 공간을 사용하며 유일하게 번지로만 접근이 가능한 메모리입니다.

# 3. ATmega328을 사용하는 이유?

AVR 시리즈 마이크로컨트롤러 중에서 가장 많이 사용되는 것은 ATmega128입니다. 8비트 64핀 구성되며 128KB 플래시 메모리를 가지고 있습니다. ATmega328은 ATmega128의 염가 버전으로 동일한 속도를 제공하지만 핀 수와 메모리 적습니다.

- ATmega128과 동일한 속도
- 적은 핀과 메모리로 간단한 프로그램만 작성
- 아두이노에서 ATmega128을 공식적으로 지원x
- DIP타입 제공하므로 DIY가 쉬움

# 4. 레지스터

## 4.1 DDRx 레지스터 - 입출력 설정

DDRx(Data Direction Register, x : B, C, D)는 8개의 핀을 묶은 포트 단위의 입출력을 설정할 수 있습니다. 비트 별로 각 핀의 입출력을 제어합니다. 비트 값이 0이면 입력, 1이면 출력으로 설정됩니다. 

예를 들어 DDRB = 0x20은 2진수로 표현시 0010 0000 이며 이는 첫번째 자리가 PORT B의 8부터 시작해서 1은 PORT B의 13번 핀입니다.

DDRB, DDRC, DDRD 등의 레지스터 이름은 io.h 파일에 정의되어 있습니다.

![alt](img/DDRx.png)

## 4.2 PORTx 레지스터 - 데이터 출력

PORTx(Port Register, x : B, C, D)는 8개의 핀을 묶은 포트 단위의 데이터 출력을 합니다. 앞서 DDRx 처럼 비트 별로 각 핀의 출력을 제어 할 수 있으며, 비트 값이 0이면 GND, 1이면 VCC를 출력합니다. 

예를 들어 1을 출력하면 LED가 켜지고, 0을 출력하면 LED가 꺼집니다.

## 4.3 PINx 레지스터 - 데이터 입력

PINx(Port Input Register, x : B, C, D)는 해당 핀에 가해지는 갑이 저장되는 레지스터입니다. 0이면 GND, 1이면 VCC가 가해집니다. 해당 핀의 DDRx 레지스터 값이 0으로 설정되어 있어야 합니다.

![alt](img/PINx.png)

## 4.5 예제 : Blink

다음 예제는 C언어 작성된 코드입니다. LED가 1초 간격으로 깜빡이도록 구현되어 있습니다.

#define F_CPU는 CPU의 클럭 수를 조절합니다. 여기서는 16Mhz이므로 16000000L입니다.

DDRB = 0x20은 0010 0000에 위치한 즉 13번핀을 출력으로 설정합니다.

PORTB = 0x00은 GND 이므로 LED가 꺼집니다.
PORTB = 0x20은 VCC 이므로 LED가 켜집니다.

```C
#include <avr/io.h>
#define F_CPU 16000000L		//16Mhz
#include <util/delay.h>

int main(void)
{
	/* */
	DDRB = 0x20;

    /* Replace with your application code */
    while (1) 
    {
		PORTB=0x00;
		_delay_ms(1000);
		PORTB=0x20;
		_delay_ms(1000);
    }
	
	return 1;
}
```

다음 예제도 동일하지만 ARDUINO 방식의 코드입니다.

pinMode()는 입출력 핀을 설정합니다. 여기서 LED_BUILTIN은 13번 핀을 의미합니다.

digitalWrite(LED_BUILTIN, HIGH)는 출력을 의미합니다. 여기서는 LED_BUILTIN 즉 13번 핀에 연결된 LED가 켜집니다.



```C
// the setup function runs once when you press reset or power the board
void setup() {
    // initialize digital pin LED_BUILTIN as an output.
    // same with pinMode(13, OUTPUT);
    pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
    // same with digitalWrite(13, HIGH);
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(1000);                       // wait for a second
}
```

아두이노는 직관적인 코드 작성이 가능하지만 불필요한 전처리 코드가 포함되어 용량이 증가합니다. 이는 용량이 32KB밖에 안되는 ATmega328에서는 중요한 부분입니다.

![alt](img/c언어용량.png)
![alt](img/아두이노스타일용량.png)

## 4.4 데이터 레지스터 구조

 