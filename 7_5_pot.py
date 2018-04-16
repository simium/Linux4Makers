import Adafruit_BBIO.ADC as ADC
import time

# Configure the ADC conversion
ADC.setup()

# Infinite loop, end with Control+C
while True:
    # Read analog pin P9_40 (AIN1)
    ldr_input = ADC.read("P9_40")

    # Print its value
    print("Potenciometro:{0:1.2f}".format(ldr_input))

    # Sleep 0.01 seconds to allow the CPU to do other stuff
    time.sleep(0.1)
