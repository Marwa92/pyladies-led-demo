#!/usr/bin/env python

import RPi.GPIO as gpio
from time import sleep

# pin definitions
pin = 8

# select the method by which we want to identify GPIO pins
gpio.setmode(gpio.BOARD)

# set our gpio pins to OUTPUT
gpio.setup(pin, gpio.OUT)

# Now get to work!
while True:

    # change the given pin to logic level HIGH
    gpio.output(pin, gpio.HIGH)

    # sleep for half a second
    sleep(.5)

    # change the pin to logic level LOW
    gpio.output(pin, gpio.LOW)

    # sleep again
    sleep(.5)
