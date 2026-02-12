#pip install adafruit-circuitpython-dht  --break-system-packages
import time
import board
import adafruit_dht
import os
import sys
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask
from guizero import App, Text

# Initialize the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D19)

#create rvr object
rvr = SpheroRvrObserver()

#read and display the temperature
def update_temp():
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

        temp_text.value = "{:.1f}".format(temperature_f)
        temp_text.after(2000, update_temp) # Used to update the temperature reading
        if temperature_f <= 72:
            rvr.drive_with_heading(
                  speed=10,  # Valid speed values are 0-255
                  heading=0,  # Valid heading values are 0-359
                  flags=DriveFlagsBitmask.none.value
              )
        else :
            rvr.drive_with_heading(
                speed=10,  # Valid speed values are 0-255
               heading=0,  # Valid heading values are 0-359
               flags=DriveFlagsBitmask.drive_reverse.value
            )
 

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        temp_text.after(2000, update_temp) # Used to update the temperature reading

 
#clean up when the window is closed
def on_close():
    print ('App is closing')
    dhtDevice.exit()
    rvr.close()
    app.destroy()
    
            
def main():
    global temp_text, app
    print ('robot program started')
    rvr.wake()
# Give RVR time to wake up
    time.sleep(2)
    rvr.reset_yaw()
    app = App(title = "Thermometer", width="500", height="300")
    Text(app, text="Temp F", size=32)
    temp_text = Text(app, text="0.00", size=110)
    temp_text.after(2000, update_temp) # Used to update the temperature reading
    app.when_closed = on_close
    app.display()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program ended by KeyboardInterrupt')
        dhtDevice.exit()
        rvr.close()


