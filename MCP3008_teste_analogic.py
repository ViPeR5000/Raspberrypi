#!/usr/bin/python
# -*- coding: utf-8 -*-

 
import spidev
import time
 
spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
# ler dados do SPI do chip  MCP3008 que tem 8 canais  adc's (0 até 7)
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout
 
while True:
    valor = readadc(0)
    volts = (value * 3.3) / 1024
    
    print ("%4d/1023 => %5.3f V % (value, volts))
    time.sleep(0.5)
