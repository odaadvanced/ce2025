#!/usr/bin/env python3
#!/usr/bin/env python3

from gpiozero import Button
from gpiozero import LED
from signal import pause
import time
# Maak Button op GPIO18 (BCM)
LedPin = 17 # Set GPIO17 as LED pin
BtnPin = 18 # Set GPIO18 as button pin

button = Button(BtnPin)
led = LED(LedPin)


Led_status = True # Set Led status to True(OFF)


# Eenvoudige callback
def on_press():
	print("Button is pressed")
# Define a setup function for some setup
# Define a callback function for button callback
	global Led_status
	# Switch led status(on-->off; off-->on)
	Led_status = not Led_status
	if Led_status:
		print ('LED OFF...')
		led.off()
	else:
		print ('...LED ON')
		led.on()

# callback
button.when_pressed = on_press

# Define a main function for main process
def main():
	# Set up a falling detect on BtnPin, 
	# and callback function to swLed
	while True:
		# Don't do anything.
		time.sleep(1)

# Define a destroy function for clean up everything after
# the script finished 
def destroy():
	# Turn off LED
	led.off()
	# Release resource
	led.close();

# If run this script directly, do:
if __name__ == '__main__':
#	setup()
	try:
		main()
	# When 'Ctrl+C' is pressed, the program 
	# destroy() will be  executed.
	except KeyboardInterrupt:
		destroy()

