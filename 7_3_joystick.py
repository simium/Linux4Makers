import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time

# Setup P9_42 (GPIO 7) as input
GPIO.setup("P9_42", GPIO.IN)

# Configure the ADC conversion
ADC.setup()

# Infinite loop, end with Control+C
while True:
    # Read analog pins P9_36 (AIN5) and P9_38 (AIN3)
    x_input = ADC.read("P9_36")
    y_input = ADC.read("P9_38")

    # Print the values
    print("X:{0:1.2f}, Y:{1:1.2f}".format(x_input, y_input))

    # If we read the input as high (3.3V)
    # just print a message
    if GPIO.input("P9_42") == GPIO.HIGH:
        print("Joystick pulsado.")

    # Sleep 0.01 seconds to allow the CPU to do other stuff
    time.sleep(0.1)
