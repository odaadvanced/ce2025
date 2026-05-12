from gpiozero import Button, LED, Buzzer
import RPi.GPIO as GPIO
from signal import pause
from PIL import Image, ImageDraw, ImageFont
import time
import adafruit_ssd1306
import board

WIDTH = 128
HEIGHT = 64

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

button = Button(25)

def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set LedPin's mode to output,and initial level to High(3.3v)
    GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH) # green LED
    GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH) # red LED
    GPIO.setup(27, GPIO.OUT, initial=GPIO.HIGH) # yellow LED

    GPIO.setup(18, GPIO.OUT)
    global Buzz
    Buzz = GPIO.PWM(18, 440)

setup()

# Function vars
activated = False

# Main function
def button_pressed():
    global activated
    print("button pressed")
    if activated == True:
        print("already activated")
        return
    else:
        print("traffic lights activated!")
        activated = True

    countdown("MAY NOT CROSS")

    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)

    countdown("MAY CROSS")

    GPIO.output(27, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    addoledtext("DO NOT CROSS")

    time.sleep(3)

    GPIO.output(22, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)

    activated = False

font = ImageFont.load_default()

def countdown(string):
    count = 16
    for x in range(1, 16):
        count -= 1
        addoledtext(f'{string}\n {count}')
        Buzz.start(5)
        time.sleep(0.1)
        Buzz.stop()
        time.sleep(.9)

# Get the size of font function
def getfontsize(font, text):
    # Calculate the size of the text in pixels
    left, top, right, bottom = font.getbbox(text)
    return right - left, bottom - top

# Adds text to oled function
def addoledtext(text):
    global oled
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    oled.fill(0)
    oled.show()
    (font_width, font_height) = getfontsize(font, text)
    draw.text(
        (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
        text,
        font=font,
        fill=255,
    )

    oled.image(image)
    oled.show()

Buzz.stop()
GPIO.output(22, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)
oled.fill(0)
oled.show()

GPIO.output(22, GPIO.LOW)
addoledtext("DO NOT CROSS")

button.when_pressed = button_pressed

pause()