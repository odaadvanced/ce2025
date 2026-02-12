import os
import sys
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask
import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D17)

rvr = SpheroRvrObserver()

def main():
    rvr.wake()
    
    time.sleep(2)
    rvr.reset_yaw()
    while True:
        try:
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9/5) + 32
            humidity = dhtDevice.humidity
            print(
                "Temp: {:.1f} F / {:.1f} C  Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity
                    )
                )

        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
        
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
        
        time.sleep(2.0)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program ended by keyboardInterrupt')
        dhtDevice.exit()
        rvr.close()
