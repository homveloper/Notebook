#define F_CPU 16000000
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

ISR(INT0_vect){
	if(PIND & 0x04){
		PORTD = 0x0C;   //D2와 D3의 내부 풀업저항을 사용하기 위해서 항상 1로 세팅
		PORTB = 0x00;
	}else{
		uint8_t on_off = 0;
		for(int i =0; i<8; i++){
			on_off |= 0x01<<i;
			
			PORTD = (on_off << 4) | 0x0c;
			PORTB = on_off >> 4;
			_delay_ms(100);
		}
	}
}


ISR(INT1_vect){
	if(PIND & 0x08){
		PORTD = 0x0C;
		PORTB = 0x00;
	}else{
		uint8_t on_off = 0;
		for(int i =0; i<8; i++){
			on_off |= 0x80>>i;
			
			PORTD = (on_off << 4) | 0x0c;
			PORTB = on_off >> 4;
			_delay_ms(100);
		}
	}
}

void INIT_PORT(void){
	DDRB = 0x0F;        //PD8, PD9, PD10, PD11을 출력으로 설정
	PORTB = 0x00;       //PORTB 초기화

	DDRD = 0xF0;        //PD4, PD5, PD6, PD7을 출력으로 설정
	PORTD = 0x0C;       //PD2, PD3 풀업 저항 사용, PD4 ~ PD7 초기화
}

void INIT_INT(void){
	EIMSK |= (1<< INT0) | (1<<INT1);    // INT0, INT1 인터럽트 활성화
	EICRA |= (1<< ISC00) | (1<<ISC10);   // 버튼 상태 변화를 감지
	sei();                  // 전역적으로 인터럽트 허용
}

int main(void){
	INIT_PORT();        //포트 설정
	INIT_INT();      //PCINT2 인터럽트 설정
	while(1){

	}
}