import RPi.GPIO as GPIO
import time
def boton1_callback(gpiopin):
    print("Pulsaste: 1")
def boton2_callback(gpiopin):
    print("Pulsaste: 2")
def boton3_callback(gpiopin):
    print("Pulsaste: 3")
def boton4_callback(gpiopin):
    print("Pulsaste: 4")

# Use BCM mode as explained in page 37
GPIO.setmode(GPIO.BCM)

# Activate channels 4, 17, 22 and 27 as input and enable their pull downs
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Call every callback function when the pins rise from low to high
# Let a bounce time of 200 ms between detections
GPIO.add_event_detect(22, GPIO.RISING, boton1_callback, bouncetime=200)
GPIO.add_event_detect(27, GPIO.RISING, boton2_callback, bouncetime=200)
GPIO.add_event_detect(17, GPIO.RISING, boton3_callback, bouncetime=200)
GPIO.add_event_detect(4, GPIO.RISING, boton4_callback, bouncetime=200)

# Infinite loop, end with Control+C
while True:
    # Now you can do other stuff
    # and not worry about button detection
    # Sleep 0.25 seconds to allow the CPU to do other stuff
    time.sleep(0.25)
