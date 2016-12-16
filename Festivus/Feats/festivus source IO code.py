import RPi.GPIO as GPIO
import time

relay_pin = 27

GPIO.setmode( GPIO.BCM )
GPIO.setup( relay_pin, GPIO.OUT )

print ("\nlinker relay pin 23\n")

while True:
    GPIO.output (relay_pin,True)
    time.sleep(5)
    GPIO.output (relay_pin,False)
    time.sleep(1)
    
import RPi.GPIO as GPIO
import spidev
import time

led_pin = 23

# A0 = 0, A1 = 1, A2 = 2, A3 =3 
temp_channel = 0

GPIO.setmode( GPIO.BCM )
GPIO.setup( led_pin,GPIO.OUT )
spi = spidev.SpiDev()
spi.open(0,0)

print ("\nlinker led pin 23")
print ("Please the linker_temperature is connected to A%1d\n" % temp_channel)
time.sleep(3)

def readadc(adcnum):
# read SPI data from MCP3004 chip, 4 possible adc's (0 thru 3)
    if adcnum > 3 or adcnum < 0:
        return -1
    r = spi.xfer2([1,8+adcnum <<4,0])
    adcout = ((r[1] &3) <<8) + r[2]
    return adcout

while True:
        value = readadc(temp_channel)
        volts = (value * 3.3) / 1024
        print("value = %4d/1023" % value)
        print("volts = %5.3f V\n" % volts )
        if value < 650 :
                GPIO.output(led_pin,True)
        else :
                GPIO.output(led_pin,False)
        time.sleep(0.5)