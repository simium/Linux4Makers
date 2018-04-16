import RPi.GPIO as GPIO
import time

# Use BCM mode as explained in page 37
GPIO.setmode(GPIO.BCM)

# Activate channel 4 as output and make it low as default
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)

# Infinite loop, end with Control+C
while True:
    # Set pin high (3.3V)
    # and tell the user
    GPIO.output(4, GPIO.HIGH)
    print("Rele ON!")
    # Sleep half a second
    time.sleep(0.5)
    # Set pin low (0V)
    # and tell the user
    GPIO.output(4, GPIO.LOW)
    print("Rele OFF!")
    # Sleep half a second
    time.sleep(0.5)
