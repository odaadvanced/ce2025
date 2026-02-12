from gpiozero import Button, LED
from signal import pause
led = LED(17)
button = Button(18)

def on_press():
    led.on()
    print("Button pressed")

def on_release():
    led.off()
    print("Button released")
# Attach event callbacks
button.when_pressed = on_press
button.when_released = on_release
# Pause keeps the script alive so callbacks can run
pause()