from tts import TTS
import RPi.GPIO as GPIO
import time

tts = TTS(engine="espeak")
tts.lang("en-US")
ObstaclePin = 27

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if 0 == GPIO.input(ObstaclePin):
            tts.say("Detected Barrier!")
        else:
            tts.say("no barrier")
        time.sleep(.1)
    
def destroy():
    print('exit cleanup')
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()