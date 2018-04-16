import Adafruit_BBIO.PWM as PWM
import time

# Servo pins are P9_14 (EHRPWM1A) and P9_16 (EHRPWM1B)
motor_pin1 = "P9_14"
motor_pin2 = "P9_16"

# Start the PWM functionality on these pins
PWM.start(motor_pin1, 0)
PWM.start(motor_pin2, 0)

# Infinite loop, end with Control+C
while True:
    # Set the motor power to 80% and
    # every 10 seconds toggle the motor direction
    PWM.set_duty_cycle(motor_pin1, 80)
    PWM.set_duty_cycle(motor_pin2, 0)
    time.sleep(10)
    PWM.set_duty_cycle(motor_pin1, 0)
    PWM.set_duty_cycle(motor_pin2, 80)
    time.sleep(10)
