#ifndef _UART_H_
#define _UART_H_

#include <avr/io.h>

void UART_INIT(void);
unsigned char UART_receive(void);
void UART_transmit(unsigned char data);
void UART_printString(char *str);
void UART_print8bitNumber(uint8_t no);
void UART_print16bitNumber(uint16_t no);
void UART_print32bitNumber(uint32_t no);

#endif