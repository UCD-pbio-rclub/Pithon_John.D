# Change a RGB LED color based on temperature

# Import required modules
import RPi.GPIO as GPIO
import time, math

# Configure the Pi to use the BCM (Broadcom) pin names,
# rather than the pin positions
GPIO.setmode(GPIO.BCM)

# Setup thermoresistor
C = 0.38 # uF - Tweek this value around 0.33 to improve accuracy
R1 = 1000 # Ohms
B = 3800.0 # The thermistor constant - change this for a different thermistor
R0 = 1000.0 # The resistance of the thermistor at 25C

# Pin a charges the capacitor through a fixed 1k resistor and the thermistor in series
# pin b discharges the capacitor through a fixed 1k resistor
a_pin = 23
b_pin = 24

# Assign colors to pins
Red = 16
Green = 20
Blue = 21

# Setup RGB sensor
GPIO.setup(Red, GPIO.OUT)
GPIO.setup(Green, GPIO.OUT)
GPIO.setup(Blue, GPIO.OUT)

# Color dictionary
colors = {1 : (0,0,100), # blue
          2 : (0,33,100),
          3 : (0,66,100),
          4 : (0,100,100), # green blue
          5 : (0,100,66),
          6 : (0,100,33),
          7 : (0,100,0), # green
          8 : (33,100,0),
          9 : (66,100,0),
          10 : (100,100,0), # green red
          11 : (100,66,0),
          12 : (100,33,0),
          13 : (100,0,0) # red
          }

# Functions for the program

# empty the capacitor ready to start filling it up
def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.01)

# return the time taken for the voltage on the capacitor to count as a
#digital input HIGH than means around 1.65V
def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    GPIO.output(a_pin, True)
    t1 = time.time()
    while not GPIO.input(b_pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 1000000 # microseconds

# Take an analog reading as the time taken to charge after first discharging
# the capacitor
def analog_read():
    discharge()
    t = charge_time()
    discharge()
    return t

# Convert the time taken to charge the capacitor into a value of resistance
# To reduce errors, do it lots of times and take the average.
def read_resistance():
    n = 10
    total = 0;
    for i in range(0, n):
        total = total + analog_read()
    t = total / float(n)
    T = t * 0.632 * 3.3
    r = (T / C) - R1
    return r

def read_temp_c():
    R = read_resistance()
    t0 = 273.15     # 0 deg C in K
    t25 = t0 + 25.0 # 25 deg C in K
    # Steinhart-Hart equation - Google it
    inv_T = 1/t25 + 1/B * math.log(R/R0)
    T = (1/inv_T - t0)
    return T

# Alter color of light based on temperature manually
def color_conversion():
    temp_c = math.floor(read_temp_c())
    key =  math.floor(temp_c - 24)
    if key <= 1:
        key = 1
    elif key >= 1 and key < 4:
        key = 4
    elif key >= 4 and key < 7:
        key = 7
    elif key >= 7 and key < 10:
        key = 10
    elif key >= 10:
        key = 13
    red, green, blue = colors[key]
    return (red, green, blue)

def color_change_c():
    red, green, blue = color_conversion()
    pwmRed.ChangeDutyCycle(red)
    pwmGreen.ChangeDutyCycle(green)
    pwmBlue.ChangeDutyCycle(blue)



# Start Pulse Width Modulation (PWM) on the red, green and blue channels to
# control the brightness of the LEDs.

pwmRed = GPIO.PWM(Red, 500)
pwmRed.start(0)

pwmGreen = GPIO.PWM(Green, 500)
pwmGreen.start(0)

pwmBlue = GPIO.PWM(Blue, 500)
pwmBlue.start(0)


# Run main loop

try:
    while True:
        color_change_c()
finally:
    GPIO.cleanup()
