# Take picture when button pressed

import time, datetime, os
import RPi.GPIO as GPIO
from picamera import PiCamera


def capture():
    now = datetime.datetime.now()
    now = '_'.join([str(now.year),str(now.month),str(now.day),
                    str(now.hour),str(now.minute),str(now.second)])
    name = now + '.jpg'
    camera.capture(name)

GPIO.setmode(GPIO.BCM)
switch_pin = 23
camera = PiCamera()
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(switch_pin) == False:
        capture()
        time.sleep(0.1)

