import RPi.GPIO as GPIO
import time
import subprocess


# Pin setup
BUTTON_PIN = 18


# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Button listener running... Press the button to start main.py")

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            print("Button pressed! Running main.py inside venv...")

            # Full bash command: activate venv and run main.py
            subprocess.run(
                "source /home/UpetLab/garbage_sort/venv/bin/activate && python /home/UpetLab/garbage_sort/src/main.py",
                shell=True,
                executable="/bin/bash"
            )

            # Wait for button release
            while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
                time.sleep(0.1)
            print("Ready for next press.")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
