!/usr/bin/python
import spidev
 
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

class CPT_HUMIDITE:
 
 def readChannel(channel):
   val = spi.xfer2([1,(8+channel)<<4,0])
   data = ((val[1]&3) << 8) + val[2]
   return data