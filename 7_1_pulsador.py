import RPi.GPIO as GPIO
import time

# Use BCM mode as explained in page 37
GPIO.setmode(GPIO.BCM)

# Activate channel 4 as input and enable its pull down
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Infinite loop, end with Control+C
while True:
    # If we read the input as high (3.3V)
    if GPIO.input(4) == GPIO.HIGH:
        # Just print a message
        print("Pulsaste el boton!")
        # Sleep 0.25 seconds to debounce
        time.sleep(0.25)

    # Sleep 0.01 seconds to allow the CPU to do other stuff
    time.sleep(0.01)
