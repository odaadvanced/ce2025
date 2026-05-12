import os
import sys
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask
import time
import board
import adafruit_dht
from guizero import App, Text

dhtDevice = adafruit_dht.DHT11(board.D17)

rvr = SpheroRvrObserver()

def update_temp():
    global app, temp_text
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9/5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C  Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
                )
            )
        temp_text.value = "{:.1f}".format(temperature_f)
        temp_text.after(2000, update_temp)
        if temperature_f <= 72:
            rvr.drive_with_heading(
                speed=10,
                heading=0,
                flags=DriveFlagsBitmask.none.value
                )
        else:
            rvr.drive_with_heading(
                speed=10,
                heading=0,
                flags=DriveFlagsBitmask.drive_reverse.value
                )

    except RuntimeError as error:
        print(error.args[0])
        temp_text.after(2000, update_temp)
    except Exception as error:
        dhtDevice.exit()
        raise error
    
    time.sleep(2.0)

def on_close():
    print('App is closing')
    dhtDevice.exit()
    rvr.close()
    app.destroy()

def main():
    global temp_text, app
    rvr.wake()
    
    time.sleep(2)
    rvr.reset_yaw()
    app = App(title = "Thermometer", width="500", height="300")
    Text(app, text="Temp F", size=32)
    temp_text = Text(app, text="0.00", size=110)
    temp_text.after(2000, update_temp)
    app.when_closed = on_close
    app.display()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program ended by keyboardInterrupt')
        dhtDevice.exit()
        rvr.close()
