#define F_CPU 16000000
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

ISR(PCINT2_vect){
	if(PIND & 0x08){
		PORTD = 0x08;   //D3의 내부 풀업저항을 사용하기 위해서 항상 1로 세팅
		PORTB = 0x10;	//D12의 내부 풀업저항을 사용하기 위해서 항상 1로 세팅
		}else{
		uint8_t on_off = 0;
		for(int i =0; i<8; i++){
			on_off |= 0x01<<i;
			
			PORTD = (on_off << 4) | 0x08;
			PORTB = on_off >> 4 | 0x10;
			_delay_ms(100);
		}
	}
}


ISR(PCINT0_vect){
	if(PINB & 0x10){
		PORTD = 0x08;
		PORTB = 0x10;
		}else{
		uint8_t on_off = 0;
		for(int i =0; i<8; i++){
			on_off |= 0x80>>i;
			
			PORTD = (on_off << 4) | 0x08;
			PORTB = on_off >> 4 | 0x10;
			_delay_ms(100);
		}
	}
}

void INIT_PORT(void){
	DDRB = 0x0F;        //PD8, PD9, PD10, PD11을 출력으로 설정
	PORTB = 0x10;       //D12 내부 풀업저항 

	DDRD = 0xF0;        //PD4, PD5, PD6, PD7을 출력으로 설정
	PORTD = 0x08;       //PD3 내부 풀업저항
}

void INIT_PCINT(void){
	PCICR |= (1<< PCIE2) | (1<< PCIE0);    // PCINT2, PCINT0 인터럽트 활성화
	PCMSK2 |= (1<< PCINT19);   // PD3 핀의 변화 인터럽트 허용
	PCMSK0 |= (1<<PCINT4);		// PD12 핀의  핀 변화 인터럽트 허용
	sei();                  // 전역적으로 인터럽트 허용
}

int main(void){
	INIT_PORT();        //포트 설정
	INIT_PCINT();      //PCINT2 인터럽트 설정
	while(1){

	}
}