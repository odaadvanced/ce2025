#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

Buzzer = 17 # Set GPIO17 as LED pin #!?
BtnPin = 18 # Set GPIO18 as button pin #!


Led_status = True # Set Led status to True(OFF) #!

# Define a setup function for some setup
def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Buzzer, GPIO.OUT, initial=GPIO.HIGH)  # Set LedPin's mode to output, and initial level to high (3.3v) #!
    GPIO.setup(BtnPin, GPIO.IN) # Set BtnPin's mode to input. #!
    GPIO.output(Buzzer, 0) #!
    print('setup')
    time.sleep(3)

# Define a callback function for button callback
def swLed(ev=None):
    global Led_status #!
    # Switch led status(on-->off; off-->on)
    #Led_status = not Led_status
    Led_status = GPIO.input(BtnPin) #!
    GPIO.output(Buzzer, Led_status) #!
    print ('Led_status ' + str(not Led_status)) #!



# Define a main function for main process
def main():
    # Set up a falling detect on BtnPin,
    # and callback function to swLed
#	GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed)
    while True:
        # Don't do anything.
        swLed()
        time.sleep(0.2)

# Define a destroy function for clean up everything after
# the script finished
def destroy():
    # Turn off LED
    GPIO.output(Buzzer, GPIO.HIGH) #!
    # Release resource
    GPIO.cleanup() #!

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        main()
    # When 'Ctrl+C' is pressed, the program
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()

        import RPi.GPIO as GPIO

import time

Buzzer = 17

CL = [0, 131, 147, 165, 175, 196, 211, 248]     # Frequency of Bass tone in C major
CM = [0, 262, 294, 330, 350, 393, 441, 495]     # Frequency of Midrange tone in C major
CH = [0, 525, 589, 661, 700, 786, 882, 990]     # Frequency of Treble tone in C major

song_1 = [  CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6], # Notes of song1
            CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
            CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
            CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5] ]

beat_1 = [  1, 1, 3, 1, 1, 3, 1, 1,             # Beats of song 1, 1 means 1/8 beat
            1, 1, 1, 1, 1, 1, 3, 1,
            1, 3, 1, 1, 1, 1, 1, 1,
            1, 2, 1, 1, 1, 1, 1, 1,
            1, 1, 3 ]

song_2 = [  CM[1], CM[1], CM[1], CL[5], CM[3], CM[3], CM[3], CM[1], # Notes of song2
            CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2],
            CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1],
            CM[3], CM[2], CL[5], CL[7], CM[2], CM[1]    ]

beat_2 = [  1, 1, 2, 2, 1, 1, 2, 2,             # Beats of song 2, 1 means 1/8 beat
            1, 1, 2, 2, 1, 1, 3, 1,
            1, 2, 2, 1, 1, 2, 2, 1,
            1, 2, 2, 1, 1, 3 ]

def setup():
    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    GPIO.setup(Buzzer, GPIO.OUT)    # Set pins' mode is output
    global Buzz                     # Assign a global variable to replace GPIO.PWM
    Buzz = GPIO.PWM(Buzzer, 440)    # 440 is initial frequency.
    Buzz.start(50)                  # Start Buzzer pin with 50% duty cycle

def loop():
    while Led_Status == True:
        print ('\n    Playing song 1...')
        for i in range(1, len(song_1)):     # Play song 1
            Buzz.ChangeFrequency(song_1[i]) # Change the frequency along the song note
            time.sleep(beat_1[i] * 0.5)     # delay a note for beat * 0.5s
        time.sleep(1)                       # Wait a second for next song.

        print ('\n\n    Playing song 2...')
        for i in range(1, len(song_2)):     # Play song 1
            Buzz.ChangeFrequency(song_2[i]) # Change the frequency along the song note
            time.sleep(beat_2[i] * 0.5)     # delay a note for beat * 0.5s

    def destory():
    Led_Status == False:
        Buzz.stop ()                  # Stop the buzzer
        GPIO.output(Buzzer, 1)        # Set Buzzer pin to High
        GPIO.cleanup()                # Release resource

if __name__ == '__main__':      # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
        destory()
