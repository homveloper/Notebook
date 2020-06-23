16 LCD
===

# 1. LCD

액체와 고체의 중간 형태 물질로 1960년대 이후 디스플레이로 사용되기 시작했습니다.

Text LCD는 3개의 제어핀으로 동작 하며, 4개 또는 8개의 데이터 핀으로 제어 또는 데이터를 전송합니다. 

## 1.1 제어순서

- RS(Register Select) : 텍스트 LCD를 제어하기 위해서는 2개의 레지스터, 즉 제어 레지스터와 데이터 레지스터가 사용되며, RS 신호는 명령을 담고 잇는 레지스터와 데이터를 담고 있는 레지스터 중 하나를 선택하기 위해 사용된다.

- R/W : 읽기(High) 및 쓰기(Low)모드를 선택하기 위해 사용된다. 일반적으로 LCD는 데이터를 쓰기 위한 용도로만 사용하므로 R/W 신호는 GND에 연결한다.

- E(Enable) : 하강 엣지에서 LCD 드라이버가 처리를 시작하도록 지시하기 위한 신호로 사용된다.

## 1.2 제어 명령어

![alt](img/LCD%20제어%20명령어.png)

RS를 제어 레지스터로 설정한 뒤 다음과 같은 명령 코드를 할당한다.


## 1.3 회로도

![alt](img/LCD%20회로도.png)

![alt](img/LCD%20핀%20설명.png)

- 7~14 : 데이터 신호 핀이 8개 있으며, 8bit 모드에서는 RS와 E, DB0~7을 포함 총 10개의 핀이 필요합니다.
- 3 : Vo는 LED의 텍스트 밝기를 조절합니다.
- 15~16 : LED에 필요한 백라이트 전원입니다.
- 4 : RS는 현재 보내는 데이터가 출력을 위한 데이터인지 명령어 인지를 선택하는 레지스터입니다.
- 5 : 0은 읽기, 1은 쓰기를 의미합니다.


## 1.4 LCD 메모리 및 표시영역

최대 80문자 저장이 가능하며 그 중 일부인 32문자만 표시된다.

- 1행으로 표시하는 경우(N=0) 0x00 ~ 0x4F(80개 주소)로 연속적으로 정해짐

- 2행으로 표시하는 경우(N=1) 0x00 ~ 0x27, 0x40 ~ 0x67로 정해짐


## 1.5 LCD 제어 상수

```c++
#define PORT_DATA		PORTD		    // 데이터 핀 연결 포트
#define PORT_CONTROL	PORTB		    // 제어 핀 연결 포트
#define DDR_DATA		DDRD		    // 데이터 핀의 데이터 방향
#define DDR_CONTROL		DDRB		    // 제어 핀의 데이터 방향

#define RS_PIN			0		        // RS 제어 핀의 비트 번호
#define E_PIN			1		        // E 제어 핀의 비트 번호

#define COMMAND_CLEAR_DISPLAY	0x01
#define COMMAND_8_BIT_MODE		0x38	// 8비트, 2라인, 5x8 폰트
#define COMMAND_4_BIT_MODE		0x28	// 4비트, 2라인, 5x8 폰트

#define COMMAND_DISPLAY_ON_OFF_BIT		2
#define COMMAND_CURSOR_ON_OFF_BIT		1
#define COMMAND_BLINK_ON_OFF_BIT		0
```

## 1.6 LCD 8비트 회로도

![alt](img/LCD%208비트%20모드.png)

## 1.7 LCD 4비트 회로도

![alt](img/LCD%204비트%20모드.png)
