#Light detecting security camera

import RPi.GPIO as GPIO
import time, math, datetime
from picamera import PiCamera

C = 0.33 # uF
R1 = 1000 # Ohms

GPIO.setmode(GPIO.BCM)

# Pin a charges the capacitor through a fixed 1k resistor and the thermistor in$
# pin b discharges the capacitor through a fixed 1k resistor 
a_pin = 18
b_pin = 23

# Set camera
camera = PiCamera()

# empty the capacitor ready to start filling it up
def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.01)
    
# return the time taken (uS) for the voltage on the capacitor to count as HIGH
# than means around 1.65V
def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    GPIO.output(a_pin, True)
    t1 = time.time()
    while not GPIO.input(b_pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 1000000

# Take an analog reading as the time taken to charge after first discharging th$
def analog_read():
    discharge()
    t = charge_time()
    discharge()
    return t
    
# To reduce errors, do it n times and take the average.
def read_resistance():
    n = 20
    total = 0;
    for i in range(1, n):
        total = total + analog_read()
    t = total / float(n)
    T = t * 0.632 * 3.3
    r = (T / C) - R1
    return r

# Take a picture
def capture():
    now = datetime.datetime.now()
    now = '_'.join([str(now.year),str(now.month),str(now.day),
                    str(now.hour),str(now.minute),str(now.second)])
    name = 'Security/' + now + '.jpg'
    camera.capture(name)

try:
    while True:
        R = read_resistance()
        if R < 0:
            for i in range(6):
                capture()
                time.sleep(5)
            while R < 0:
                R = read_resistance()
                time.sleep(30)
finally:  
    print("Cleaning up")
    GPIO.cleanup()
