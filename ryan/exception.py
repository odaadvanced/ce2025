import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D17)

while True:
    try:
        temperture_c= dhtDevice.temperature
        temperture_f=temperture_c*(9/5)+32
        humidity=dhtDevice.humidity
        print("Temp: {:.1f} F/{:.1f}C Humidity: {}%".format(temperture_f,temperture_c,humidity
                                                     )
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