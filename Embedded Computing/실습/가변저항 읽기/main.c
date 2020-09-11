#define F_CPU 16000000L
#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include "UART.h"

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
	int read;
	char buffer[5];
	
	UART_INIT();
	ADC_INIT(0);
	
	/* Replace with your application code */
	while (1)
	{
		read = readADC();
		
		intToString(read, buffer);
		UART_printString(buffer);
		UART_printString("\n");
		
		_delay_ms(1000);
	}
}