#!/usr/bin/env python

import RPi.GPIO as gpio
from time import sleep

# pin definitions
red = 26
blue = 24
green = 22

# select the method by which we want to identify GPIO pins
gpio.setmode(gpio.BOARD)

# set our gpio pins to OUTPUT
gpio.setup(red, gpio.OUT)
gpio.setup(green, gpio.OUT)
gpio.setup(blue, gpio.OUT)

# since the RGB led uses negative logic, we have to set them HIGH
gpio.output(red, gpio.HIGH)
gpio.output(green, gpio.HIGH)
gpio.output(blue, gpio.HIGH)

while True:
    gpio.output(red, gpio.LOW)
    sleep(.5)
    gpio.output(red, gpio.HIGH)
    sleep(.5)

    gpio.output(green, gpio.LOW)
    sleep(.5)
    gpio.output(green, gpio.HIGH)
    sleep(.5)

    gpio.output(blue, gpio.LOW)
    sleep(.5)
    gpio.output(blue, gpio.HIGH)
    sleep(.5)

gpio.cleanup()
