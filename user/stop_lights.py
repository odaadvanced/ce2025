from gpiozero import Button, LED, Device
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from signal import pause
import time
from oled_io import Oled_io

display = Oled_io()
beep = TonalBuzzer(16)

red_light = LED(17)
green_light = LED(22)
yellow_light = LED(4)

button = Button(18)
is_pressed = False
light = 0

def beep_display(text, light_wait, length):
    global beep, light
    display.print(text)
    if light != 0:
        for count in range(light_wait):
            beep.play(Tone("A4"))
            time.sleep(length/2)
            beep.stop()
            time.sleep(length/2)
    else:
        time.sleep(length * light_wait)
                  

def set_red_on():
    global light, is_pressed
    red_light.off()
    beep_display ("DO NOT CROSS", 15, 0.5)
    is_pressed = False
        
def turn_lights_off():
    green_light.on()
    red_light.on()
    yellow_light.on()

def red_light_on():
    global light
    turn_lights_off()
    red_light.off()
    beep_display ("DO NOT CROSS", 15, 0.0)
    light = light + 1
    green_light_on()
        
def yellow_light_on():
    global light, is_pressed
    turn_lights_off()
    yellow_light.off()
    beep_display ("DO NOT CROSS", 3, 0.5)
    light = 0
    turn_lights_off()
    set_red_on()
           
def green_light_on():
    global light
    turn_lights_off()
    green_light.off()
    beep_display ("MAY CROSS", 15, 0.5)
    light = light + 1
    yellow_light_on()
       
    
def on_press():
    global  is_pressed
    
    if is_pressed == True:
        return
    
    display_lights()
    
    

def display_lights():
    global light, is_pressed
    
    is_pressed = True

    if light == 0:
        red_light_on()       
    
    elif light == 1:
        green_light_on()
        
    elif light == 2:
        yellow_light_on()
    
  
   
def on_release():
    led.off()
    print ("button release")



try:
    button.when_pressed = on_press
    turn_lights_off()
    set_red_on()
    pause()
finally:
    print ("closing down")
    beep.close()
    red_light.close()
    green_light.close()
    yellow_light.close()
    button.close()
    Device.close()
    
