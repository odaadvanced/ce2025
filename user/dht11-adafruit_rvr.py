#pip install adafruit-circuitpython-dht  --break-system-packages
import time
import board
import adafruit_dht
import os
import sys
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D19)

rvr = SpheroRvrObserver()

def main():
    rvr.wake()
# Give RVR time to wake up
    time.sleep(2)
    rvr.reset_yaw()
    while True:
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

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        
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
        
        time.sleep(2.0)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program ended by KeyboardInterrupt')
        dhtDevice.exit()
        rvr.close()


