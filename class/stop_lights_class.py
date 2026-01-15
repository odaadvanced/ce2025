from gpiozero import Button, LED, Device
import RPi.GPIO as GPIO

buzzer_bcm = 16
red_bcm = 17
green_bcm = 22
yellow_bcm = 4
button_bcm = 18

from signal import pause
import time
from oled_io import Oled_io

def setup():
    global Buzz                     # Assign a global variable to replace GPIO.PWM
    global red_light_position, red_light, green_light, yellow_light, button, display, light, is_pressed

    display = Oled_io()
    GPIO.setmode(GPIO.BCM)        # Numbers GPIOs by BCM number
    GPIO.setup(buzzer_bcm, GPIO.OUT)    # Set pins' mode is output
    Buzz = GPIO.PWM(buzzer_bcm, 440)    # 440 is initial frequency.

    red_light = LED(red_bcm, active_high=False)
    green_light = LED(green_bcm, active_high=False)
    yellow_light = LED(yellow_bcm, active_high=False)
    red_light_position = 0

    button = Button(button_bcm)
    is_pressed = False
    light = red_light_position
    button.when_released = on_release
    turn_lights_off()
    set_red_on()
 
def beep_display(text, light_wait, length):
    '''do count down and display text on screen
text = text to be displayed
light_wait = number of time units to be shown
length = time unit in seconds
'''
    for count in range(light_wait):
        display.print(text + '\n ' + str(light_wait - count))
        if light != red_light_position:
            Buzz.start(50)
            time.sleep(length/2)
            Buzz.stop()
            time.sleep(length/2)
        else:
            time.sleep(length)             

def set_red_on():
    red_light.on()
    display.print ("DO NOT CROSS")
    is_pressed = False
        
def turn_lights_off():
    green_light.off()
    red_light.off()
    yellow_light.off()

def red_light_on():
    global light
    turn_lights_off()
    red_light.on()
    beep_display ("DO NOT CROSS", 15, 0.5)
    light = light + 1
    green_light_on()
        
def yellow_light_on():
    global light
    turn_lights_off()
    yellow_light.on()
    beep_display ("DO NOT CROSS", 3, 0.5)
    light = 0
    turn_lights_off()
    set_red_on()
           
def green_light_on():
    global light
    turn_lights_off()
    green_light.on()
    beep_display ("MAY CROSS", 15, 0.5)
    light = light + 1
    yellow_light_on()
       
    
def on_release():
    
    if is_pressed == True:
        return
    
    display_lights()
    
    
def display_lights():  
    is_pressed = True

    if light == 0:
        red_light_on()       
    
    elif light == 1:
        green_light_on()
        
    elif light == 2:
        yellow_light_on() 
   
def destroy():
 
    red_light.close()
    green_light.close()
    yellow_light.close()
    button.close()
    Buzz.stop()                 # Stop the buzzer
    GPIO.output(buzzer_bcm, 1)      # Set Buzzer pin to High
    GPIO.cleanup()              # Release resource

try:
    setup()
    pause()
except KeyboardInterrupt:   # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
    destroy()