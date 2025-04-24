import RPi.GPIO as GPIO     # only for Raspberry Pi
import time

# Pinul PWM la care e conectat servo-ul
SERVO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# PWM la 50 Hz (standard for servomotors)
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)


def set_angle(angle: float):
    """Sends a PWM signal for an angle between 0 and 180°."""
    duty = 2 + (angle / 18)  # formula for SG90
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)


def move_to(label: str):
    """
    Move the servo according to the label.
    Example: plastic→30°, paper→150°.
    """
    if label == 'plastic':
        set_angle(30)
    elif label == 'paper':
        set_angle(150)
    else:
        set_angle(90)  # neutral position

