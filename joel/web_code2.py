from gpiozero import TrafficLights, Button, Device
from time import sleep

from oled_io import Oled_io

display = Oled_io()


button = Button(24)
lights = TrafficLights(27, 22, 17)


while True:
    if button.is_pressed:
        lights.green.on()
        lights.red.off()
        display.print("may cross")
        sleep(5)
        lights.amber.on()
        lights.green.off()
        display.print("dont cross")
        sleep(5)
        lights.red.on()
        lights.amber.off()
        sleep(1)
        lights.off()
    else:
        lights.red.on()
        lights.amber.off()
        lights.green.off()
        display.print("dont cross")