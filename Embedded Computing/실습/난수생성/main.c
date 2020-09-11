/*
 * randomNumber.c
 *
 * Created: 2020-05-20 오후 12:30:01
 * Author : bum44
 */ 

#define F_CPU 16000000
#include <avr/io.h>
#include "UART.h"
#include <stdio.h>
#include <util/delay.h>

void ADC_INIT(unsigned char channel){
	ADMUX |= 0x40;							// AVCC를 기준전압으로 선택
	ADCSRA |= 0x07;							// 분주비 설정
	ADCSRA |= (1<< ADEN);					// ADC 활성화
	ADCSRA |= (1<<ADATE);					// 자동트리거 모드
	ADMUX |= ((ADMUX & 0xE0) | channel);	// 채널선택
	ADCSRA |= (1<<ADSC);					// 변환시작
}

int readADC(void){
	while(!(ADCSRA & (1<<ADIF)));			// 변화종료 대기
	return ADC;								// 10비트 값을 변환
}

void intToString(int n, char *buffer){
	sprintf(buffer, "%04d", n);
	buffer[4] = '\0';
}


int main(void)
{
	UART_INIT();
	ADC_INIT(0);
	srand(readADC());
	
    /* Replace with your application code */
	
	UART_printString("Start generating random number\n");

    while (1) 
    {
		int randomNumber = rand() % 100 + 1;	//1~100사이 난수
		
		UART_print8bitNumber(randomNumber);
		UART_transmit('\n');
		
		_delay_ms(1000);
    }
}

