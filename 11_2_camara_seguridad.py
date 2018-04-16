import RPi.GPIO as GPIO
import time
import os

# Use BCM mode as explained in page 37
GPIO.setmode(GPIO.BCM)

# Activate channel 4 as input and enable its pull up
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Infinite loop, end with Control+C
while True:
    # Wait 5 seconds for the GPIO to fall from high to low
    channel = GPIO.wait_for_edge(4, GPIO.FALLING, timeout=5000)

    # If the GPIO fall was detected
    if channel is not None:
        # Execute a command line instruction from here
        os.system('fswebcam -r 1280x720 -S 5 --jpeg 100 --save /home/pi/%H%M%S.jpg')
