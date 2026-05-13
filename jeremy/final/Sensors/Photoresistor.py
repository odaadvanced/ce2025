#!/usr/bin/env python3
import RPi.GPIO as GPIO
from Sensors import ADC0834
import time

# Setup
def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    ADC0834.setup()

# Destroy
def destroy():
    GPIO.cleanup()

# Activate
def activate():
    analogVal = ADC0834.getResult()
    return analogVal

#if __name__ == '__main__':
#    setup()
#    try:
#        loop()
#    except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the program destroy() will be executed.
#        destroy()