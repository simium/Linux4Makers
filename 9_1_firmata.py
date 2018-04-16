from pyfirmata import Arduino, util
import time

# Create an Arduino object on serial port /dev/ttyACM0
board = Arduino("/dev/ttyACM0")

# LED pin on the Arduino board is a digital output pin on pin 13
led_pin = board.get_pin("d:13:o")

# Infinite loop, end with Control+C
while True:
    # Toggle the pin state every 0.5 seconds
    led_pin.write(0)
    time.sleep(0.5)
    led_pin.write(1)
    time.sleep(0.5)
