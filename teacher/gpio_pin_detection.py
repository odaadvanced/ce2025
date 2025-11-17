import RPi.GPIO as GPIO

import atexit

def cleanup_gpio():
    GPIO.cleanup()

atexit.register(cleanup_gpio)

# Your GPIO setup and edge detection code here
input_pin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def my_function(channel):
    print("I was called!")
GPIO.add_event_detect(input_pin, GPIO.FALLING, callback=my_function, bouncetime=200)