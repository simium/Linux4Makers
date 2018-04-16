import Adafruit_BBIO.PWM as PWM
import time

# Servo pin is P9_14 (EHRPWM1A)
servo_pin = "P9_14"

# Start the PWM functionality on this pin
PWM.start(servo_pin, 0)

# For each duty value in the range from 0 to 99
for duty in range(0,100):
    # Set the duty cycle value for the servo pin
    PWM.set_duty_cycle(servo_pin, duty)
    # sleep 1/5 seconds
    time.sleep(0.2)
