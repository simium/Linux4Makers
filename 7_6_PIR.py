import Adafruit_BBIO.GPIO as GPIO
import time

# Setup P9_12 (GPIO 60) as input
GPIO.setup("P9_12", GPIO.IN)

# Infinite loop, end with Control+C
while True:
    # If we read the input as low (0V)
    # just print a message
    if GPIO.input("P9_12") == GPIO.LOW:
        print("PIR activado!")
    # Sleep 0.01 seconds to allow the CPU to do other stuff
    time.sleep(0.1)
