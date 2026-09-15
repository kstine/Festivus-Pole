import os
import sys
import time

# GPIO Simulator for macOS / Actual GPIO for Raspberry Pi
try:
    import RPi.GPIO as GPIO
except ImportError:
    # GPIO Simulator for macOS/Linux (not Raspberry Pi)
    import time as GPIO
    GPIO = type('GPIO', (), {})
    GPIO.setup = lambda pin, mode, initial=True: setattr(GPIO, f'setup_{pin}', initial)
    GPIO.output = lambda pin, value: setattr(GPIO, f'output_{pin}', value)
    GPIO.HIGH = 1
    GPIO.LOW = 0
    GPIO.BCM = 'BCM'
    GPIO.setmode = lambda mode: None

relay_pin = 27

if os.name == 'posix':  # Raspberry Pi
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_pin, GPIO.OUT)
    print("\nlinker relay pin 23\n")

while True:
            GPIO.output(relay_pin, True)
            time.sleep(5)
            GPIO.output(relay_pin, False)
            time.sleep(1)
            
import os
import sys
import time

# SPI Simulator for macOS / Actual SPI for Raspberry Pi
try:
    import spidev
except ImportError:
    # SPI Simulator for macOS/Linux
    class SpiDev:
        def __init__(self, bus=0, device=0):
            pass
        def open(self, bus, device):
            pass
        def write(self, data):
            return [0] * 3  # Simulate
        def xfer2(self, data):
            return data
    spi = SpiDev()
    spi.open(0, 0)

# Use GPIO module
if os.name == 'posix':
    led_pin = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)
    spi = spidev.SpiDev()
    spi.open(0, 0)
    print("\nlinker led pin 23")
    print(f"Please the linker_temperature is connected to A{temp_channel}")
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
        print(f"value = {value}/1023")
        print(f"volts = {volts:.3f} V")
        if value < 650:
            GPIO.output(led_pin, True)
        else:
            GPIO.output(led_pin, False)
        time.sleep(0.5)