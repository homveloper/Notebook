#include <avr/io.h>
#define F_CPU 16000000L		//16Mhz
#include <util/delay.h>

int main(void)
{
	/* */
	DDRB = 0x01;
	DDRD = 0x80;

	/* Replace with your application code */
	while (1)
	{
		PORTB = 0x01;
		PORTD = 0x00;
		_delay_ms(1000);
		PORTB = 0x00;
		PORTD = 0x80;
		_delay_ms(1000);
	}
	
	return 1;
}