/*
* HelloBlink.c
*
* Created: 2020-04-21 오후 9:09:36
* Author : bum44
*/

#include <avr/io.h>
#define F_CPU 16000000L		//16Mhz
#include <util/delay.h>

int main(void)
{
	/* */
	DDRD = 0xF0;
	DDRB = 0x0F;

	/* Replace with your application code */
	while (1)
	{
		for(int i=0; i<8; i++){
			char p1 = 0x01 << i;
			char p2 = 0x01 << (7-i);
				
			PORTB = p1 | p2;
			PORTD = p1 | p2;
			_delay_ms(1000);
		}
	}
	
	return 1;
}

