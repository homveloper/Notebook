LED 깜빡이
===

# 코드

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
        PORTB = 0x00;
        _delay_ms(1000);
        PORTB = 0x20;
        _delay_ms(1000);
    }
	
	return 1;
}
```