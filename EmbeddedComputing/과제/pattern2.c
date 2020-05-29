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
	DDRD = 0xFC;
	DDRB = 0x03;

	/* Replace with your application code */
	while (1)
	{
		for(int i=0; i<8; i++){
			if((i==4) | (i==7))
				continue;
			
			PORTD = 0x01 << (i+2) | 0x01 << (9-i);
			PORTB = 0x02 >> i | 0x01 >> (6-i);
			_delay_ms(1000);
		}
	}
	
	return 1;
}

