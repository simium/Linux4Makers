import Adafruit_BBIO.PWM as PWM
import time
from random import randint

# RGB pins are P8_13 (EHRPWM2B),
# P8_19 (EHRPWM2A) and P9_14 (EHRPWM1A)
R_pin = "P8_13"
G_pin = "P8_19"
B_pin = "P9_14"

# Start the PWM functionality on these pins
PWM.start(R_pin, 0)
PWM.start(G_pin, 0)
PWM.start(B_pin, 0)

# Infinite loop, end with Control+C
While True:
    # Every 10 seconds set the pins to a random
    # value between 0 and 100
    PWM.set_duty_cycle(R_pin, randint(0, 100))
    PWM.set_duty_cycle(G_pin, randint(0, 100))
    PWM.set_duty_cycle(B_pin, randint(0, 100))
    time.sleep(10)
