from gpiozero import Button, LED
from signal import pause
led = LED(17)
button = Button(18)
LED_status = False

def on_press():
    global LED_status
    LED_status = not LED_status
    if (LED_status == True):
        led.on()
        print ("LED On")
    else:
        led.off()
        print ("   LED off")
    
def on_release():
    led.off()
    print ("button release")

button.when_pressed = on_press


pause()
