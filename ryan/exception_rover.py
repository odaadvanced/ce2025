import time
import board
import adafruit_dht
import os
import sys
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask

dhtDevice = adafruit_dht.DHT11(board.D17)

rvr = SpheroRvrObserver()

def main():
    rvr.wake()
    time.sleep(2)
    rvr.reset_yaw()
    while True:
        try:
            temperture_c= dhtDevice.temperature
            temperture_f=temperture_c*(9/5)+32
            humidity=dhtDevice.humidity
            print("Temp: {:.1f} F/{:.1f}C Humidity: {}%".format(temperture_f,temperture_c,humidity
                                                         )
           )
            rvr.drive_with_heading(
            speed=10,
            heading=0,
            flags=DriveFlagsBitmask.none.value
            )

        except RuntimeError as error:
     # Errors happen fairly often, DHT'sare hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
           dhtDevice.exit()
           raise error
        
        time.sleep(2.0)
    
if __name__=='__main__':
    try:
            main()
    except KeyboardInterrupt:
            print('Program ended by KeyboardInterrupt')
            dhtDevice.exit()
            rvr.close()