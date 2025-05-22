from adafruit_pca9685 import PCA9685
import time
import board
import busio
import os


i2c = busio.I2C(board.SCL, board.SDA)
pwm = PCA9685(i2c)
pwm.frequency = 50



def set_servo_angle(channel: int, angle: float):
    """
    channel: PCA9685 channel number (0-15)
    angle: angle 0-180
    """
    pulse = int((angle / 180.0) * 2000 + 500)
    duty = int(pulse * 65535 / 20000)
    pwm.channels[channel].duty_cycle = duty
    time.sleep(0.3)


def check_command_file():
    if os.path.exists('command.txt'):
        with open('command.txt', 'r') as f:
            cmd = f.read().strip()
        os.remove('command.txt')  # Remove after reading
        if cmd in ['plastic', 'metal', 'biodegradable']:
            move_to_start(cmd)


check_command_file()


def move_trap(position: int):
    """
    position: 1 = closed (50),
              2 = open (0)
    """
    if position == 1:
        set_servo_angle(1, 50)  
    elif position == 2:
        set_servo_angle(1, 0)
    else:
        raise ValueError("Trap position must be 1 or 2")


def move_sorter(position: int):
    """
    position: 1 = 0, 
              2 = 90, 
              3 = 180
    """
    mapping = {
        1: 0,
        2: 90,
        3: 180
    }
    
    if position not in mapping:
        raise ValueError("Sorter position must be 1, 2 or 3")

    set_servo_angle(0, mapping[position])  # 1 is for soter



def move_to(label: str):
    """
    Receives label from model and moves corresponding mechanism.
    'plastic' == sorter position 1;
    'metal' == sorter position 2;
    'biodegradable' == open hatch.
    """
    if label == 'metal':
        move_sorter(1)
        time.sleep(0.1)
        move_trap(2)
        move_trap(1)
    elif label == 'plastic':
        move_sorter(2)
        time.sleep(0.1)
        move_trap(2)
        move_trap(1)
    elif label == 'biodegradable':
        move_sorter(3)
        time.sleep(0.1)
        move_trap(2)
        move_trap(1)
    else:
        move_sorter(1)
        move_trap(1)
        
