import board, time
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class Oled_io:
    # Use for I2C.
    def __init__ (self, WIDTH=128, HEIGHT = 64, BORDER = 5) :
        self.i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, self.i2c, addr=0x3C)
        self.border = BORDER
        self.colon = False
    # Clear display.
        self.oled.fill(0)
        self.oled.show()

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
        self.image = Image.new("1", (self.oled.width, self.oled.height))

    # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)


    # Load default font.
        self.font = ImageFont.truetype("FreeMonoBold.ttf", 12)
     
    def clear (self):
        self.oled.fill(0)
        self.oled.show()
       
    def print(self, text):

 # Draw a smaller inner rectangle
        self.draw.rectangle(
            (self.border, self.border, self.oled.width - self.border - 1, self.oled.height - self.border - 1),
            outline=0,
            fill=0,
        )
        if self.colon == True :
            text = text.replace(':', ' ')
            
        (font_width, font_height) = self.font.getsize(text)
        self.draw.text(
            (self.oled.width // 2 - font_width // 2, self.oled.height // 2 - font_height // 2),
            text,
            font=self.font,
            fill=255,
        )
        self.oled.image(self.image)
        self.oled.show()
