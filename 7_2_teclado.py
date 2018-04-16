import RPi.GPIO as GPIO
import time

# Use BCM mode as explained in page 37
GPIO.setmode(GPIO.BCM)

# Activate channels 4, 17, 22 and 27 as input and enable their pull downs
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Infinite loop, end with Control+C
while True:
    # If we read the input as high (3.3V)
    # just print a message
    if GPIO.input(22) == GPIO.HIGH:
        print("Pulsaste: 1")
    elif GPIO.input(27) == GPIO.HIGH:
        print("Pulsaste: 2")
    elif GPIO.input(17) == GPIO.HIGH:
        print("Pulsaste: 3")
    elif GPIO.input(4) == GPIO.HIGH:
        print("Pulsaste: 4")

    # Sleep 0.25 seconds to debounce
    time.sleep(0.25)
