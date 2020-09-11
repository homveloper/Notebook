/*
 * ButtonInput.c
 *
 * Created: 2020-05-13 오후 2:32:06
 * Author : bum44
 */ 

#define F_CPU 16000000L
#include <avr/io.h>
#include "UART.h"

void INIT_PORT(void){
	DDRB = 0x20;		// PB5 출력으로 설정
	PORTB = 0x00;		//PORTB가 꺼진상태에서 시작
	DDRD = 0x00;		// 버튼 입력
	PORTD = 0x04;       // PD2 풀업저항 사용
}

int main(void)
{
	/* Replace with your application code */
	INIT_PORT();
	UART_INIT();
	
	int state = 0;
	
	while (1)
	{
		//PORTD D2가 1인가?
		if((PIND & 0x04) == 0x04){
			PORTB = 0x00;	// LED OFF
			state = 0;
		}
		else{
			// 눌러지지 않은 상태에서 눌러진 상태로 바뀔때 마다 "*" 문자 전송
			if(state == 0)	UART_transmit('*');
			
			state = 1;
			PORTB = 0x20;	// LED ON
		}
	}
}

